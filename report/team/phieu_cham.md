# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): CapNongCapNia 
- Nhóm được chấm: VOI

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | "Go có điều kiện" khớp số: phạm vi 4.131 đ/yêu cầu (đã cộng 82 ca nhân viên làm thay) so với 12.000 đ. Nêu cả hai con số bất lợi: power chỉ 0,64 nếu tác động thật +5 điểm, và xem lại 100% lên 11.743–12.415 đ/việc ≈ 12.000 đ [simulated]. Có cách xử lý: Giám đốc vận hành ký đánh đổi MDE 6 điểm; giảm xem lại có kiểm tra an toàn. Mục 5 còn "Chưa" (đồng thuận chưa tính) nhưng đã đưa thành điều kiện, không giấu. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mọi số chi phí ở mục 1, 2, 3, 7 đều ghi simulated; mục 4 tính từ cột không giả lập nên không cần nhãn. Thu hẹp về noi_dia + hang_nang (982 yêu cầu) có lý do bằng số: quoc_te chỉ thành công 27,3%, 22.515 đ/việc [simulated]. Góp ý: doi_tac chỉ ghi "điều khoản riêng", nên thêm số (0,85× của 12.000 đ). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Tách được tác động: đối chứng đồng thời, chia theo nhân viên 20 cụm/nhánh, DE 6,96, n hiệu dụng 859/nhánh cho MDE 6 điểm (ghi rõ đánh đổi, power 0,64 nếu +5 điểm), ngày quyết định 05/01/2027. Ba luật dừng trong `pilot_plan.yaml` đủ ngưỡng, thời hạn, người có quyền dừng (an toàn: +2 điểm so với đối chứng hoặc > 6%, 3 ngày, Giám đốc vận hành tắt trong 30 phút; chi phí > 8.000 đ, 2 tuần; sử dụng > 40%, 1 tuần). Góp ý: hồ sơ một trang chưa chép ngưỡng luật dừng; seed và ngày bắt đầu chưa chốt; ca hoàn trùng nên dừng ngay, không chờ 3 ngày. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Chi phí trong phạm vi 4.131 đ/yêu cầu, chỉ khoảng 0,34× của 12.000 đ [simulated], và thiết kế pilot tách được tác động (20 cụm/nhánh, đối chứng đồng thời). Trước khi bật pilot phải: (1) chép ngưỡng ba luật dừng vào hồ sơ một trang và tách luật hoàn trùng thành dừng ngay; (2) chốt seed và ngày bắt đầu; (3) tính đồng thuận nhãn ≥ 16/20; (4) có kế hoạch giảm tỉ lệ xem lại, vì xem lại 100% đưa chi phí lên 11.743–12.415 đ/việc, ngang mức nhân viên tự làm [simulated].

**Một câu hỏi cho đội trình:** Tỉ lệ mở lại 7 ngày hiện tại đã là 4,25% (51/1.200). Luật dừng an toàn của nhóm đặt ngưỡng bao nhiêu, đo trong bao lâu, và ai bấm dừng? Nếu đặt ngưỡng tuyệt đối dưới 4,25% thì pilot có bị dừng ngay tuần đầu không?

**Câu trả lời của đội trình (ghi lại tại buổi):** Ba luật dừng ghi trong `pilot_plan.yaml` của VOI (dòng 49). Luật an toàn không dùng ngưỡng tuyệt đối dưới 4,25% mà so với đối chứng:

| Luật | Ngưỡng | Thời hạn | Người xử lý |
| --- | --- | --- | --- |
| An toàn | Mở lại 7 ngày cao hơn đối chứng ≥ 2 điểm, hoặc vượt 6%, hoặc ≥ 1 ca hoàn trùng | 3 ngày liên tiếp | Giám đốc vận hành tắt trợ lý trong 30 phút |
| Chi phí | Chi phí mỗi việc thành công > 8.000 đ [simulated] | 2 tuần liên tiếp | PM thu hẹp về noi_dia, giới hạn tối đa 2 lần chạy |
| Sử dụng | Tỉ lệ gợi ý bị sửa hoặc bỏ > 40% | 1 tuần | Trưởng nhóm CSKH phỏng vấn 5 nhân viên trong 3 ngày |

Chỉ số chính thu mẫu từ bước rollout 50%; một yêu cầu đạt nếu đóng trong 24 giờ và không mở lại trong 7 ngày sau khi đóng; ngày quyết định 05/01/2027.

**Nhận xét của hội đồng:** theo câu chữ hiện tại, cả ba điều kiện an toàn đều nằm dưới "3 ngày liên tiếp", nên một ca hoàn trùng phải lặp 3 ngày mới dừng. Đề nghị VOI tách riêng: chỉ cần 1 ca hoàn trùng là dừng ngay.
