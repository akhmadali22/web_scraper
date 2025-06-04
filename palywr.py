import os
import pandas as pd
from playwright.sync_api import sync_playwright

df_urls = pd.read_csv("url_rumah123.csv")
output_file = "data_properti_detail_rumah123.csv"
fail_file = "detail_rumah12_fail.csv"

if not os.path.exists(output_file):
    pd.DataFrame(columns=[
        "URL", "Lokasi", "Harga", "Luas Bangunan", "Luas Tanah",
        "Kamar Tidur", "Kamar Mandi", "Garasi", "Jumlah Lantai"
    ]).to_csv(output_file, index=False, encoding="utf-8-sig")

if not os.path.exists(fail_file):
    pd.DataFrame(columns=["URL"]).to_csv(fail_file, index=False, encoding="utf-8-sig")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    for index, row in df_urls.iterrows():
        url = row["URL"]
        print(f"🔎 Mengunjungi: {url}")
        try:
            page.goto(url, timeout=60000)

            # Scroll dan klik tombol "Lihat Semua"
            page.locator("button:has-text('Lihat Semua')").click(timeout=10000)
            page.wait_for_timeout(3000)

            lokasi = page.locator("p.text-xs.text-gray-500.mb-2").text_content()
            harga = page.locator("span.text-primary.font-bold.whitespace-pre").text_content()

            data_detail = {
                "URL": url,
                "Lokasi": lokasi,
                "Harga": harga,
                "Luas Bangunan": "-",
                "Luas Tanah": "-",
                "Kamar Tidur": "-",
                "Kamar Mandi": "-",
                "Garasi": "-",
                "Jumlah Lantai": "-"
            }

            for detail in page.locator("div.mb-4.flex.items-center.gap-4.text-sm.border-0.border-b.border-solid.border-gray-200.pb-2").all():
                key_val = detail.locator("p").all()
                if len(key_val) >= 2:
                    key = key_val[0].text_content().strip()
                    val = key_val[1].text_content().strip()
                    if key in data_detail:
                        data_detail[key] = val
                    elif key in ["Carport", "Garasi"]:
                        data_detail["Garasi"] = val

            pd.DataFrame([data_detail]).to_csv(output_file, mode='a', header=False, index=False, encoding="utf-8-sig")
            print(f"✅ Berhasil ambil dan simpan: {url}")
        except Exception as e:
            print(f"⚠️ Gagal ambil data dari {url}: {e}")
            pd.DataFrame([{"URL": url}]).to_csv(fail_file, mode='a', header=False, index=False, encoding="utf-8-sig")
            continue

    browser.close()
