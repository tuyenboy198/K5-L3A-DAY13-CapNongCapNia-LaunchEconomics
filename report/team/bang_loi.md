# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Phan Sỹ Hùng (@KumaMichio) · Người gắn nhãn 2: Dương Thị Huệ (@dhuee10) (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Hệ thống | Ngầm | Không | Ngầm (đề xuất, chờ Huệ xác nhận) |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 19 / 20 = 95% (cần ≥ 16/20 = 80%). Ca không trùng: 17.

Phân bố bộ nhãn người 2: Do người dùng 4 (ca 1, 6, 9, 14) · Hệ thống 5 (ca 2, 7, 8, 15, 20) · Ngữ cảnh 4 (ca 3, 10, 16, 18) · Giới hạn hệ thống 4 (ca 4, 11, 13, 19) · Ngầm 3 (ca 5, 12, 17).

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Ca 17 (người 1: Hệ thống · người 2: Ngầm): hệ thống làm sai, nhưng 212 đơn lệch trong 9 ngày không ai mở lại và không cảnh báo nào kích. Quy tắc: lỗi do hệ thống mà chưa ai nhận ra cho tới khi kiểm tra thì gắn **Ngầm**; chỉ gắn **Hệ thống** khi lỗi đã lộ ra (khách mở lại, nhân viên bắt được, có cảnh báo). Cùng quy tắc với ca 5 và 12.

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
