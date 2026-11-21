# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | ... |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | ... |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | ... |
| Dùng | Nhóm tự đề xuất: ... | ... | Không cần tính |
| An toàn | Nhóm tự đề xuất: ... | ... | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- ...

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

Gốc A2: 4.472 đ/việc thành công [simulated]. Phạm vi pilot `noi_dia` + `hang_nang`: 982 yêu cầu, 900 việc thành công, 3.414 đ/việc [simulated]. Số được kiểm độc lập bằng tính tay (script thư viện chuẩn đọc hai file CSV), khớp các dòng B1, B4, A4 của `bang_chi_phi.md`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi (yếu tố nhạy nhất, B1) | +51,8%, từ 4.472 đ lên 6.787 đ/việc [simulated] | Tỉ lệ `ket_qua = lam_lai` trong phạm vi theo tuần > 7% (đợt chạy thử: 4,9% = 48/982), đếm từ `staff_review_decision` + `trace_id` | Thu hẹp về `noi_dia`, rà 20 trace làm lại gần nhất trước bước rollout kế tiếp | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài (B4) | 11.743 đ = 0,98× của 12.000 đ với 9 phút làm lại; 12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated]. Hoà vốn khi mỗi lần xem lại ≤ 5,1 phút [simulated] | % yêu cầu được xem lại > 50% ở cuối bước rollout 0,25, hoặc phút xem lại đo thật trung vị > 5 phút | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% (phạm vi chạy thử: 21,1% = 27/128) | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến (A4) | Cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng (4.599 đ = 0,38×); +2.370 đ/việc nếu còn một nửa (5.784 đ = 0,48×) [simulated] | Số việc thành công theo tuần < 50% kế hoạch (kế hoạch 33.750/tháng ≈ 7.800/tuần), đếm từ `ticket_closed` không có `ticket_reopened` | Không mở rộng pilot; đàm phán lại hợp đồng chi phí cố định | Giám đốc vận hành |
