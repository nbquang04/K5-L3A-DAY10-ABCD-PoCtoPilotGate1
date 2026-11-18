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

## Phân công công việc

Đây là kế hoạch phân công, không phải xác nhận đã hoàn thành. Cả nhóm thống nhất ngưỡng và quyết định v1/v2; người được giao chịu trách nhiệm ghi kết quả. Nhóm tự xác nhận trưởng nhóm trong bảng trên.

| Thành viên      | File / mục phiếu phụ trách                                                                                                                                                  | Công việc và đầu ra                                                                                                                                                                                                                                               |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hoàng Văn Bảo   | `lab10/guards.py`; Phiếu A: A2 cột Offline; Phiếu B: B2, B7.1–B7.3; Phiếu C: C2, C7                                                                                         | Thiết kế metric offline; phân tích `T-002@55`; viết 2–3 guard vòng 1; nêu hai bước tránh rò rỉ dữ liệu đánh giá; thiết kế hai ticket hiểm; phân tích lỗi sự cố và sửa guard vòng 2. Gửi yêu cầu chạy thử cho Duẩn.                                                |
| Đỗ Đức Duẩn     | `lab10/monitors.py`; Phiếu A: A3; Phiếu B: B0–B1; Phiếu C: C0–C1, C5–C6, C8–C9                                                                                              | Chạy kiểm thử và đánh giá; ghi mã lần chạy, khoảng tin cậy, so sánh ba mốc; viết specification, giả định môi trường và fault tree trước/sau; thêm ít nhất một monitor mới và đăng ký vào `MONITORS`.                                                              |
| Bùi Nguyên Dũng | `config/acceptance_criteria.json` trước khi ký; Phiếu A: A1 câu 1.1, A4–A5; Phiếu B: B3, B6, B7.4, B8; Phiếu C: C12                                                         | Tổng hợp tiêu chí, lý do chọn ngưỡng; lập bản đồ dữ liệu và ví dụ drift; tổng hợp pre-mortem bốn lăng kính; đề xuất phần `business` để Quảng nhập config; ghi quyết định v1/v2 đã được nhóm thống nhất; thực hiện ký tiêu chí, commit và push.                    |
| Nguyễn Bá Quảng | `config/operating_gates.json` (người ghi duy nhất); `submission/submission.json`; Phiếu A: A1 câu 1.2, A2 cột Telemetry; Phiếu B: B4–B5, B7.5–B7.6; Phiếu C: C3–C4, C10–C11 | Nhập phần `business` theo giá trị đã thống nhất với Dũng; phụ trách `operations`, `legal`; viết HAZOP, checklist có PIC, kế hoạch giờ cao điểm, runbook 1–5; làm phần riêng của đúng thẻ đã bốc; cập nhật risk register, metadata bài nộp và bảng thông tin nhóm. |

### Chi tiết file và việc cần làm của từng người

#### Hoàng Văn Bảo — guard và kiểm thử hành vi

| File                                   | Cần làm                                                                                                                                                                                                                                                                                      |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `lab10/guards.py`                      | Đọc hướng dẫn trong file và `lab10/helpers.py`; viết 2–3 cổng trong `pre_guard(ctx)` / `write_gate(ctx, action)` từ rủi ro đã phân tích. Kiểm tra dữ liệu và quyền trước thao tác ghi; dùng quy tắc tổng quát, không xử lý riêng mã ticket. Vòng 2 sửa tiếp file này theo nguyên nhân sự cố. |
| `templates/form-a-criteria.md`         | Điền A2 cột Offline: chọn một bước, định nghĩa thước đo, nguồn dữ liệu/nhãn, công thức, mẫu số, xử lý thiếu dữ liệu và điểm mù.                                                                                                                                                              |
| `templates/form-b-evaluation-gates.md` | Điền B2: phân loại lỗi `T-002@55`, bằng chứng trace, nguồn và hướng xử lý. B7.1: mô tả từng guard và liên hệ HAZOP/pre-mortem. B7.2: hai bước tránh rò rỉ dữ liệu đánh giá. B7.3: một tính chất và hai ticket mới, kèm kết quả Duẩn chạy.                                                    |
| `templates/form-c-incident.md`         | Điền C2: ít nhất hai lỗi có nguồn khác nhau, có một lỗi chìm; ai chịu hại và số liệu base. Điền C7: mỗi nguyên nhân gắn chỗ sửa, tầng bảo vệ, giảm hay ngăn và mã lần chạy.                                                                                                                  |

- [ ] Bàn giao guard vòng 1 trước checkpoint; guard vòng 2 trước đánh giá cuối.
- [ ] Có hai ticket hiểm để demo; các ca trước đúng vẫn đúng sau sửa, theo report Duẩn cung cấp.

#### Đỗ Đức Duẩn — chạy đánh giá và monitor

| File                                                                                 | Cần làm                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `lab10/monitors.py`                                                                  | Thêm ít nhất một hàm monitor mới, nhận dữ liệu trial không có nhãn và trả về số; đăng ký trong `MONITORS`. Chỉ số phải phát hiện được tín hiệu liên quan sự cố, không chỉ dùng lại `escalation_rate`.                                                                                                      |
| `templates/form-a-criteria.md`                                                       | Điền A3: chọn kết luận từ số minh họa về khoảng tin cậy và giải thích.                                                                                                                                                                                                                                     |
| `templates/form-b-evaluation-gates.md`                                               | Điền B0 ít nhất ba lần chạy: baseline, thử guard vòng 1, prepared; ghi mã, khoảng tin cậy và kết luận. B1: ngưỡng chưa đạt, số kinh doanh/vận hành, phân khúc xấu nhất và khuyến nghị tự chặn/người duyệt/kết hợp.                                                                                         |
| `templates/form-c-incident.md`                                                       | C0: nhật ký vòng 2. C1: prepared đỡ được gì, còn vượt trần gì, đối chiếu pre-mortem. C5: specification kiểm được và giả định môi trường. C6/C9: cây nguyên nhân trước/sau, ít nhất hai nhánh ở hai tầng, bằng chứng tại lá và nhánh còn hở. C8: công thức monitor, dữ liệu, ngưỡng, điểm mù và giá trị đo. |
| `runs/`                                                                              | Cho lệnh tự sinh report, trace và `journal.jsonl`; lấy số liệu để bàn giao, không sửa tay. Chạy baseline chỉ sau khi Dũng báo tiêu chí đã ký và push. Chạy grade ngay khi nhận thẻ, trước mọi sửa vòng 2.                                                                                                  |
| `lab10/guards_round1.py`, `config/operating_gates.round1.json`, `config/round1.lock` | Sinh bằng `python -m lab10.checkpoint` sau khi Bảo và Quảng bàn giao vòng 1; không tự viết hoặc sửa các bản chốt.                                                                                                                                                                                          |
| `submission/manifest.json` và các file được gom                                      | Sinh bằng `python -m lab10.check_submission --collect` sau khi phiếu và metadata hoàn chỉnh; sửa nguyên nhân thiếu ở file nguồn rồi gom lại.                                                                                                                                                               |

- [ ] Test công khai đạt; có report base, prepared, after và mã chạy để mọi người trích dẫn.
- [ ] Monitor mới có tín hiệu; kiểm tra integrity, criteria, visible, regression và các trần; báo trung thực mục còn chưa đạt.
- [ ] Bản gom cuối chạy trên đúng code/config cuối và in `ĐỦ THÀNH PHẦN`.

#### Bùi Nguyên Dũng — tiêu chí và kinh doanh

| File                                   | Cần làm                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `config/acceptance_criteria.json`      | Trước khi đánh giá: điền `team` đúng tên repo, `signed_by`, năm ngưỡng `required`, `nice_to_have.escalation_rate_max`, ba ngưỡng `business_ops`, `stop_condition` và đủ bốn dòng `decision_rule`. Dựa vào dữ kiện, không chép ngưỡng example. Sau khi nhóm duyệt: ký, commit, push rồi giữ nguyên file.                         |
| `templates/form-a-criteria.md`         | A1 câu 1.1: mục tiêu cấp hệ thống. A4: tiêu chí có hành động khi trượt, bốn câu soát, hai ranh giới đầu ra, ngưỡng kinh doanh và ngày xem lại. A5: thời gian ký, commit và xác nhận push.                                                                                                                                       |
| `templates/form-b-evaluation-gates.md` | B3: bản đồ dữ liệu, nguồn sự thật/bản sao, drift cụ thể và chỉ số phát hiện. B6: tổng hợp ý kiến đủ bốn lăng kính, chọn 2–3 lý do thành cổng. B7.4: giá trị `business` và lý do có số từ `ops_limits`, `ops_facts`; gửi Quảng nhập config. B8: quyết định v1, ba bằng chứng, quy tắc đã ký, phân khúc xấu nhất và ngày xem lại. |
| `templates/form-c-incident.md`         | C12: quyết định v2, mã ba mốc, ba bằng chứng, so với v1, rủi ro chưa đo và ngày xem lại. Viết ba câu bắt buộc về giả định môi trường, giảm/ngăn tác hại và điều cần đo trong pilot thật; gửi nguyên văn cho Quảng.                                                                                                              |
| Git của repo nhóm                      | Commit/push tiêu chí trước đánh giá; commit/push bản chốt và v1; commit/push bài cuối sau khi Duẩn gom đủ. Không push lên upstream.                                                                                                                                                                                             |

- [ ] Mỗi ngưỡng và đề xuất kinh doanh có lý do để giải thích khi demo.
- [ ] Quyết định v1/v2 do cả nhóm thống nhất, khớp `decision_rule` và report; không chọn Tiếp tục khi còn ngưỡng bắt buộc chưa đạt hoặc vượt trần.

#### Nguyễn Bá Quảng — vận hành, pháp lý và bài nộp

| File                                   | Cần làm                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `config/operating_gates.json`          | Là người ghi duy nhất. Nhập `business` đã thống nhất với Dũng: trần hoàn/ngày, ngân sách máy/ticket, phạm vi và ROI. Điền `operations`: PIC, approver, số người trực, công suất, hạn chờ, điều kiện dừng, kênh báo; vòng 2 điều chỉnh ghi chú giải thích/kiểm mẫu nếu cần. Điền `legal`: trường PII bị chặn và yêu cầu nguyên nhân ghi lỗi hãng. Tên/mã nhân viên và số liệu phải dựa vào `data/world.json`. |
| `templates/form-a-criteria.md`         | A1 câu 1.2: mục tiêu của chị Oanh và chị Hạnh. A2 cột Telemetry: tín hiệu thiệt hại bên thứ ba, dữ liệu không nhãn, công thức, khung thời gian, ngưỡng báo và điểm mù.                                                                                                                                                                                                                                       |
| `templates/form-b-evaluation-gates.md` | B4: HAZOP một tool ghi, ít nhất ba dòng kỹ thuật và thêm ít nhất hai dòng ngoài kỹ thuật, có nhánh chưa thấy trên trace. B5: đủ chín nhóm việc, trạng thái, bằng chứng, PIC có tên. B7.5: runbook 1–3, cách dừng và hạn dừng. B7.6: giờ cao điểm, người trực, ngưỡng gọi thêm người/thu hẹp và tác động chi phí.                                                                                             |
| `templates/form-c-incident.md`         | Ghi số thẻ ở đầu phiếu. C3 chỉ làm phần đúng thẻ; S4 dùng C1 và B7.6. C4: HAZOP sự cố ít nhất ba dòng, có nhánh chưa thấy trên trace. C10: ít nhất một rủi ro có PIC, metric/ngưỡng và hành động. C11: cập nhật checklist, runbook 4–5; nêu ai liên hệ bên chịu hại và thời hạn.                                                                                                                             |
| `submission/submission.json`           | Điền `team` giống hệt tên repo/tiêu chí; đủ bốn `members` dạng `HoVaTen-MSSV`; đúng `incident`; v1/v2 khớp phiếu; chép nguyên ba câu C12 vào `three_lines`.                                                                                                                                                                                                                                                  |
| `TEAM.md`                              | Hoàn thiện thông tin nhóm, tên repo, lớp, thẻ và bảng thành viên theo thông tin được xác nhận; nhắc từng người hoàn thiện mục cá nhân và nộp LMS. Không viết thay đóng góp cá nhân.                                                                                                                                                                                                                          |

- [ ] Số liệu trong config, runbook và phiếu khớp nhau; PIC có tên, có hạn dừng và đường xử lý ticket còn chờ.
- [ ] Metadata đủ và khớp phiếu; bàn giao cho Duẩn gom bài, không sửa bản sao trong `submission/docs/`.

### Quy tắc tránh trùng việc

- Mỗi người chỉ sửa mục phiếu được giao; giữ nguyên cấu trúc, câu hỏi và không format lại toàn bộ file dùng chung.
- Chỉ Quảng ghi `config/operating_gates.json`; Dũng gửi giá trị phần `business` kèm lý do để Quảng nhập.
- Chỉ Duẩn chạy `unittest`, `eval`, `trace`, `gate`, `checkpoint`, `grade` và `check_submission`; các thành viên gửi yêu cầu thử và cùng đọc bằng chứng.
- Chỉ Dũng chạy lệnh ký tiêu chí, commit và push trên máy chung; mọi người lưu xong và báo trước khi commit.
- Cả bốn cùng góp ý pre-mortem và duyệt ngưỡng, v1/v2; Dũng ghi kết luận đã thống nhất.
- Mỗi người tự viết mục cá nhân trong `TEAM.md`: đóng góp thực tế, bằng chứng, việc có dùng AI và exit ticket. Không ghi công việc dự kiến thành đóng góp đã hoàn thành.
- Không sửa tiêu chí sau khi ký, bản chốt vòng 1, file bị khóa hoặc kết quả trong `runs/` bằng tay.

### Thứ tự bàn giao

1. Bảo và Quảng hoàn thiện phần đo lường; Dũng tổng hợp tiêu chí để cả nhóm duyệt, ký, commit và push. Sau khi push thành công, Duẩn mới chạy baseline.
2. Duẩn bàn giao baseline và trace; Bảo phân tích lỗi, Dũng và Quảng hoàn thiện phân tích rủi ro và cấu hình vòng 1.
3. Bảo bàn giao guard, Quảng bàn giao config; Duẩn kiểm thử, chốt vòng 1 và đánh giá `prepared`; Dũng ghi v1, commit và push trước khi nhận sự cố.
4. Khi nhận đúng thẻ đã bốc, Quảng ghi số thẻ ở đầu Phiếu C; Duẩn chạy `grade --incident Sx` trước khi bất kỳ ai sửa vòng 2.
5. Bảo sửa guard, Duẩn thêm monitor, Dũng đề xuất thay đổi kinh doanh, Quảng cập nhật config và quy trình. Duẩn đánh giá sau từng thay đổi và kiểm tra regression.
6. Duẩn bàn giao report cuối; cả nhóm chốt v2, Dũng ghi C12; Quảng điền `submission.json`; Duẩn gom bài tới khi `ĐỦ THÀNH PHẦN`; Dũng commit và push.
7. Sau demo, trả các giá trị thử về bản v2 nếu có thay đổi; Duẩn chạy lại grade và gom bài, Dũng push bản cuối. Mỗi thành viên tự nộp link repo trên LMS.

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
- Thêm regression test cho `T-002@55`, kiểm tra không hồi quy bộ nền và kiểm tra loại PII khỏi thông báo hãng.
- Điền đề xuất metric offline A2, phân tích trace B2, thiết kế cổng và hai ticket hành vi B7.1–B7.3.
- C2 và C7 còn chờ gói incident đúng thẻ; không ghi nguyên nhân hoặc kết quả chạy chưa có.

### Bằng chứng

- `python -m unittest discover -s tests -v`: 15 test đạt.
- Trace `T-002@55` trong test: không hoàn tiền, không ghi lỗi hãng; ticket chuyển người.
- Hai trace adhoc trong B7.3: một ca chèn chỉ thị bị chuyển người, một ca hợp lệ gửi thông báo hãng đã lọc PII.
- Chưa có mã commit hoặc `runs/<mã>`: tiêu chí chưa ký nên chưa chạy `lab10.eval`; chưa nhận gói incident để chạy grade.

### Có sử dụng AI

Có — trợ lý AI hỗ trợ triển khai guard, test và biên tập phiếu; cần rà soát nội dung và xác nhận trước khi nộp.

### Exit ticket

Học được rằng lệnh ghi cần được kiểm tra lại với nguồn sự thật, không chỉ dựa trên kết quả model. Còn cần nhóm xác nhận cách xử lý các tình huống incident sau khi có thẻ và quyết định vận hành.
