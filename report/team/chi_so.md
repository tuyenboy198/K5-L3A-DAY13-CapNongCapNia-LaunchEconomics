# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200); phạm vi `noi_dia` + `hang_nang` 3,97% |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm trợ lý có mở gợi ý của trợ lý | Số `refund_request_created` có `arm = tro_ly` và có ít nhất một `agent_suggestion_shown` cùng `trace_id`, chia số `refund_request_created` có `arm = tro_ly` | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | Số `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia số đơn được kiểm trong tuần | Không cần tính |

Số tính thử bằng pandas trên `logix_requests.csv` (đọc với `keep_default_na=False`): `((dong_trong_24h == 1) & (mo_lai_trong_7_ngay == 0)).mean()`; `quyet_dinh_xem_lai.isin(['sua', 'bo']).mean()` trên 177 yêu cầu có `duoc_xem_lai == 1`; `mo_lai_trong_7_ngay.mean()`. Chỉ số trong đợt chạy thử là 82,83%, chưa so được với baseline 0,70 vì không có nhóm đối chứng.

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, depot, staff_id, arm (tro_ly / doi_chung), trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | request_id, attempt, tokens_in, tokens_out, tool_calls, status, phien_ban_bang_gia, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện cho nhân viên |
| `staff_review_decision` | Nhân viên | staff_id, quyet_dinh (giu / sua / bo), phut_xem_lai đo thật, trace_id | Khi nhân viên bấm giữ, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | staff_id, phut_lam_lai đo thật, ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua (ok / loi / bank_reject), trace_id | Khi ghi lệnh hoàn |
| `handoff_to_staff` | Agent | reason (het_lan_chay / thieu_du_lieu / ngoai_pham_vi), tom_tat, trace_id | Khi chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | request_id, closed_at, trace_id | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | request_id, reopened_at, reason, trace_id | Khi khách mở lại |
| `audit_sample_checked` | Kế toán | request_id, so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần, trên mẫu đơn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chính: `refund_request_created` (mẫu số) + `ticket_closed` trong 24 giờ + không có `ticket_reopened` trong 7 ngày, nối bằng `trace_id`. Đo được.
- Dùng (bỏ qua gợi ý): `staff_review_decision` với `quyet_dinh` là `sua` hoặc `bo`, chia tổng `staff_review_decision`. Đo được.
- An toàn (mở lại 7 ngày): `ticket_reopened` trong 7 ngày sau `ticket_closed`, chia `refund_request_created`. Đo được.
- Dùng tự đề xuất: `agent_suggestion_shown` chia `refund_request_created` có `arm = tro_ly`. Đo được.
- An toàn tự đề xuất: `audit_sample_checked` (so `so_tien_da_hoan` với `so_tien_dung`). Đo được; cần `phien_ban_bang_gia` trong `agent_run_completed` để tìm nguyên nhân.
- Chi phí mỗi việc thành công (luật dừng chi phí trong `pilot_plan.yaml`): `agent_run_completed` (token, tool) + `staff_review_decision` (phút xem lại) + `staff_rework_completed` (phút làm lại), chia số yêu cầu có `ticket_closed` không bị `ticket_reopened`. Đo được, thay cho phút `_simulated`.
- Ca hoàn trùng (luật dừng an toàn): hai `refund_ledger_write` `ket_qua = ok` cùng request_id. Đo được.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

Gốc A2: 4.472 đ/việc thành công [simulated]. Phạm vi pilot `noi_dia` + `hang_nang`: 982 yêu cầu, 900 việc thành công, 3.414 đ/việc [simulated]. Số lấy từ các dòng B1, B4, A4 của `bang_chi_phi.md` (do `src/lab13.py` tính), đã kiểm độc lập bằng tính tay trên hai file CSV: trùng khớp.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi (yếu tố nhạy nhất, B1) | +51,8%, từ 4.472 đ lên 6.787 đ/việc [simulated] | Tỉ lệ `ket_qua = lam_lai` trong phạm vi theo tuần > 7% (đợt chạy thử: 4,9% = 48/982), đếm từ `staff_review_decision` + `trace_id` | Thu hẹp về `noi_dia`, rà 20 trace làm lại gần nhất trước bước rollout kế tiếp | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài (B4) | 11.743 đ = 0,98× của 12.000 đ với 9 phút làm lại; 12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated]. Hoà vốn khi mỗi lần xem lại ≤ 5,1 phút [simulated] | % yêu cầu được xem lại > 50% ở cuối bước rollout 0,25, hoặc phút xem lại đo thật trung vị > 5 phút | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% (phạm vi chạy thử: 21,1% = 27/128) | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến (A4) | Cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng (4.599 đ = 0,38×); +2.370 đ/việc nếu còn một nửa (5.784 đ = 0,48×) [simulated] | Số việc thành công theo tuần < 50% kế hoạch (kế hoạch 33.750/tháng ≈ 7.800/tuần), đếm từ `ticket_closed` không có `ticket_reopened` | Không mở rộng pilot; đàm phán lại hợp đồng chi phí cố định | Giám đốc vận hành |
