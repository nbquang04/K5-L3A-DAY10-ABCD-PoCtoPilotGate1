# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): ABCD
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-ABCD-PoCtoPilotGate1` (đối chiếu remote `origin`)
- Thẻ sự cố đã bốc (S1–S8): S1 (đã nhận trong commit `9d0a8b5` theo chỉ định của người dùng)

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên       | MSSV        | Vai                                    | Trưởng nhóm |
| --: | --------------- | ----------- | -------------------------------------- | :---------: |
|   1 | Hoàng Văn Bảo   | 2A202603549 | Kỹ sư cổng — guard và kiểm thử hành vi |             |
|   2 | Đỗ Đức Duẩn     | 2A202603590 | Kỹ sư cổng — đánh giá và giám sát      |             |
|   3 | Bùi Nguyên Dũng | 2A202603587 | Sản phẩm và kinh doanh                 |             |
|   4 | Nguyễn Bá Quảng | 2A202603555 | Vận hành và pháp lý; tổng hợp bài nộp  |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.


## Cá nhân

## NguyenBaQuang-2A202603555

### Phần việc phụ trách

Vận hành và pháp lý: Phiếu A câu 1.2, 1.4; Phiếu B B4–B5, B7.5–B7.6; config vận hành/pháp lý và metadata bài nộp. Vòng 2 phụ trách C3–C4, C10–C11 khi có thẻ.

### Đóng góp cụ thể

Đã dùng trợ lý AI để đọc yêu cầu, đối chiếu dữ liệu mock và code; chuẩn bị mục tiêu của Oanh/Hạnh, thiết kế telemetry PII, HAZOP tool gửi hãng, checklist chín nhóm có PIC và dự thảo runbook. Đã điền thông tin nhóm/thành viên theo TEAM và remote origin vào metadata. Các đề xuất vận hành chưa được coi là quyết định của cả nhóm; chưa áp dụng config, chưa chạy đánh giá, chưa làm phần sự cố khi chưa có thẻ.

Cập nhật sau khi nhận S1: đã nhập operations/legal trong operating_gates.json; hoàn thiện bảng runbook 1–3 và giờ cao điểm, cập nhật HAZOP theo guard hiện tại, metadata incident=S1. Giữ nguyên business của Dũng và tiêu chí đã ký. Chưa có runs/round1.lock trên máy khi cập nhật; không coi cấu hình này là bản prepared trước sự cố, chưa kết luận đạt SLA/chi phí/pháp lý. Chưa chạy eval, grade hoặc tạo checkpoint; cần Duẩn và nhóm xác minh mốc đánh giá với Coach.

### Bằng chứng

`templates/form-a-criteria.md`: A1 câu 1.2 và A2 cột Telemetry. `templates/form-b-evaluation-gates.md`: B4, B5 và dự thảo ở B7.5. `submission/submission.json`: team và bốn members. Nguồn: `data/world.json` (staff, ops_limits, ops_facts, policies), đọc tĩnh `lab10/agent.py`, `lab10/tools.py`. Chưa có mã chạy hoặc commit chứng minh kết quả đánh giá.

Đã đối chiếu thêm `docs/eval_card.md` và `docs/PRD_v1.1.md` từ repo Lab 9 `K5-L3A-DAY09-NguyenBaQuang-2A202603555-EvaluationandFailureAnalysis`: kế thừa nguyên tắc giữ dữ kiện DB, kiểm quyền/ledger và xử lý khi gate chặn; mở rộng sang PII người nhận và vận hành Lab 10. Đã ghi nguồn và giới hạn trong Phiếu A/B; không dùng report Lab 9 thay baseline Lab 10, không sao chép ngưỡng cũ. Việc đối chiếu được trợ lý AI hỗ trợ, cần tự đọc lại trước demo.

### Exit ticket

Điều rút ra khi chuẩn bị: lọc tên trường cấp ngoài không đủ nếu PII nằm trong đối tượng lồng hoặc ghi chú tự do; monitor sau gửi chỉ phát hiện, không thu hồi được dữ liệu. Điều chưa chắc: một người duyệt 6 ca/giờ có đủ ở giờ dồn ca hay không; cần report và kiểm tra chi phí/ROI sau khi tiêu chí đã ký. Cần tự rà lại và bổ sung sau demo.

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoangVanBao-2A202603549

### Phần việc phụ trách

Kỹ sư cổng — guard và kiểm thử hành vi; `lab10/guards.py`; Phiếu A mục A2 Offline; Phiếu B mục B2, B7.1–B7.3; Phiếu C mục C2, C7.

### Đóng góp cụ thể

- Thêm guard ghim policy theo ngày hiệu lực; đối chiếu hoàn tiền với tracking, policy và phê duyệt; xác minh parcel/hãng/ngày trễ trước khi ghi lỗi hãng; lọc payload gửi hãng theo allowlist.
- Bổ sung guard S1: không suy diễn tracking thiếu/mâu thuẫn thành bằng chứng khi giao nhận chưa được xác nhận; vẫn giữ xử lý ca `IN_TRANSIT` hợp lệ.
- Điền đề xuất metric offline A2, phân tích trace B2, thiết kế cổng và hai ticket hành vi B7.1–B7.3.
- Điền C2 và C7 theo gói incident S1; mã lần chạy và kết quả đánh giá vẫn chờ Duẩn cung cấp.

### Bằng chứng

- `python -m unittest discover -s tests -v`: 15 test công khai đạt sau khi thêm guard S1; các ca `T-014@*` vẫn đạt.
- Trace `T-002@55` trong test: không hoàn tiền, không ghi lỗi hãng; ticket chuyển người.
- Hai ticket hiểm B7.3 được ghi trong phiếu; chưa ghi mã adhoc hoặc report eval/grade vì Duẩn phụ trách chạy.

### Có sử dụng AI

Có — trợ lý AI hỗ trợ triển khai guard, test và biên tập phiếu; cần rà soát nội dung và xác nhận trước khi nộp.

### Exit ticket

Học được rằng lệnh ghi cần được kiểm tra lại với nguồn sự thật, không chỉ dựa trên kết quả model. Còn cần nhóm xác nhận cách xử lý các tình huống incident sau khi có thẻ và quyết định vận hành.


## Cập nhật hoàn thiện hồ sơ bằng trợ lý AI

Nguyễn Bá Quảng yêu cầu trợ lý hoàn thiện các phần còn lại: chạy grade/trace và replay, thêm guard trần hãng trước ghi tiền, kiểm quyền lợi trước trả lời từ chối, thêm monitor không dùng nhãn, điền Phiếu B/C và metadata theo bằng chứng. Các mốc ký và snapshot giữ nguyên; xem submission/evidence/review-notes.md. Quyết định đề xuất v1/v2 đều Cải tiến thêm, chưa phải phê duyệt của từng thành viên.

Bằng chứng cập nhật: grade `R-S1-grade-20261118-174856-4ee9d5`, full-scope `R-S1-after-20261118-174844-1c97cc`; 15 test công khai đạt. Đây là cập nhật thay cho các ghi chú “chờ mã chạy” ở các phần đóng góp lịch sử phía trên. Bản gom đạt đủ thành phần; grade tổng vẫn FAIL do integrity, chưa được coi đã qua lab hoặc đã được phép pilot.

### Các mục cá nhân còn cần xác nhận

## DoDucDuan-2A202603590

### Phần việc phụ trách

Đánh giá, monitor và tổng hợp bằng chứng cho Gate 1.

### Đóng góp có bằng chứng

Đã hoàn thành B0/B1 từ các report baseline, thử guard vòng 1 và prepared; điền mã lần chạy, khoảng tin cậy, ngưỡng chưa đạt, số liệu kinh doanh/vận hành, phân khúc có lỗi và khuyến nghị kết hợp tự chặn với chuyển người duyệt. Đã bổ sung monitor `carrier_fault_rate`, tính tỷ lệ trial có bản ghi lỗi hãng từ dữ liệu vận hành không nhãn.

### Exit ticket

Bài học rút ra là `carrier_fault_rate` đo tần suất ghi lỗi hãng, không cho biết lỗi đó có oan hay không. Vì vậy cần đọc chỉ số cùng guard events, độ phủ và kết quả kiểm tra để không nhầm việc chuyển nhiều ca cho người với việc đã loại bỏ rủi ro. Pilot thật vẫn cần xác nhận độ đúng của tracking và khả năng người duyệt giữ SLA vào giờ cao điểm.

### Kết quả rà soát phần việc

Phiếu C đã có C0, C1, C5, C6, C8 và C9 với mã report, số liệu prepared, các nhánh fault tree, công thức monitor và điểm mù. Cổng vòng 1 đã có snapshot. Grade S1 cuối là `FAIL`: còn lỗi visible và integrity chưa đạt. Report/journal/trace được lệnh lab sinh tự động, không chỉnh tay. Bản gom cuối đã đạt đủ thành phần theo lần kiểm tra gần nhất.

## BuiNguyenDung-2A202603587

### Phần việc phụ trách

- **Vai trò:** Sản phẩm và kinh doanh (Criteria & Business).
- **Phiếu A:** A1.1, A4, A5.
- **Phiếu B:** B3, B6, B7.4, B8.
- **Phiếu C:** C12 (phối hợp tổng hợp).
- **File:** `config/acceptance_criteria.json`, `templates/form-a-criteria.md`, `templates/form-b-evaluation-gates.md`, phần `business` của `config/operating_gates.json`, `templates/form-c-incident.md`.

### Đóng góp cụ thể

- Xây dựng tiêu chí chấp nhận, ký và đẩy tiêu chí trước khi đánh giá.
- Lập bản đồ dữ liệu, phân tích data drift và tổng hợp pre-mortem theo bốn góc nhìn.
- Đề xuất các ngưỡng kinh doanh về ngân sách hoàn tiền, chi phí LLM, phạm vi pilot và ROI.
- Phối hợp với nhóm tổng hợp quyết định Gate v1/v2.
- **Có sử dụng AI** để hỗ trợ đọc hiểu yêu cầu, phân tích dữ liệu, kiểm tra cấu hình và biên tập một số nội dung báo cáo.

### Bằng chứng

- Commit ký tiêu chí: `448ef7a` — `Sign acceptance criteria`.
- Thời gian ký: `2026-11-18T16:20:54`.
- Phiếu A: A1.1, A4, A5.
- Phiếu B: B3, B6, B7.4.
- Cấu hình: `config/acceptance_criteria.lock`, phần `business` trong `config/operating_gates.json`.

### Exit ticket

- **Điều học được:** Một hệ thống AI muốn chuyển từ PoC sang pilot cần có tiêu chí đánh giá rõ ràng, giới hạn rủi ro và các cổng kiểm soát về kinh doanh, vận hành, pháp lý; không chỉ dựa vào độ chính xác của mô hình.
- **Điều còn chưa chắc:** Cách xác định ngưỡng ROI, ngân sách và phạm vi pilot phù hợp khi triển khai trên dữ liệu thực tế thay vì dữ liệu mô phỏng.
