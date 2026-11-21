# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Phan Sỹ Hùng (@KumaMichio) · Người gắn nhãn 2: Dương Thị Huệ (@dhuee10) (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | _chờ Hùng_ | Do người dùng | _chờ so_ | _chờ gộp_ |
| 2 | _chờ Hùng_ | Hệ thống | _chờ so_ | _chờ gộp_ |
| 3 | _chờ Hùng_ | Ngữ cảnh | _chờ so_ | _chờ gộp_ |
| 4 | _chờ Hùng_ | Giới hạn hệ thống | _chờ so_ | _chờ gộp_ |
| 5 | _chờ Hùng_ | Ngầm | _chờ so_ | _chờ gộp_ |
| 6 | _chờ Hùng_ | Do người dùng | _chờ so_ | _chờ gộp_ |
| 7 | _chờ Hùng_ | Hệ thống | _chờ so_ | _chờ gộp_ |
| 8 | _chờ Hùng_ | Hệ thống | _chờ so_ | _chờ gộp_ |
| 9 | _chờ Hùng_ | Do người dùng | _chờ so_ | _chờ gộp_ |
| 10 | _chờ Hùng_ | Ngữ cảnh | _chờ so_ | _chờ gộp_ |
| 11 | _chờ Hùng_ | Giới hạn hệ thống | _chờ so_ | _chờ gộp_ |
| 12 | _chờ Hùng_ | Ngầm | _chờ so_ | _chờ gộp_ |
| 13 | _chờ Hùng_ | Giới hạn hệ thống | _chờ so_ | _chờ gộp_ |
| 14 | _chờ Hùng_ | Do người dùng | _chờ so_ | _chờ gộp_ |
| 15 | _chờ Hùng_ | Hệ thống | _chờ so_ | _chờ gộp_ |
| 16 | _chờ Hùng_ | Ngữ cảnh | _chờ so_ | _chờ gộp_ |
| 17 | _chờ Hùng_ | Ngầm | _chờ so_ | _chờ gộp_ |
| 18 | _chờ Hùng_ | Ngữ cảnh | _chờ so_ | _chờ gộp_ |
| 19 | _chờ Hùng_ | Giới hạn hệ thống | _chờ so_ | _chờ gộp_ |
| 20 | _chờ Hùng_ | Hệ thống | _chờ so_ | _chờ gộp_ |

**Tỉ lệ đồng thuận:** _chờ so nhãn_ / 20 = _…_% (cần ≥ 16/20 = 80%)

Phân bố bộ nhãn người 2: Do người dùng 4 (ca 1, 6, 9, 14) · Hệ thống 5 (ca 2, 7, 8, 15, 20) · Ngữ cảnh 4 (ca 3, 10, 16, 18) · Giới hạn hệ thống 4 (ca 4, 11, 13, 19) · Ngầm 3 (ca 5, 12, 17).

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- _Điền sau khi so nhãn với người gắn nhãn 1 (mỗi ca không trùng một câu quy tắc)._

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

Bảng nháp theo bộ nhãn người 2; chốt lại sau khi gộp nếu nhãn thống nhất của ca nào khác đi.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `refund_ledger_write` có `ket_qua = bank_reject` lý do sai số tài khoản, theo `trace_id`; cảnh báo khi > 1% lệnh hoàn trong ngày | Kiểm độ dài, định dạng số tài khoản ngay ở form; tra tên chủ tài khoản qua ngân hàng và bắt khách xác nhận trước khi tạo lệnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát hằng ngày: tin "đã hoàn thành công" mà không có `refund_ledger_write` `ket_qua = ok` cùng `trace_id`; ngưỡng > 0 ca/ngày là báo động | Chỉ gửi tin thành công sau khi sổ cái xác nhận; API lỗi (503) sau 3 lần thì `handoff_to_staff` và báo khách "đang xử lý" | Trưởng nhóm kỹ thuật trợ lý |
| 18 | Ngữ cảnh | `ticket_reopened` lý do "hoàn thiếu" trong khi kiểm tra cho thấy số tiền đúng; theo dõi theo tuần, ngưỡng > 2% yêu cầu đã đóng | Mẫu tin nhắn luôn ghi cách tính (VD: phí 30.000 đ × 50% = 15.000 đ, điều khoản áp dụng) | PM trợ lý hoàn phí |
| 13 | Giới hạn hệ thống | Mỗi tuần lấy mẫu 50 hội thoại có ý định ngoài phạm vi (bảo hiểm, hãng khác); ngưỡng: > 0 ca trợ lý trả lời mà không có `handoff_to_staff` | Thêm bộ phân loại phạm vi; ngoài phạm vi thì nói rõ "trợ lý không xử lý được", chuyển nhân viên hoặc đưa đầu mối của đối tác bảo hiểm | Trưởng nhóm CSKH |
| 17 | Ngầm | Event `audit_sample_checked` hằng tuần trên 200 đơn: so `so_tien_da_hoan` với `so_tien_dung`; ngưỡng lệch > 1% số đơn hoặc lặp ở cùng nhóm đơn. Ghi `phien_ban_bang_gia` vào `agent_run_completed` để so với bản hiện hành | Xoá bộ nhớ đệm bảng giá mỗi khi bảng giá đổi; từ chối chạy nếu phiên bản bảng giá cũ hơn bản hiện hành; hoàn bù 212 đơn đã lệch | Kế toán trưởng (đối soát) |
