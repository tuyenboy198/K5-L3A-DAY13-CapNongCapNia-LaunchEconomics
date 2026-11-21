# Báo cáo cá nhân — DuongMinhTan-2A202603464

## 1. Thông tin thành viên

- Họ tên: Dương Minh Tân
- MSSV: 2A202603464
- Email: duongminhtan325@gmail.com
- Vai trong nhóm: Người kiểm số (CP1–CP2) · Người viết code 2 sau giải lao (CP4)

## 2. Phần việc phụ trách

- CP1–CP2: tính tay độc lập để đối chiếu với `mo_hinh` trong `src/lab13.py`; điền bảng và câu trả lời A2, A3, A4, B1–B4 trong `report/team/bang_chi_phi.md`.
- CP3: cùng Hưng hoàn thiện CP2 trong lúc hai người gắn nhãn làm việc độc lập.
- CP4: viết `co_mau()` và `nhiem_vu_d()` trong `src/lab13.py`; điền toàn bộ `report/team/pilot_plan.yaml`.

## 3. Đóng góp cụ thể

- Kiểm số: tính hoá đơn token + tool trên cả 1.624 lần chạy = 329.585 đ → 274,7 đ/yêu cầu; chi phí mỗi việc thành công 4.373.585 / 978 = 4.472 đ [simulated], gấp 16,3×.
- Chỉ ra khi so với 12.000 đ phải cộng 222 ca nhân viên làm thay → 5.865 đ/yêu cầu = 0,49× (không phải 0,37×).
- Kiểm B1: mỗi kịch bản "giảm một nửa" đúng bằng nửa "gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9).
- D1: tính đủ 5 câu (1.251 · 3.103 = 42 người/nhóm · tối đa 1.000 · tối đa 300 · m ≥ 299) trước khi chọn chia theo nhân viên 20 + 20, chấp nhận mde 6 điểm (power còn ~0,64 nếu tác động thật 5 điểm).
- D3: tính tỉ lệ mở lại 7 ngày hiện tại 4,25% (3,97% trong phạm vi) rồi mới đặt luật an toàn so với đối chứng (+2 điểm) kèm trần 6%; viết 3 luật dừng đủ 4 vế.

## 4. Bằng chứng

- `report/team/bang_chi_phi.md`: dòng kiểm số tính tay, bảng A2–A4, B1–B4.
- `src/lab13.py`: hàm `co_mau()` (có assert 1.251 và 859) và `nhiem_vu_d()`.
- `report/team/pilot_plan.yaml`: `yaml.safe_load` đọc được; `grep -v '^ *#' ... | grep -n '?'` không in gì.
- Commit: `332e0c1` trên nhánh `mihtan05/cp4`

## 5. Công cụ AI đã dùng

- Claude Code: lập plan theo checklist vai, viết script kiểm số độc lập (tính trực tiếp từ CSV, không gọi `mo_hinh`), viết `co_mau`, nháp `pilot_plan.yaml` và các câu trả lời.
- Tự kiểm tra: so mọi số với số đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch < 1%); chạy hai lệnh tự kiểm tra của CP4; tự tính lại câu e bằng tay (2,82m ≥ 841,82 → m ≥ 299).

## 6. Tự đánh giá

- Làm tốt: tính số độc lập và khớp 100% với code của Hưng (A2–B4); tính đủ 5 câu D1 trước khi chọn cách chia, và ghi rõ con số bất lợi (power ~0,64 nếu tác động thật chỉ 5 điểm).
- Chưa tốt: dựa nhiều vào AI để viết nháp; chưa chạy thử `lab13.py` trên máy khác trong nhóm.
- Bài học: cách chia theo cụm quyết định cỡ mẫu nhiều hơn tổng số yêu cầu; phải xem tỉ lệ hiện tại (4,25%) trước khi đặt ngưỡng an toàn.
