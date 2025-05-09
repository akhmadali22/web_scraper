import pandas as pd
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Baca file CSV URL
df_url = pd.read_csv("url_dan_lokasi_properti123_batch2.csv")

# Setup headless Chrome
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(options=options)

# Nama file hasil
output_file = "data_properti_detail_lengkap.csv"

# Tulis header hanya jika file belum ada
if not os.path.exists(output_file):
    pd.DataFrame(columns=[
        "URL", "Lokasi", "Harga", "Luas Bangunan", "Luas Tanah",
        "Kamar Tidur", "Kamar Mandi", "Garasi", "Jumlah Lantai"
    ]).to_csv(output_file, index=False, encoding="utf-8-sig")

count = 0

for index, row in df_url.iterrows():
    url = row["URL"]
    lokasi = row["Lokasi"]
    harga = row["Harga"]
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.meta"))
        )

        def get_spec(selector):
            try:
                return driver.find_element(By.CSS_SELECTOR, selector).text.strip()
            except:
                return "-"

        luas_bangunan = get_spec("div.area span:nth-child(2)")
        kamar_tidur = get_spec("div.bedroom span:nth-child(2)")
        kamar_mandi = get_spec("div.bathroom span:nth-child(2)")
        garasi = get_spec("div.garage span:nth-child(2)")

        info_items = driver.find_elements(By.CSS_SELECTOR, "div.property-info div.item.row")
        jumlah_lantai = "-"
        luas_tanah = "-"
        for item in info_items:
            try:
                tipe = item.find_element(By.CSS_SELECTOR, ".type").text.strip().lower()
                value = item.find_element(By.CSS_SELECTOR, ".value").text.strip()
                if "jumlah lantai" in tipe:
                    jumlah_lantai = value
                elif "luas tanah" in tipe:
                    luas_tanah = value
            except:
                continue

        row_data = {
            "URL": url,
            "Lokasi": lokasi,
            "Harga": harga,
            "Luas Bangunan": luas_bangunan,
            "Luas Tanah": luas_tanah,
            "Kamar Tidur": kamar_tidur,
            "Kamar Mandi": kamar_mandi,
            "Garasi": garasi,
            "Jumlah Lantai": jumlah_lantai
        }

        # Simpan langsung ke CSV (append, tanpa header)
        pd.DataFrame([row_data]).to_csv(output_file, mode='a', header=False, index=False, encoding="utf-8-sig")

        print(f"✅ Berhasil ambil dan simpan: {url}")
        count += 1

    except Exception as e:
        print(f"❌ Gagal ambil data dari {url}: {e}")
    if count == 40:
        print("🔄 Istirahat sejenak...")
        time.sleep(2)
        count = 0
        driver.quit()


print(f"🎉 Semua data sudah disimpan ke '{output_file}'")