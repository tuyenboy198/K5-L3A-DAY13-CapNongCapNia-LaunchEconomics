# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: CapNongCapNia
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để hội đồng Gate 2a duyệt kế hoạch pilot. Nhóm trả lời bốn câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào để ra được quyết định. Mọi số tính bằng `src/lab13.py` trên hai file CSV giả lập; số từ cột `_simulated` ghi nhãn simulated. Nhóm 5 người nên tách thêm vai trưởng nhóm kiêm giữ hồ sơ; người viết code đổi sau giải lao.

## 3. Giải pháp

- **A · Chi phí** ([bang_chi_phi.md](bang_chi_phi.md)): `mo_hinh()` cộng token + tool của mọi lần chạy kể cả lỗi, cộng phút xem lại và làm lại, chia cho số việc thành công; gọi lại theo từng loại yêu cầu và cộng chi phí cố định cho phạm vi pilot.
- **B · Độ nhạy** ([bang_chi_phi.md](bang_chi_phi.md)): 9 kịch bản đổi từng yếu tố, một cặp, giới hạn 1/2/3 lần chạy tính cả phần nhân viên làm thay, kịch bản xem lại 100%.
- **C · Bảng lỗi** ([bang_loi.md](bang_loi.md)): hai người gắn nhãn độc lập 20 ca theo năm loại Google PAIR, commit trước khi so; bảng khắc phục 5 ca, mỗi dòng có event, ngưỡng và một vai trò.
- **D · Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): tính đủ 5 câu cỡ mẫu trước khi chọn cách chia; chọn chia theo nhân viên 20 + 20; 3 luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ. D1 được kiểm bằng một phương pháp thứ hai (Cohen's h).
- **E · Chỉ số, rủi ro, hồ sơ** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): ba chỉ số tính thử, danh sách event có `trace_id`, ba dòng rủi ro kinh tế lấy số từ bảng độ nhạy.

## 4. Kết quả

- Chi phí mỗi việc thành công **4.472 đ** (978 việc), gấp 16,3 lần hoá đơn token + tool chia số yêu cầu [simulated]. Cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated].
- Theo loại: `noi_dia` 0,22× · `hang_nang` 0,69× · `doi_tac` 0,85× · `quoc_te` 1,88× [simulated]; chạy lại không cứu `quoc_te` (ok 30,0% → 11,4% → 2,2%).
- Ba yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương (+23,1%) [simulated]. Giới hạn 2 lần chạy rẻ nhất cho cả hệ thống (6.901.220 đ).
- Con số bất lợi: xem lại 100% còn 0,98×–1,03× của 12.000 đ [simulated]; mde 6 điểm nên power chỉ 0,64 nếu tác động thật là 5 điểm.
- Chỉ số trong đợt chạy thử: chính 82,83% · bỏ qua gợi ý 27,12% · mở lại 7 ngày 4,25%.
- **Đề xuất: Go có điều kiện** cho pilot `noi_dia` + `hang_nang`, 4 điều kiện có vai trò và ngày kiểm tra (xem `ho_so_launch_v0.md`).
- Kết quả duyệt chéo nhóm nhận được: hội đồng nhóm VOI chấm **25/30** (khớp bằng chứng 10 · số giả lập và phạm vi 10 · pilot 5), quyết định **Go có điều kiện**. Tiêu chí pilot bị trừ vì hồ sơ một trang chỉ ghi "3 luật dừng", hội đồng chưa đối chiếu ngưỡng, thời hạn, người có quyền dừng trong `pilot_plan.yaml` (file đã có đủ). Câu hỏi: cần bao nhiêu yêu cầu mỗi tuần để kịp ngày quyết định 2027-01-12 nếu bước 50% bắt đầu 2026-12-21. Nhóm trả lời: 3.000 yêu cầu/nhóm/tuần (~150/nhân viên, khớp ước tính ~31/người/ngày trong `pilot_plan.yaml`), sau 2 tuần có ~6.000/nhóm, vượt mức 5.980 cần thiết; nếu lưu lượng thấp thì kéo dài thu mẫu cho cả hai nhóm và lùi ngày quyết định. Bài học: chép ngưỡng luật dừng vào hồ sơ một trang.

## 5. Khó khăn và cách xử lý

- Trên Windows, pandas 3.1.1 cài từ `requirements.txt` bị chặn khi import: `ImportError: DLL load failed while importing fields: An Application Control policy has blocked this file.` Xử lý: `python -m pip install pandas==2.2.3` trong `.venv`; sau đó `python lab13.py` chạy hết.
- In tiếng Việt ra console Windows cần đặt `PYTHONIOENCODING=utf-8`.
- Với 40 nhân viên, không cách chia theo cụm nào đủ mẫu cho mức chênh 5 điểm; nhóm chấp nhận mde 6 điểm và ghi rõ power 0,64 trong hồ sơ.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Phút xem lại và làm lại là số giả lập; tuần 1 của pilot phải thay bằng phút đo thật từ event `staff_review_decision`, `staff_rework_completed`.
- Đợt chạy thử không có nhóm đối chứng, nên chỉ số 82,83% chưa nói được tác động của trợ lý.
- Kế hoạch giảm xem lại theo bậc mới ở mức ngưỡng (sửa + bỏ < 15%), chưa thử trên dữ liệu thật.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure"
- Tài liệu statsmodels, `stats.power.NormalIndPower`, `stats.proportion.proportion_effectsize`
- Đề bài và hướng dẫn chi tiết Lab 13 trong `docs/`
