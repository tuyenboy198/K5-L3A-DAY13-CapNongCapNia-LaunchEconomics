"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CO_DINH_THANG = 40_000_000   # chi phí cố định của trợ lý, đồng / tháng
YC_THANG = 45_000            # yêu cầu hoàn phí mỗi tháng (1.500 / ngày)
PHAM_VI = ['noi_dia', 'hang_nang']


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        # Bỏ lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn coi là chuyển nhân viên, không còn phút xem lại/làm lại.
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


def tieu_de(s):
    print(f'\n===== {s} =====')


# ---------- Nhiệm vụ D1 · Cỡ mẫu ----------
def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm để so hai tỉ lệ p1, p2 (kiểm định hai phía)."""
    from statistics import NormalDist
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def nhiem_vu_d(reqs, icc=0.02):
    n5, n6 = co_mau(0.70, 0.75), co_mau(0.70, 0.76)
    assert n5 == 1251 and n6 == 859, (n5, n6)
    de75 = 1 + 74 * icc
    # e: 20m / (1 + (m - 1) * icc) >= n6  →  m >= n6 * (1 - icc) / (20 - n6 * icc)
    m_e = math.ceil(n6 * (1 - icc) / (20 - n6 * icc))
    print('\nD1 · Cỡ mẫu (baseline 0,70; ICC 0,02)')
    print(f'  a) Chia theo yêu cầu: {n5:,} mỗi nhóm')
    print(f'  b) Theo nhân viên, m=75: DE={de75:.2f} → {math.ceil(n5 * de75):,} mỗi nhóm '
          f'= {math.ceil(n5 * de75 / 75)} người/nhóm (cần {2 * math.ceil(n5 * de75 / 75)} > 40)')
    print(f'  c) 20 nhân viên mỗi nhóm: tối đa {20 / icc:,.0f} < {n5:,} → không đạt')
    print(f'  d) 6 depot mỗi nhóm: tối đa {6 / icc:,.0f}')
    print(f'  e) Mức chênh 6 điểm ({n6}/nhóm), 20 người/nhóm: m ≥ {m_e} (DE {1 + (m_e - 1) * icc:.2f})')
    print(f'D3 · mo_lai_trong_7_ngay hiện tại: {reqs.mo_lai_trong_7_ngay.mean():.2%}; '
          f'noi_dia+hang_nang: {reqs[reqs.loai.isin(["noi_dia", "hang_nang"])].mo_lai_trong_7_ngay.mean():.2%}')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    print(f'  E[số lần chạy] p=0,8 k=2: {so_lan_chay_ky_vong(0.8, 2):.2f} · k=∞: {so_lan_chay_ky_vong(0.8):.2f}'
          f' · hệ số chi phí k=3: {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')

    # ---------- A2 ----------
    tieu_de('A2 · Mô hình chi phí từ trace (xem_lai, lam_lai, tong, cps: simulated)')
    goc = mo_hinh(runs, reqs)
    for ten, gia_tri in goc.items():
        print(f'{ten:16s} {gia_tri:>14,.1f}')
    print(f'cps / hoá đơn mỗi yêu cầu: {goc["cps"] / goc["hoa_don_moi_yc"]:.1f} lần')
    for k in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f'  tỉ trọng {k:8s} {goc[k] / goc["tong"] * 100:5.1f}%')
    khong_tc = len(reqs) - goc['thanh_cong']
    he_thong = (goc['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'Chi phí cả hệ thống mỗi yêu cầu (cộng {khong_tc} ca nhân viên làm thay): '
          f'{he_thong:,.0f} đ = {he_thong / BASELINE:.2f}× [simulated]')

    # ---------- A3 ----------
    tieu_de('A3 · Tách theo loại yêu cầu (cps: simulated)')
    print(f'{"loai":10s} {"so_yc":>6s} {"ti_le_tc":>9s} {"chay/yc":>8s} {"cps":>9s} {"so_12k":>7s}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        m = mo_hinh(runs, r)
        so_chay = runs['request_id'].isin(r['request_id']).sum()
        print(f'{loai:10s} {len(r):6d} {m["thanh_cong"] / len(r):9.1%} {so_chay / len(r):8.2f} '
              f'{m["cps"]:9,.0f} {m["cps"] / BASELINE:6.2f}×')
    ok_theo_lan = (runs.merge(reqs[['request_id', 'loai']], on='request_id')
                   .assign(ok=lambda d: d['status'] == 'ok')
                   .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean'))
    print('\nTỉ lệ ok theo lần thử:')
    print((ok_theo_lan * 100).round(1).to_string())

    # ---------- A4 ----------
    tieu_de('A4 · Chi phí cố định, phạm vi noi_dia + hang_nang (simulated)')
    pv = reqs[reqs['loai'].isin(PHAM_VI)]
    m_pv = mo_hinh(runs, pv)
    print(f'Phạm vi: {len(pv)} yêu cầu, {m_pv["thanh_cong"]} thành công, cps {m_pv["cps"]:,.0f} đ')
    for nhan, kl in [('45.000 yêu cầu/tháng', YC_THANG), ('Một nửa khối lượng', YC_THANG / 2)]:
        tc_thang = kl * m_pv['thanh_cong'] / len(reqs)
        co_dinh = CO_DINH_THANG / tc_thang
        tong_viec = m_pv['cps'] + co_dinh
        print(f'{nhan:22s} thành công/tháng {tc_thang:9,.0f} · cố định/việc {co_dinh:7,.0f} đ'
              f' · cps + cố định {tong_viec:7,.0f} đ = {tong_viec / BASELINE:.2f}×')

    # ---------- B1 ----------
    tieu_de('B1 · Đổi từng yếu tố (simulated)')
    kich_ban = {
        'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':          dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':     dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':          dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':     dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':           dict(luong_phut=2500),
        'Tối đa 2 lần chạy':        dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':           dict(max_lan_chay=1),
    }
    print(f'{"Gốc (A2)":25s} {goc["cps"]:8,.0f}')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:25s} {cps:8,.0f} {(cps / goc["cps"] - 1) * 100:+6.1f}%')

    # ---------- B2 ----------
    tieu_de('B2 · Đổi một cặp (simulated)')
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'Token gấp đôi + xem lại gấp đôi: {cap:,.0f} đ ({(cap / goc["cps"] - 1) * 100:+.1f}%)')

    # ---------- B3 ----------
    tieu_de('B3 · Giới hạn chạy lại và chi phí cả hệ thống (simulated)')
    print(f'{"gioi_han":9s} {"tong_tro_ly":>12s} {"khong_tc":>9s} {"ca_he_thong":>12s} {"cps":>8s}')
    for k in [1, 2, 3]:
        m = mo_hinh(runs, reqs, max_lan_chay=k)
        ktc = len(reqs) - m['thanh_cong']
        print(f'{k:9d} {m["tong"]:12,.0f} {ktc:9d} {m["tong"] + ktc * BASELINE:12,.0f} {m["cps"]:8,.0f}')

    # ---------- B4 ----------
    tieu_de('B4 · Xem lại 100% cho noi_dia + hang_nang (simulated)')
    PHUT_XEM, PHUT_LAM = 5, 9   # giả định của đề cho B4
    so_ok = runs[(runs['status'] == 'ok') & runs['request_id'].isin(pv['request_id'])]['request_id'].nunique()
    so_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    token_tool = m_pv['token'] + m_pv['tool']
    phut_lam_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print(f'{so_ok} yêu cầu có lần chạy ok, {so_lam_lai} ca làm lại, token + tool {token_tool:,.0f} đ, '
          f'{m_pv["thanh_cong"]} việc thành công')
    for phut_lam in [PHUT_LAM, phut_lam_tb]:
        tong = so_ok * PHUT_XEM * LUONG_PHUT + so_lam_lai * phut_lam * LUONG_PHUT + token_tool
        cps = tong / m_pv['thanh_cong']
        hoa_von = (BASELINE * m_pv['thanh_cong'] - token_tool - so_lam_lai * phut_lam * LUONG_PHUT) / (so_ok * LUONG_PHUT)
        print(f'làm lại {phut_lam:4.1f} phút/ca: tổng {tong:,.0f} đ · cps {cps:,.0f} đ = {cps / BASELINE:.2f}× '
              f'· hoà vốn khi xem lại ≤ {hoa_von:.1f} phút')

    # CP4 · Nhiệm vụ D: cỡ mẫu (dùng statistics.NormalDist, không cần statsmodels).
    nhiem_vu_d(reqs)
