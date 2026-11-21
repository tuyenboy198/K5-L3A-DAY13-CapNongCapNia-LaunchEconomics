# Team

## Thông tin nhóm

- Tên nhóm: CapNongCapNia
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-CapNongCapNia-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/tuyenboy198/K5-L3A-DAY13-CapNongCapNia-LaunchEconomics · `main` · commit chốt: `9ec0982` (toàn bộ code và hồ sơ; commit sau chỉ ghi mã này vào `TEAM.md`)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Dương Ngọc Tuyên | 2A202603511 | vlthuthuatblog@gmail.com | tuyenboy198 | Trưởng nhóm · Người giữ hồ sơ · Tích hợp |
|   2 | Nguyễn Tiến Hưng | 2A202603365 | nguyentienhung04042004@gmail.com | tienhungw | Người viết code 1 (CP1–CP2) · Kiểm số D |
|   3 | Dương Minh Tân | 2A202603464 | duongminhtan325@gmail.com | mihtan05 | Người kiểm số (CP1–CP2) · Người viết code 2 (CP4) |
|   4 | Phan Sỹ Hùng | 2A202603420 | hungphan120304@gmail.com | KumaMichio | Người gắn nhãn 1 · Chỉ số và event |
|   5 | Dương Thị Huệ | 2A202603430 | duonghue2004yp@gmail.com | dhuee10 | Người gắn nhãn 2 · Bảng lỗi · Rủi ro kinh tế · Phiếu chấm |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

Nhóm có 5 người nên tách thêm vai **trưởng nhóm · giữ hồ sơ · tích hợp**; vai giữ hồ sơ chuyển từ người gắn nhãn 2 sang trưởng nhóm. Người viết code đổi từ Hưng (trước giải lao) sang Tân (sau giải lao).

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

## DuongNgocTuyen-2A202603511

### Phần việc phụ trách

- Tạo repo nhóm, điền `TEAM.md`, tích hợp và push bản nộp.
- Giữ hồ sơ: `report/team/ho_so_launch_v0.md` (7 mục và đề xuất cuối).
- `report/team/group_report.md`; trình bày khi nhóm bị duyệt chéo Gate 2a.
- Nhận thêm phần còn lại của vai người viết code 1: kiểm số D1, chạy lại `lab13.py` từ bản clone sạch.

### Đóng góp cụ thể

- Setup repo, `TEAM.md`, khung hồ sơ (commit `a621235`).
- Viết A1–A4, B1–B4 trong `src/lab13.py` và các bảng số A1–A4, B1, B3, B4 trong `bang_chi_phi.md` (commit `fb9af99`): ba phép thử ĐẠT; 4.472 đ/việc thành công [simulated].
- Kiểm số D1 bằng cách độc lập (statsmodels `NormalIndPower`, Cohen's h): 1.250 so với 1.251 · DE 2,48 · 1.000 · 300 · m ≥ 299; power 0,64 ở mức 5 điểm với n = 859. Lệch ≤ 0,3%.
- Clone sạch nhánh nộp, chạy `python lab13.py` hết, `pilot_plan.yaml` qua `yaml.safe_load`, không còn `?`.
- E1 trong `chi_so.md`: tính thử 3 chỉ số (82,83% · 27,12% · 4,25%), 2 chỉ số tự đề xuất, 10 event có `trace_id`, kiểm tra chéo chỉ số ↔ event.
- `ho_so_launch_v0.md` đủ 7 mục và đề xuất Go có điều kiện (4 điều kiện, mỗi điều kiện có vai trò và ngày kiểm tra); `group_report.md`; merge các nhánh.

### Bằng chứng

- Commit `a621235`, `fb9af99`; nhánh `tuyenboy198/cp5-hoso`; `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `report/team/2A202603511_DuongNgocTuyen.md`.

## NguyenTienHung-2A202603365

### Phần việc phụ trách

- `src/lab13.py` phần CP1–CP2 (A1–A4, B1–B4); các bảng số trong `report/team/bang_chi_phi.md`.
- Kiểm số D1 sau giải lao; chạy lại `lab13.py` trên máy mình trước khi nộp.

### Đóng góp cụ thể

- A1–A4, B1–B4 trong `lab13.py`: ba phép thử ĐẠT; chi phí mỗi việc thành công 4.472 đ, 978 việc thành công, gấp 16,3 lần hoá đơn token + tool [simulated].
- Bảng A2, A3, A4, B1, B3, B4 và câu trả lời trong `bang_chi_phi.md`: yếu tố nhạy nhất là số ca làm lại (+51,8%); giới hạn 2 lần rẻ nhất cho cả hệ thống; xem lại 100% còn 0,98×–1,03× [simulated].
- Chờ: kiểm số D1 (cần code CP4 của Tân).

### Bằng chứng

- Nhánh `tienhungw/cp1`, `tienhungw/report`; `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/2A202603365_NguyenTienHung.md`.

## DuongMinhTan-2A202603464

### Phần việc phụ trách

- Kiểm số CP1–CP2 (tính tay, câu trả lời A2–A4, B2–B4 trong `report/team/bang_chi_phi.md`).
- `src/lab13.py` phần CP4 (D1); `report/team/pilot_plan.yaml`.

### Đóng góp cụ thể

-

### Bằng chứng

-

## PhanSyHung-2A202603420

### Phần việc phụ trách

- Gắn nhãn độc lập 20 ca (người 1) trong `report/team/bang_loi.md`.
- `report/team/chi_so.md` phần E1 và danh sách event; hội đồng chấm nhóm n + 1.

### Đóng góp cụ thể

- Đối chiếu CP1–CP2 với đáp án: A2 4.472 đ, A3, B1–B4 đều khớp (lệch tối đa 0,01%) [simulated].
- Tính độc lập E1 để kiểm bản trong `chi_so.md`: 82,83% · 27,12% · 4,25% (phạm vi 3,97%), khớp; cả 51 ca mở lại đều là `lam_lai`.
- Bộ nhãn độc lập người 1 cho 20 ca (commit `028c8ed` trước khi so); đồng thuận 19/20 = 95%, quy tắc cho ca 17.
- Chờ: câu hỏi hội đồng cho nhóm n + 1.

### Bằng chứng

- Nhánh `hung/e1-chi-so-event`; `report/team/2A202603420_PhanSyHung.md`.

## DuongThiHue-2A202603430

### Phần việc phụ trách

- Gắn nhãn độc lập 20 ca (người 2); gộp nhãn, tỉ lệ đồng thuận, bảng khắc phục trong `report/team/bang_loi.md`.
- `report/team/chi_so.md` phần E2 (rủi ro kinh tế); chủ trì `report/team/phieu_cham.md`.

### Đóng góp cụ thể

- Bộ nhãn độc lập người 2 cho 20 ca (commit trước khi so nhãn); bảng khắc phục 5 ca đủ 5 loại.
- E2: 3 dòng rủi ro kinh tế (làm lại × 2, xem lại 100%, chi phí cố định ở nửa khối lượng), có nhãn simulated.
- Gộp nhãn với người gắn nhãn 1: đồng thuận 19/20 = 95%; cập nhật mục 5 hồ sơ.
- Chờ: phiếu chấm nhóm n + 1.

### Bằng chứng

- Nhánh `dhuee10/cp3-cp5`; `report/team/bang_loi.md`, `report/team/chi_so.md` (E2), `report/team/2A202603430_DuongThiHue.md`.
