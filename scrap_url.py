import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup headless Chrome
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

# Base URL template
base_url = "https://www.properti123.com/properti-jual?post_date=DESC&free_text=jakarta&listing_type=SALE&property_type=rumah&page={}"

data = []

# Ambil URL dan lokasi dari 167 halaman
for page in range(170, 221):
    print(f"🔄 Mengunjungi halaman {page}...")
    driver.get(base_url.format(page))
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.listing-item"))
        )
        listings = driver.find_elements(By.CSS_SELECTOR, "li.listing-item")
        for item in listings:
            try:
                url = item.find_element(By.CSS_SELECTOR, "div.property-grid > a").get_attribute("href")
                lokasi = item.find_element(By.CSS_SELECTOR, "span.location").text.strip()
                harga = item.find_element(By.CSS_SELECTOR, "span.price").text.strip()
                data.append({"URL": url, "Lokasi": lokasi, "Harga": harga})
            except Exception as inner_e:
                print(f"⚠️ Gagal ambil salah satu listing: {inner_e}")
        print(f"✅ {len(listings)} listing diproses di halaman {page}")
    except Exception as e:
        print(f"❌ Gagal ambil dari halaman {page}: {e}")

driver.quit()

print(f"🎯 Total listing terkumpul: {len(data)}")

# Simpan ke CSV
df = pd.DataFrame(data)
df.to_csv("url_dan_lokasi_properti123_batch2.csv", index=False, encoding="utf-8-sig")

print("📁 URL dan lokasi berhasil disimpan ke 'url_dan_lokasi_properti123_batch2.csv'")