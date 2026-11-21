# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: CapNongCapNia · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc (978 việc), gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ) [simulated]. Phạm vi `noi_dia` + `hang_nang`: 3.414 đ, cộng cố định 40 triệu đ/tháng thành 4.599 đ [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (× 2: +51,8%) · 2. Tỉ lệ xem lại (× 2: +40,7%) · 3. Lương nhân viên (+25%: +23,1%) [simulated]. Giá token × 2 chỉ +5,6% | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ (đã cộng 222 ca nhân viên làm thay) [simulated]. Theo loại: `noi_dia` 0,22× · `hang_nang` 0,69× · `doi_tac` 0,85× · `quoc_te` 1,88× → pilot chỉ `noi_dia` + `hang_nang`. Bất lợi: xem lại 100% còn 0,98×–1,03× [simulated] | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử: chính 82,83% (994/1.200) · bỏ qua gợi ý 27,12% (48/177) · mở lại 7 ngày 4,25% (51/1.200). Không có đối chứng nên chưa nói được trợ lý làm chỉ số thay đổi. 10 event có `trace_id`, mọi chỉ số đều tính được từ event | Xong, có bằng chứng (`chi_so.md`) | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Bảng khắc phục 5 ca đủ 5 loại (ca 1, 7, 18, 13, 17), mỗi dòng có event, ngưỡng, vai trò. Tỉ lệ đồng thuận chờ bộ nhãn người 1 (cần ≥ 16/20) | Chưa (chờ so nhãn) | Trưởng nhóm kỹ thuật trợ lý |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, ngẫu nhiên phân tầng theo depot; mde 6 điểm, 859/nhóm, DE 6,96, m ≥ 299; 3 luật dừng; quyết định 2027-01-12. Bất lợi: nếu tác động thật chỉ 5 điểm thì power 0,64 | Xong, có bằng chứng (`pilot_plan.yaml`) | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại × 2: 6.787 đ (+51,8%) · xem lại 100%: 0,98×–1,03×, hoà vốn khi xem lại ≤ 5,1 phút · khối lượng còn một nửa: +2.370 đ/việc [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot `noi_dia` + `hang_nang` tại 6 depot đang chạy thử, bắt đầu 2026-12-07. Không đưa `quoc_te` (1,88×, thành công 27,3%) và `doi_tac` (0,85×) vào pilot [simulated].

- Có khoá chống hoàn trùng và đối soát sổ cái theo `trace_id` (ca 7, 20 trong bảng lỗi), ngưỡng 0 ca lệch · Trưởng nhóm kỹ thuật trợ lý · kiểm tra 2026-12-04.
- Ký chấp nhận mde 6 điểm, biết rằng power chỉ 0,64 nếu tác động thật là 5 điểm · Giám đốc vận hành · kiểm tra 2026-12-04.
- Bật đủ event có `trace_id`; thay phút `_simulated` bằng phút xem lại, làm lại đo thật · PM trợ lý hoàn phí · kiểm tra 2026-12-14 (hết tuần 1).
- Có kế hoạch giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%, vì xem lại 100% thì chi phí 0,98×–1,03× của 12.000 đ [simulated] · Trưởng nhóm CSKH · kiểm tra 2026-12-21 (cuối bước 0.25).
