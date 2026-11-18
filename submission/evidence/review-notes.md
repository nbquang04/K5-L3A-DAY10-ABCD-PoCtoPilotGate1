# Kiểm chứng và giới hạn hồ sơ Gate 1

Grade cuối: `R-S1-grade-20261118-174856-4ee9d5`. Quyết định soạn từ bằng chứng: Cải tiến thêm, chưa cho pilot thật.

- Criteria, visible, regression, monitor đạt; integrity chưa đạt, hidden không có. Các ngưỡng xanh không thay thế điều kiện integrity.
- Diagnostic hash chỉ đọc: {'CRLF_only': 22, 'missing': 28, 'different': 1}. `CRLF_only` nghĩa là thay CRLF bằng LF trong bộ nhớ thì khớp manifest, không khẳng định file đã được sửa hoặc được Coach chấp thuận. Không sửa file khóa/manifest để lấy PASS.
- Chỉ lấy S1 theo cách Coach hướng dẫn; 28 file S2–S8 thiếu nhưng manifest tham chiếu. Không tải/đọc thẻ khác để sửa số kiểm.
- tests/test_public.py khác manifest ngoài newline; cần Coach cung cấp bản gốc/phát hành khớp. Không thay test hoặc manifest của bộ chấm.
- Tiêu chí ký 16:20:54, commit 448ef7a 16:21:45; journal cũ có grade S1 16:42:42; nhận S1 commit 16:45:30; checkpoint 17:05:30. Không hồi tố v1 hoặc khẳng định prepared trước khi biết S1. B8 là bản bổ sung hồi cứu.
- Journal cũ từ submission được phục hồi nguyên dòng và hợp nhất với các dòng máy sinh mới, loại trùng run_id; không tạo dòng đánh giá giả. Report cũ chưa có trên máy không được tái tạo dưới ID cũ; replay có ID mới.
- Full-scope `R-S1-after-20261118-174844-1c97cc`: 65/65 trial đạt, 0 hoàn sai/under-refund/lỗi oan/PII; chi phí CT 10562đ, DN 10564đ > 10000đ làm tay. Không mở rộng chỉ vì pass=1.
- HN cuối: S1 25/25 trial, 8724đ/ticket, ROI 0,15, coverage 38,46%; nền 40/40 trial, 8102đ, ROI 0,23, coverage 36,36%, escalation 37,5% > mức nên có 30%. Phân khúc kho ? nền 10359đ là ca chuyển người thiếu đơn/kho, vẫn theo dõi; không che số liệu này bằng trung bình.
- Mục cá nhân và chữ ký thực tế cần từng thành viên tự xác nhận. Trợ lý hỗ trợ biên tập, không giả lập duyệt thủ công hoặc demo đã diễn ra.

## Nội dung cần trình Coach

Xác nhận nguồn manifest cho gói S1-only, newline Windows và file test; xác nhận cách tính prepared khi nhận thẻ/chạy sự cố trước checkpoint. Giữ các file hiện có để đối chiếu, không sửa lịch sử. Đây là điều kiện còn chờ xác minh ngoài khả năng hoàn tất kỹ thuật trong workspace.
