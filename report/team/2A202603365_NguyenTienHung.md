# Báo cáo cá nhân — NguyenTienHung-2A202603365

## 1. Thông tin thành viên

- Họ tên: Nguyễn Tiến Hưng
- MSSV: 2A202603365
- Email: nguyentienhung04042004@gmail.com
- GitHub: tienhungw
- Vai trong nhóm: người viết code 1 (CP1–CP2) · kiểm số D1

## 2. Phần việc phụ trách

- `src/lab13.py` phần CP1–CP2: A1 (ba hàm và ba phép thử), A2 (`mo_hinh`), A3, A4, B1–B4.
- Các bảng số và câu trả lời trong `report/team/bang_chi_phi.md` (tiêu chí C1, C2).
- Kiểm số D1 sau giải lao; chạy lại `lab13.py` trên máy mình trước khi nộp.

## 3. Đóng góp cụ thể

- Viết ba hàm A1; ba phép thử đáp án biết trước ĐẠT (1,20 · 1,25 · 1,25).
- Viết `mo_hinh` có sẵn tham số giá, hệ số và `max_lan_chay`: tử số cộng mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm `ket_qua == 'thanh_cong'`. Chi phí mỗi việc thành công 4.472 đ, 978 việc thành công [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ).
- A3 bốn loại yêu cầu (`quoc_te` 22.515 đ = 1,88× nên không đáng xử lý); A4 cộng chi phí cố định 40 triệu đ/tháng: 4.599 đ = 0,38× ở 45.000 yêu cầu/tháng, 5.784 đ = 0,48× ở một nửa khối lượng [simulated].
- B1 chín kịch bản; B2 cặp token + xem lại +46,3% bằng tổng hai tác động riêng; B3 giới hạn 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ) còn 1 lần thấp nhất theo chi phí mỗi việc (4.111 đ); B4 xem lại 100%: 0,98× (làm lại 9 phút), 1,03× (15,3 phút), hoà vốn xem lại ≤ 5,1 phút [simulated].
- Điền đủ các câu trả lời A2–A4, B2–B4 (mỗi câu ≤ 3 dòng, có số, có nhãn simulated).
- Kiểm số D1 sau khi có code CP4 của Dương Minh Tân: `lab13.py` in đủ năm câu, khớp đáp án: a) 1.251 mỗi nhóm · b) DE 2,48 → 3.103 mỗi nhóm = 42 người/nhóm (84 > 40) · c) tối đa 1.000 < 1.251, không đạt · d) tối đa 300 · e) mức chênh 6 điểm (859/nhóm), 20 người/nhóm: m ≥ 299 (DE 6,96).

## 4. Bằng chứng

- Nhánh `tienhungw/cp1` (commit `fb9af99` CP1–CP2) và `tienhungw/report` (bảng trả lời, báo cáo cá nhân, TEAM.md).
- `src/lab13.py`; `report/team/bang_chi_phi.md`.
- Chạy lại `python lab13.py` (Windows, Python 3.11, đặt `PYTHONIOENCODING=utf-8` để in tiếng Việt): ba phép thử ĐẠT; A2 4.472 đ/việc; B1 đủ 9 dòng; "giảm một nửa" bằng nửa mức tăng (2,8 / 5,6 · 20,3 / 40,7 · 25,9 / 51,8).

## 5. Công cụ AI đã dùng

- Claude Code: gợi ý khung code `mo_hinh` và các vòng B1–B4, soạn câu chữ cho các câu trả lời trong `bang_chi_phi.md`.
- Cách tự kiểm tra: chạy `lab13.py` và so với đáp án tham chiếu trong hướng dẫn (lệch ≤ 2%); kiểm "giảm một nửa = nửa mức tăng"; cộng tay tỉ trọng 5,6% + 1,9% + 40,7% + 51,8% = 100%; tự giải thích được vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công.

## 6. Tự đánh giá

- Xong: CP1–CP2 trong code, bảng A1–B4 và toàn bộ câu trả lời, báo cáo cá nhân, mục đóng góp trong `TEAM.md`.
- Xong thêm: kiểm số D1 năm câu khớp đáp án; chạy lại `lab13.py` lần cuối trên `main` sau khi có phần CP4, chạy hết (exit 0).
