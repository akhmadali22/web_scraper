import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

# Load URL hasil scraping sebelumnya
df_urls = pd.read_csv("url_rumah123.csv")

# Setup Chrome headless
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')

output_file = "data_properti_detail_rumah123.csv"

if not os.path.exists(output_file):
    pd.DataFrame(columns=[
        "URL", "Lokasi", "Harga", "Luas Bangunan", "Luas Tanah",
        "Kamar Tidur", "Kamar Mandi", "Garasi", "Jumlah Lantai"
    ]).to_csv(output_file, index=False, encoding="utf-8-sig")

for index, row in df_urls.iterrows():
    url = row["URL"]
    print(f"🔎 Mengunjungi: {url}")
    try:
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
        )
        try:
            wait = WebDriverWait(driver, 10)
            lihat_semua_btn = wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR,
                r"button.text-primary.text-sm.w-full.flex.justify-center.md\:justify-start.py-2.items-center.gap-2.cursor-pointer.mt-4"
            )))

            # Scroll ke tombol dan klik
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", lihat_semua_btn)
            time.sleep(1)  # beri waktu animasi scroll selesai
            ActionChains(driver).move_to_element(lihat_semua_btn).click().perform()

            # Tunggu detail tambahan dimuat (sesuaikan waktu jika perlu)
            time.sleep(2)

            # Ambil semua detail
            details = driver.find_elements(By.CSS_SELECTOR,
                "div.mb-4.flex.items-center.gap-4.text-sm.border-0.border-b.border-solid.border-gray-200.pb-2")

            for detail in details:
                key_val = detail.find_elements(By.TAG_NAME, "p")
                if len(key_val) >= 2:
                    key = key_val[0].text.strip()
                    val = key_val[1].text.strip()
                    print(f"{key}: {val}")

        except Exception as e:
            print("⚠️ Gagal klik tombol: ", e)

        try:
            harga_elem = driver.find_element(
                By.CSS_SELECTOR,
                "span.text-primary.font-bold.whitespace-pre"
            )
            harga = harga_elem.text.strip()
        except:
            harga = "-"

        try:
            lokasi_elem = driver.find_element(
                By.CSS_SELECTOR,
                "p.text-xs.text-gray-500.mb-2"
            )
            lokasi = lokasi_elem.text.strip()
        except:
            lokasi = "-"

        luas_bangunan = "N/A"
        try:
            detail_divs = driver.find_elements(By.CSS_SELECTOR, "div.mb-4.flex.items-center.gap-4.text-sm")

            for div in detail_divs:
                labels = div.find_elements(By.TAG_NAME, "p")
                if len(labels) >= 2:
                    key = labels[0].text.strip()
                    value = labels[1].text.strip()
                    print(f"{key}: {value}")
        except Exception as e:
            print(f"Gagal ambil Luas Bangunan: {e}")


        row_data = {
            "URL": url,
            "Lokasi": lokasi,
            "Harga": harga,
            "Luas Bangunan": luas_bangunan,
            "Luas Tanah": "test",
            "Kamar Tidur": "test",
            "Kamar Mandi": "test",
            "Garasi": "test",
            "Jumlah Lantai": "test"
        }
        pd.DataFrame([row_data]).to_csv(output_file, mode='a', header=False, index=False, encoding="utf-8-sig")
        print(f"✅ Berhasil ambil dan simpan: {url}")
        time.sleep(2)  # delay untuk menghindari blok
        driver.quit()

    except Exception as e:
        print(f"⚠️ Gagal ambil data dari {url}: {e}")
        continue


# Simpan hasil detail
print("📁 Detail listing berhasil disimpan ke 'detail_rumah123.csv'")
