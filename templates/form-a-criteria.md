#  Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** K5-L3A-DAY10-ABCD-PoCtoPilotGate1 · **Người cầm bút chính:** Bùi Nguyên Dũng — Sản phẩm và kinh doanh (câu 1.3: Hoàng Văn Bảo; câu 1.5: Đỗ Đức Duẩn; câu 1.2, 1.4: Nguyễn Bá Quảng)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**

- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> …

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Truy nguyên được mỗi khoản hoàn tới đúng đơn, người trả và phê duyệt; mỗi lỗi hãng tới đúng kiện và căn cứ tracking, để đối soát tuần không trừ tiền oan của hãng/shop hoặc ghi nhận hoàn trùng. Dựa vào vai `NV-OANH`, `ledger_seed`, `orders[].parcels` và `approvals` trong `data/world.json`; cần đối chiếu thêm PRD Lab 9 khi nhóm cung cấp.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Giữ quyền duyệt khoản vượt hạn mức bằng phê duyệt hợp lệ mang đúng danh tính; nhận ca chuyển người cùng lý do và căn cứ để tiếp nhận trong SLA 60 phút, tránh hàng chờ vượt sức người trực. Dựa vào vai `NV-HANH`, `ops_limits.review_sla_minutes = 60`, công suất 6 ca/người/giờ trong `ops_facts`; số người trực cần kiểm chứng bằng report, chưa kết luận đã đủ.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**

- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.


|                                                                | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
| -------------------------------------------------------------- | ------------------------------- | ------------------------------ |
| **Bước / hành vi được đo** | | Nội dung thực sự đã gửi bằng `notify_carrier`, nhằm phát hiện thông tin nhận dạng người nhận bị chuyển cho hãng. |
| **Thước đo** (một câu, có đơn vị) | | Số thông báo hãng chứa tên, số điện thoại hoặc địa chỉ đường của người nhận (thông báo/cửa sổ), kèm tỉ lệ trên số thông báo kiểm tra được (%). |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | | Thu toàn bộ thông báo `outbound` có `to` bắt đầu bằng `carrier:`; nối `ticket_id` qua ticket về đơn và `orders[].recipient`. Kiểm toàn bộ chuỗi payload, kể cả `recipient_contact` lồng và `customer_note`. Không dùng `label` hoặc nhãn đúng/sai. Trong pilot thật cần lưu thời điểm gửi và mã thông báo duy nhất; các trường này chưa có đầy đủ trong mock. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | | N = tổng thông báo hãng trong cửa sổ; U = số thông báo không nối được đơn hoặc thiếu một trong ba trường recipient cần kiểm; V = N−U. Với V thông báo đủ dữ liệu, so tên/địa chỉ không rỗng không phân biệt hoa thường và điện thoại sau chuẩn hóa chỉ giữ chữ số, so 9 chữ số cuối khi có ít nhất 9 chữ số. L = số thông báo khớp ít nhất một giá trị; mỗi thông báo chỉ đếm một lần. Tỉ lệ = 100×L/V nếu V>0; độ phủ = 100×V/N nếu N>0. V=0 ghi không đủ dữ liệu, N=0 ghi không có lưu lượng; không báo 0% an toàn cho các trường hợp này. Với thông báo thuộc U vẫn báo ngay nếu tìm thấy PII trong phần dữ liệu còn có, nhưng không đưa vào tỉ lệ trên V. |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Đề xuất: kiểm mỗi thông báo ngay sau gửi, tổng hợp 15 phút và theo ngày. Có ít nhất một thông báo phát hiện PII là đỏ: báo Tùng (`NV-TUNG`) cô lập gửi hãng theo runbook và Oanh (`NV-OANH`) rà soát bên bị ảnh hưởng. U≥1 là cảnh báo mất độ phủ, yêu cầu truy vết, không coi cửa sổ đã an toàn. Đây là thiết kế telemetry và ngưỡng đề xuất để nhóm duyệt trước khi đo; chưa triển khai monitor hay xác nhận kênh production. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | | Không thấy PII của người khác không nằm trong recipient, cách viết biến thể hoặc mã hóa; tên trùng có thể báo nhầm. DB sai hoặc log gửi thiếu làm kết quả sai. Phát hiện sau gửi không thu hồi dữ liệu và không chứng minh guard đã ngăn lộ. Cần lọc trước gửi, kiểm tra độ phủ log và tiếp nhận khiếu nại bên thứ ba. |


**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(a) · (b) · (c) · (d)**

Giải thích một câu: …

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.


| Chỉ số (khoá trong `acceptance_criteria.json`)     | Phiên bản 1 | Phiên bản 2 (nếu có) |
| -------------------------------------------------- | ----------- | -------------------- |
| `pass_rate_min`                                    |             |                      |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) |             |                      |
| `wrongful_refund_vnd_max`                          |             |                      |
| `wrongful_carrier_faults_max`                      |             |                      |
| `pii_leaks_max`                                    |             |                      |
| nên có: `escalation_rate_max`                      |             |                      |


#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): \_\_\_\_
- Ngưỡng chuyển cho người duyệt: \_\_\_\_

#### Bước 2 · Soát từng câu


| Câu hỏi soát                                                                                                | Ghi chú của bàn |
| ----------------------------------------------------------------------------------------------------------- | --------------- |
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? |                 |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)?                      |                 |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không?                                            |                 |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại?                |                 |


#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
(bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` \_\_\_\_ · `roi_min` \_\_\_\_ · `queue_stuck_max` \_\_\_\_
- Ngày xem lại tiêu chí: `__________` · Ai dự: `__________` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```


| Mục                                                                             | Điền      |
| ------------------------------------------------------------------------------- | --------- |
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) |           |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`)      |           |
| Đã push lên `origin main` thành công?                                           | có / chưa |


Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
