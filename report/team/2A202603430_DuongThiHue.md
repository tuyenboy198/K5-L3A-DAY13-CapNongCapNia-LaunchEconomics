# Báo cáo cá nhân — DuongThiHue-2A202603430

## 1. Thông tin thành viên

- Họ tên: Dương Thị Huệ
- MSSV: 2A202603430
- Email: duonghue2004yp@gmail.com
- GitHub: dhuee10
- Vai trong nhóm: người gắn nhãn 2 · bảng lỗi · rủi ro kinh tế (E2) · chủ trì phiếu chấm hội đồng

## 2. Phần việc phụ trách

- `report/team/bang_loi.md` (nhiệm vụ C, tiêu chí C3): bộ nhãn độc lập người 2, chủ trì gộp nhãn với người gắn nhãn 1, tỉ lệ đồng thuận, quy tắc cho ca không trùng, bảng khắc phục 5 ca.
- `report/team/chi_so.md` phần E2 (hỗ trợ C5): các dòng rủi ro kinh tế lấy số từ bảng độ nhạy.
- `report/team/phieu_cham.md`: chủ trì phiếu chấm nhóm n + 1 khi làm hội đồng Gate 2a.

## 3. Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca theo nguyên nhân gốc, commit trước khi so nhãn. Phân bố: Do người dùng 4 · Hệ thống 5 · Ngữ cảnh 4 · Giới hạn hệ thống 4 · Ngầm 3.
- Viết bảng khắc phục 5 ca, mỗi loại một ca (ca 1, 7, 18, 13, 17). Mỗi dòng có event hoặc kiểm tra mẫu, ngưỡng, tần suất và một vai trò phụ trách.
- Viết 3 dòng rủi ro E2: làm lại gấp đôi +51,8% (6.787 đ) [simulated]; xem lại 100% còn 0,98× (1,03× với 15,3 phút làm lại) [simulated]; chi phí cố định +1.185 đ/việc, +2.370 đ/việc ở nửa khối lượng [simulated].
- Gộp nhãn với Phan Sỹ Hùng: đồng thuận 19/20 = 95%; ca không trùng duy nhất là ca 17 (Hệ thống / Ngầm), thống nhất Ngầm theo quy tắc "lỗi chưa ai nhận ra cho tới khi kiểm tra mẫu". Bảng khắc phục giữ nguyên vì 5 ca đã chọn đều khớp nhãn thống nhất; cập nhật mục 5 của hồ sơ launch v0.
- Còn chờ: chấm `phieu_cham.md` khi nhận hồ sơ nhóm n + 1 tại buổi Gate 2a.

## 4. Bằng chứng

- Nhánh `dhuee10/cp3-cp5`.
- Commit bộ nhãn độc lập người 2 trong `report/team/bang_loi.md` (trước khi so nhãn).
- Gộp nhãn: bộ nhãn người 1 trên nhánh `hung/e1-chi-so-event` (19/20), gộp vào nhánh `dhuee10/cp3-cp5`.
- Commit bảng khắc phục và E2 trong `report/team/bang_loi.md`, `report/team/chi_so.md`.
- Số E2 kiểm độc lập trên `src/logix_runs.csv`, `src/logix_requests.csv`: gốc 4.472 đ/việc; phạm vi noi_dia + hang_nang 900 việc thành công, 3.414 đ/việc; B4 948 yêu cầu được xem lại × 5 phút, 48 ca làm lại [simulated].

## 5. Công cụ AI đã dùng

- Claude Code: đọc đề và hướng dẫn, soạn nháp bảng khắc phục và câu chữ cho các dòng rủi ro E2, viết script kiểm số bằng thư viện chuẩn Python.
- Cách tự kiểm tra: chạy script trên hai file CSV và so với bảng B1, B4, A4 (lệch ≤ 2%); kiểm "giảm một nửa = nửa mức tăng"; lệnh grep tìm từ cấm (quy tắc 5 trong `README.md`) trên `report/team` không in gì. Bộ nhãn 20 ca tôi tự rà lại từng ca theo câu hỏi nhận diện của PAIR trước khi commit; không đọc bảng nhãn tham khảo trong hướng dẫn chi tiết.

## 6. Tự đánh giá

- Xong: bộ nhãn người 2, bảng khắc phục 5 ca đủ 5 loại, E2 3 dòng có nhãn simulated, dấu hiệu theo dõi và người phụ trách.
- Xong thêm: tỉ lệ đồng thuận 19/20, quy tắc ca 17, cột nhãn thống nhất, mục 5 hồ sơ.
- Xong thêm: phiếu chấm hội đồng (cùng Phan Sỹ Hùng) cho nhóm VOI, 30/30, quyết định Go có điều kiện; góp ý tách luật hoàn trùng thành dừng ngay (`report/team/phieu_cham.md`).
