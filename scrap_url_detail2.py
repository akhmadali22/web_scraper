import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium_stealth import stealth
import time

# Load URL hasil scraping sebelumnya
df_urls = pd.read_csv("data_baru.csv")

# Setup Chrome headless
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')

output_file = "detail_rumah123_new.csv"

fail_file = "detail_rumah12_fail.csv"

if not os.path.exists(output_file):
    pd.DataFrame(columns=[
        "URL", "Lokasi", "Harga", "Luas Bangunan", "Luas Tanah",
        "Kamar Tidur", "Kamar Mandi", "Garasi", "Jumlah Lantai"
    ]).to_csv(output_file, index=False, encoding="utf-8-sig")

if not os.path.exists(fail_file):
    pd.DataFrame(columns=[
        "URL", "Lokasi", "Harga", "Luas Bangunan", "Luas Tanah",
        "Kamar Tidur", "Kamar Mandi", "Garasi", "Jumlah Lantai"
    ]).to_csv(fail_file, index=False, encoding="utf-8-sig")

def create_driver():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    return webdriver.Chrome(options=options)


for index, row in df_urls.iterrows():
    url = row["URL"]
    driver = create_driver()
    wait = WebDriverWait(driver, 8)
    try:
        stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )
        driver.get(url)
        time.sleep(10)
        date_start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"🔎 [{date_start}] Mengunjungi: {url}")
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
        )
        print("🔄 Element body ditemukan...")
        lokasi = "-"
        harga = "-"
        luas_bangunan = "-"
        luas_tanah = "-"
        kamar_tidur = "-"
        kamar_mandi = "-"
        garasi = "-"
        jumlah_lantai = "-"
        try:
            print("🔄 Mencari Button...")
            wait_button = WebDriverWait(driver, 10)
            lihat_semua_btn = wait_button.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                r"button.text-primary.text-sm.w-full.flex.justify-center.md\:justify-start.py-2.items-center.gap-2.cursor-pointer.mt-4"
            )))
        except TimeoutException:
            print("Timeout. Button tidak ditemukan.")
            driver.save_screenshot("timeout_debug.png")
            continue

        # Scroll ke tombol dan klik
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", lihat_semua_btn)
        time.sleep(5)
        print("🔄 Klik Button...")  # beri waktu animasi scroll selesai
        ActionChains(driver).move_to_element(lihat_semua_btn).click().perform()

        # Tunggu detail tambahan dimuat (sesuaikan waktu jika perlu)
        time.sleep(5)
        print("🔄 Tunggu detail dimuat...")

        # Ambil semua detail
        details = driver.find_elements(By.CSS_SELECTOR,
            "div.mb-4.flex.items-center.gap-4.text-sm.border-0.border-b.border-solid.border-gray-200.pb-2")
        
        for detail in details:
            key_val = detail.find_elements(By.TAG_NAME, "p")
            if len(key_val) >= 2:
                key = key_val[0].text.strip()
                val = key_val[1].text.strip()
                if key == "Luas Bangunan":
                    luas_bangunan = val
                elif key == "Luas Tanah":
                    luas_tanah = val
                elif key == "Kamar Tidur":
                    kamar_tidur = val
                elif key == "Kamar Mandi":
                    kamar_mandi = val
                elif key == "Garasi" or key == "Carport":
                    garasi = val
                elif key == "Jumlah Lantai":
                    jumlah_lantai = val
        print("🔄 Ambil detail selesai...")
        harga_elem = driver.find_element(
            By.CSS_SELECTOR,
            "span.text-primary.font-bold.whitespace-pre"
        )
        harga = harga_elem.text.strip()

        lokasi_elem = driver.find_element(
            By.CSS_SELECTOR,
            "p.text-xs.text-gray-500.mb-2"
        )
        lokasi = lokasi_elem.text.strip()

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
        pd.DataFrame([row_data]).to_csv(output_file, mode='a', header=False, index=False, encoding="utf-8-sig")
        date_stop = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"✅ [{date_stop}] Berhasil ambil dan simpan")
        
    except Exception as e:
        print(f"⚠️ Gagal ambil data dari {url}: {e}")
        pd.DataFrame([{
            "URL": url,
        }]).to_csv(fail_file, mode='a', header=False, index=False, encoding="utf-8-sig")
        continue
    try:
        driver.quit()
        driver.service.stop()
        print("🔄 Close Driver...")
        time.sleep(10)
    except Exception as e:
        print(f"⚠️ Error saat quit driver: {e}")

# driver.quit()
# driver.service.stop()
# Simpan hasil detail
print("📁 Detail listing berhasil disimpan ke 'detail_rumah123.csv'")
