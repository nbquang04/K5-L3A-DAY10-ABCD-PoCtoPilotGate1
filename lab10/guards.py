"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H
from .tools import Verdict


def _order_and_policy(ctx, action):
    ticket_id = ctx.ticket.get("ticket_id")
    order_id = ctx.ticket.get("order_id")
    if action.get("ticket_id") != ticket_id or action.get("order_id") != order_id:
        return None, None

    order = ctx.tools.lookup_order(order_id)
    if order is None or order.get("customer_id") != ctx.ticket.get("customer_id"):
        return None, None

    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    return order, policy


def pre_guard(ctx):
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return Verdict.escalate("không tìm thấy chính sách có hiệu lực tại ngày xử lý")
    return Verdict.allow(policy_id=policy["policy_id"])


def _confirmed_parcel(order, ctx, allow_in_transit=False):
    parcels = order.get("parcels") or []
    if not parcels:
        return None, "đơn không có kiện để đối chiếu độ trễ"

    parcel = max(parcels, key=lambda p: H.db_delay_days(p, ctx.as_of))
    if not parcel.get("delivered_date"):
        if not allow_in_transit or parcel.get("status") != "IN_TRANSIT":
            return None, "tracking chưa có ngày giao nhận xác nhận; không tự hoàn hoặc ghi lỗi hãng"
    if not parcel.get("delay_cause"):
        return None, "tracking chưa ghi nguyên nhân trễ; không tự hoàn hoặc ghi lỗi hãng"
    if parcel.get("status") not in (None, "DELIVERED") and not (
            allow_in_transit and parcel.get("status") == "IN_TRANSIT"):
        return None, "trạng thái kiện không xác nhận đã giao nhận"
    return parcel, None


def write_gate(ctx, action):
    tool = action.get("tool")

    if tool == "send_reply":
        plan = next((e for e in ctx.events if e.get("type") == "llm_extract"), {})
        if plan.get("intent") == "LATE" and not ctx.tools.ledger_rows(ticket_id=ctx.ticket.get("ticket_id")):
            order = ctx.tools.lookup_order(ctx.ticket.get("order_id"))
            policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
            if order and policy and order.get("customer_id") == ctx.ticket.get("customer_id"):
                parcel, error = _confirmed_parcel(order, ctx, allow_in_transit=True)
                if parcel and H.entitlement_vnd(policy, order, H.db_delay_days(parcel, ctx.as_of), parcel.get("delay_cause")) > 0:
                    ctx.log("unpaid_entitlement", order_id=order["order_id"])
                    return Verdict.escalate("tracking xác nhận quyền hoàn nhưng sổ chưa ghi; người duyệt kiểm trước khi trả lời từ chối")

    if tool == "issue_refund":
        order, policy = _order_and_policy(ctx, action)
        if order is None or policy is None:
            return Verdict.escalate("không xác minh được đơn, chủ đơn hoặc chính sách hiện hành")

        if ctx.tools.ledger_rows(ticket_id=action["ticket_id"]):
            return Verdict.deny("ticket đã có khoản hoàn; không ghi hoàn lần hai")

        parcel, tracking_error = _confirmed_parcel(order, ctx, allow_in_transit=True)
        if parcel is None:
            ctx.log("incomplete_tracking", reason=tracking_error)
            return Verdict.escalate(tracking_error)
        delay = H.db_delay_days(parcel, ctx.as_of)
        cause = parcel.get("delay_cause")
        entitled = H.entitlement_vnd(policy, order, delay, cause)
        if entitled <= 0:
            return Verdict.escalate("dữ liệu tracking và chính sách không xác nhận quyền hoàn")

        strike_cap = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
        strikes = ctx.tools.fault_rows(carrier_id=parcel.get("carrier_id"))
        if (strike_cap is not None and len(strikes) >= strike_cap
                and H.carrier_at_fault(policy, parcel, delay)):
            ctx.log("carrier_strike_limit", carrier_id=parcel.get("carrier_id"), count=len(strikes))
            return Verdict.escalate("hãng đã chạm trần lỗi tự động trong ngày; chuyển người trước khi ghi tiền")

        amount = action.get("amount_vnd")
        if type(amount) is not int or amount <= 0:
            return Verdict.escalate("số tiền hoàn không hợp lệ")
        if amount > entitled:
            amount = entitled
        elif amount < entitled:
            return Verdict.escalate("số tiền đề xuất không khớp quyền lợi; cần người duyệt")

        approval_id = action.get("approval_id")
        needs_approval = amount > policy["auto_limit_vnd"] or action.get("payer", "LOGIX") != "LOGIX"
        if needs_approval:
            approvals = ctx.tools.lookup_approvals(
                approval_id=approval_id, order_id=order["order_id"],
                customer_id=order["customer_id"], status="valid",
            ) if approval_id else []
            if not any(
                approval.get("ticket_id") == ctx.ticket.get("ticket_id")
                and approval.get("expires_at", "") >= ctx.as_of
                and approval.get("max_vnd", 0) >= amount
                for approval in approvals
            ):
                return Verdict.escalate("thiếu phê duyệt còn hạn, đúng ticket và đủ hạn mức")
        return Verdict.modify(
            "đã đối chiếu số tiền với tracking và chính sách hiện hành",
            amount_vnd=amount,
        ) if amount != action.get("amount_vnd") else Verdict.allow()

    if tool == "file_carrier_fault":
        order, policy = _order_and_policy(ctx, action)
        if order is None or policy is None:
            return Verdict.escalate("không xác minh được đơn, chủ đơn hoặc chính sách hiện hành")

        parcel, tracking_error = _confirmed_parcel(order, ctx, allow_in_transit=True)
        if parcel is None:
            ctx.log("incomplete_tracking", reason=tracking_error)
            return Verdict.deny(tracking_error)
        delay = H.db_delay_days(parcel, ctx.as_of)
        if not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny("tracking không xác nhận độ trễ và nguyên nhân thuộc trách nhiệm hãng")
        strike_cap = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
        if strike_cap is not None and len(ctx.tools.fault_rows(carrier_id=parcel.get("carrier_id"))) >= strike_cap:
            return Verdict.deny("đã đạt trần ghi lỗi tự động của hãng trong ngày; chờ người xác minh")
        if any((
            action.get("parcel_id") != parcel["parcel_id"],
            action.get("carrier_id") != parcel["carrier_id"],
            action.get("driver_id") != parcel.get("driver_id"),
            action.get("delay_days") != delay,
        )):
            return Verdict.modify(
                "đã đối chiếu kiện, hãng và độ trễ với tracking",
                parcel_id=parcel["parcel_id"],
                carrier_id=parcel["carrier_id"],
                driver_id=parcel.get("driver_id"),
                delay_days=delay,
            )
        return Verdict.allow()

    if tool == "notify_carrier":
        if action.get("ticket_id") != ctx.ticket.get("ticket_id"):
            return Verdict.deny("ticket không khớp với thông báo gửi hãng")
        order_id = ctx.ticket.get("order_id")
        order = ctx.tools.lookup_order(order_id)
        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        if (order is None or policy is None
                or order.get("customer_id") != ctx.ticket.get("customer_id")):
            return Verdict.deny("không xác minh được đơn, chủ đơn hoặc chính sách hiện hành")

        fault = next((
            row for row in ctx.tools.fault_rows(ticket_id=action["ticket_id"])
            if row.get("order_id") == order["order_id"]
            and row.get("carrier_id") == action.get("carrier_id")
        ), None)
        if fault is None:
            return Verdict.deny("chỉ thông báo hãng sau khi đã ghi lỗi hãng có căn cứ")

        source_fields = {
            "order_id": order["order_id"],
            "parcel_id": fault["parcel_id"],
            "district": (order.get("recipient") or {}).get("district"),
            "delay_days": fault["delay_days"],
        }
        allowed = set(policy.get("carrier_notice_fields", [])) & set(source_fields)
        payload = {key: source_fields[key] for key in allowed if source_fields[key] is not None}
        if action.get("payload") != payload:
            return Verdict.modify(
                "thông báo hãng chỉ chứa trường cho phép lấy từ nguồn sự thật",
                payload=payload,
            )

    return Verdict.allow()
