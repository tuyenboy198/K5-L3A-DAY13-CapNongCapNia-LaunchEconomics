# Báo cáo cá nhân — PhanSyHung-2A202603420

## 1. Thông tin thành viên

- Họ tên: Phan Sỹ Hùng
- MSSV: 2A202603420
- Email: hungphan120304@gmail.com
- GitHub: @KumaMichio
- Vai trong nhóm: người gắn nhãn 1 · chỉ số và event · hội đồng duyệt chéo (cùng Huệ)

## 2. Phần việc phụ trách

- CP1–CP2: theo dõi điều kiện "Xong khi" của từng checkpoint; đối chiếu số của nhóm với đáp án.
- CP3: gắn nhãn độc lập 20 ca lỗi (cột nhãn người 1 trong `report/team/bang_loi.md`); so nhãn với Huệ.
- CP4–CP5 · E1: tính thử 3 chỉ số, đề xuất 1 chỉ số dùng và 1 chỉ số an toàn, danh sách event có `trace_id`, kiểm tra chéo trong `report/team/chi_so.md`.
- 17:00: cùng Huệ làm hội đồng chấm nhóm n + 1.

## 3. Đóng góp cụ thể

- Đối chiếu CP1–CP2: chạy lại `src/lab13.py`, ba phép thử ĐẠT; A2 4.472 đ, A3 (2.696 · 8.221 · 22.515 · 10.215 đ), B1 9 dòng, B2 6.543 đ, B3 rẻ nhất ở 2 lần (6.901.220 đ), B4 11.743 đ = 0,98× đều khớp đáp án; B4 với 15,3 phút ra 12.415 đ so với 12.414 đ, lệch 0,01% [simulated].
- E1: tính độc lập trên 1.200 yêu cầu, khớp bản trong `chi_so.md`: chỉ số chính trong đợt chạy thử 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177: 41 sửa + 7 bỏ), lỗi lọt đến khách 4,25% (51/1.200), phạm vi `noi_dia` + `hang_nang` 3,97% (39/982).
- Phát hiện thêm: cả 51 ca mở lại đều có `ket_qua = lam_lai`; chỉ số chính theo loại là `noi_dia` 95,27%, `hang_nang` 76,58%, `doi_tac` 58,82%, `quoc_te` 32,00%. Đây là chênh lệch trong đợt chạy thử, chưa phải tác động của trợ lý.
- CP3: tự gắn nhãn độc lập 20 ca (commit `028c8ed` trước khi so); đồng thuận với Huệ 19/20 = 95%. Ca 17 không trùng (tôi: Hệ thống, Huệ: Ngầm); quy tắc: lỗi hệ thống chưa ai nhận ra cho tới khi kiểm tra thì gắn Ngầm.
- Hội đồng: ... (điền câu hỏi có số đã đặt cho nhóm n + 1)

## 4. Bằng chứng

- `report/team/chi_so.md` (E1), `report/team/bang_loi.md` (cột nhãn người 1).
- Commit: `c0f6f24` (đối chiếu CP1–CP2, E1), `028c8ed` (bộ nhãn người 1, trước khi so), `3188925` (so nhãn, quy tắc ca 17).

## 5. Công cụ AI đã dùng

Dùng Claude Code để tính lại ba chỉ số bằng pandas, chạy lại `lab13.py` và đối chiếu với số trong hướng dẫn chi tiết (mục A, B, E1). Tôi tự kiểm tra bằng cách so từng con số với đáp án, lệch không quá 2%. Nhãn 20 ca ở CP3 do tôi tự gắn; AI chỉ dùng để chép nhãn vào bảng và đếm số ca trùng.

## 6. Tự đánh giá

...
