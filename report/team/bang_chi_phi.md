# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 · ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 · ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 · ĐẠT |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | simulated |
| Số việc thành công | 978 | `ket_qua` | đo từ dữ liệu |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? Gấp 16,3 lần: 4.472 đ so với 274,7 đ [simulated]. Phần chênh là giờ nhân viên xem lại và làm lại, hoá đơn token + tool không thấy.
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? Làm lại 51,8% (2.264.000 đ), kế đó xem lại 40,7%; token chỉ 5,6% và tool 1,9% [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× |

Tỉ lệ lần chạy `ok` theo lần thử (đo từ trace): noi_dia 91,0% → 75,7% → 38,9% · hang_nang 70,9% → 39,1% → 17,9% · quoc_te 30,0% → 11,4% → 2,2% · doi_tac 51,5% → 18,2% → 14,8%.

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? `quoc_te`: thành công 27,3%, 22.515 đ = 1,88× của 12.000 đ [simulated]. Chạy lại không giúp, tỉ lệ ok giảm 30,0% → 11,4% → 2,2% qua ba lần thử, lỗi lặp lại nên chỉ tốn thêm tiền; `doi_tac` (0,85×) sát ngưỡng nên cũng ngoài phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 3.414 + 1.185 = 4.599 đ [simulated] | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 3.414 + 2.370 = 5.784 đ [simulated] | 0,48× |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Không ở 45.000 yêu cầu/tháng (4.599 đ = 0,38×), vẫn rẻ hơn nhiều so với 12.000 đ. Ở một nửa khối lượng cố định tăng gấp đôi lên 2.370 đ/việc (5.784 đ = 0,48×) nhưng vẫn dưới 12.000 đ [simulated].

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Gốc (A2) | | 4.472 đ [simulated] | |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ [simulated] | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ [simulated] | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ [simulated] | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ [simulated] | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ [simulated] | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ [simulated] | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ [simulated] | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ [simulated] | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ [simulated] | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: 6.543 đ (+46,3%) [simulated], bằng +5,6% + 40,7% vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất (theo mức đổi khi gấp đôi/tăng): 1. số ca làm lại (+51,8%) · 2. tỉ lệ xem lại (+40,7%) · 3. lương nhân viên (+23,1% khi tăng 25%) [simulated]. Giá token chỉ +5,6% nên không phải yếu tố cần theo dõi chính.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

Mọi số trong bảng B3 là simulated (có tiền xem lại, làm lại). Chi phí cả hệ thống = tổng trợ lý + 12.000 đ × số yêu cầu không thành công.

Số liệu B4 (simulated, `noi_dia` + `hang_nang`): 948 yêu cầu có lần chạy ok × 5 phút xem lại; 48 ca làm lại; token + tool 224.513 đ; 900 việc thành công. Làm lại 9 phút/ca: 11.743 đ = 0,98×, hoà vốn khi xem lại ≤ 5,1 phút. Làm lại 15,3 phút/ca (trung bình cột `phut_lam_lai_simulated`): 12.415 đ = 1,03×, hoà vốn ≤ 4,8 phút.

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? Giới hạn 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ), nhưng chi phí mỗi việc thành công thấp nhất ở giới hạn 1 lần (4.111 đ); hai giới hạn không trùng. Giới hạn 1 lần đẩy thêm 85 yêu cầu (319 so với 234) sang nhân viên, mỗi yêu cầu 12.000 đ [simulated].

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: 11.743 đ = 0,98× (làm lại 9 phút/ca); 12.415 đ = 1,03× với 15,3 phút làm lại như dữ liệu, tức đắt hơn nhân viên tự làm [simulated].
- Kết quả này nói gì về thứ pilot cần học được? Tiền xem lại chiếm 89,7% tổng (9.480.000 đ / 10.568.513 đ) nên xem lại 100% gần như không tiết kiệm. Pilot cần đo tỉ lệ xem lại giảm được bao nhiêu mà vẫn an toàn, và mỗi lần xem lại có ≤ 5 phút (hoà vốn 5,1 phút) được không [simulated].
