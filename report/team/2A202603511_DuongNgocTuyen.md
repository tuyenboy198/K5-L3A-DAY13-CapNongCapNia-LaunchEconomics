# Báo cáo cá nhân — DuongNgocTuyen-2A202603511

## 1. Thông tin thành viên

- Họ tên: Dương Ngọc Tuyên
- MSSV: 2A202603511
- Email: vlthuthuatblog@gmail.com
- Vai trong nhóm: Trưởng nhóm · Người giữ hồ sơ · Tích hợp (nhóm 5 người nên tách vai giữ hồ sơ khỏi người gắn nhãn 2); nhận thêm phần còn lại của vai người viết code 1

## 2. Phần việc phụ trách

- Tạo repo nhóm, điền `TEAM.md`, merge nhánh và push bản nộp.
- Điền `report/team/ho_so_launch_v0.md`; viết đề xuất cuối.
- Viết `report/team/group_report.md`; chạy checklist nộp bài trong `SUBMISSION.md`.
- Phần còn lại của người viết code 1: kiểm số D1, chạy lại `lab13.py` từ bản clone sạch.
- Trình bày hồ sơ của nhóm trong buổi duyệt chéo Gate 2a.

## 3. Đóng góp cụ thể

- Viết A1–A4, B1–B4 trong `src/lab13.py`: ba phép thử A1 ĐẠT (1,20 · 1,25 · 1,25); chi phí mỗi việc thành công 4.472 đ, gấp 16,3 lần hoá đơn token + tool chia số yêu cầu [simulated]; điền bảng số A1–A4, B1, B3, B4 trong `bang_chi_phi.md`.
- Kiểm số D1 của người viết code 2 bằng cách tính khác (statsmodels `NormalIndPower` với Cohen's h, không dùng hàm `co_mau`): 1.250 so với 1.251 yêu cầu mỗi nhóm; DE 2,48; tối đa 1.000 và 300; m ≥ 299 (DE 6,96); power 0,64 khi tác động thật 5 điểm với n = 859.
- Điền hồ sơ launch v0 đủ 7 mục; đề xuất **Go có điều kiện** cho pilot `noi_dia` + `hang_nang`, nêu cả con số bất lợi (xem lại 100% còn 0,98×–1,03× [simulated], power 0,64).
- E1 trong `chi_so.md`: tính thử 3 chỉ số trên 1.200 yêu cầu (chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25%), đề xuất 1 chỉ số dùng và 1 chỉ số an toàn, 10 event có `trace_id`, kiểm tra chéo mỗi chỉ số với event.
- Viết báo cáo nhóm; merge các nhánh của thành viên.

## 4. Bằng chứng

- Commit `a621235` (setup), `fb9af99` (A, B); nhánh `tuyenboy198/cp5-hoso`.
- Clone sạch nhánh nộp, `python lab13.py` chạy hết (exit 0); `yaml.safe_load` đọc được `pilot_plan.yaml`; `grep -v '^ *#' pilot_plan.yaml | grep '?'` không in gì.

## 5. Công cụ AI đã dùng

- Claude Code: viết code A1–A4, B1–B4, script kiểm số D1, soạn hồ sơ launch v0, báo cáo nhóm, trang phân công việc.
- Cách tự kiểm tra: chạy `lab13.py` và so mọi số với số đối chiếu trong hướng dẫn chi tiết (lệch ≤ 2%); kiểm "giảm một nửa = nửa mức tăng" ở B1; kiểm D1 bằng một phương pháp thứ hai; đọc lại ca 7 và ca 20 trong đề gốc trước khi dẫn vào điều kiện của đề xuất.

## 6. Tự đánh giá

- Xong: setup repo, A và B, kiểm số D1, hồ sơ launch v0 (mục 1, 2, 3, 6, 7 và đề xuất), báo cáo nhóm.
- Còn chờ: mục 5 của hồ sơ chuyển sang "Xong" khi có bộ nhãn người 1 và tỉ lệ đồng thuận; điền commit chốt vào `TEAM.md` khi push bản cuối.
