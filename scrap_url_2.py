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

base_url = "https://www.rumah123.com/jual/dki-jakarta/rumah/?maxPrice=9000000000&minPrice=1000000000&sort=posted-desc&page={}"
data = []

for page in range(400, 452):  # ubah sesuai kebutuhan

    try:
        driver = webdriver.Chrome(options=options)
        print(f"🔄 Mengunjungi halaman {page}...")
        driver.get(base_url.format(page))
        WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.ID, "ui-search-page-id"))
        )

        # Ambil semua container listing
        listing_elements = driver.find_elements(By.CSS_SELECTOR, "div.ui-organism-intersection__element")

        for listing in listing_elements:
            try:
                anchor = listing.find_element(
                    By.CSS_SELECTOR,
                    "div.featured-card-component div.ui-atomic-card.card-featured div.card-featured__content-wrapper div.card-featured__middle-section > a"
                )
                url = anchor.get_attribute("href")
                if url:
                    data.append({"URL": url})
            except Exception:
                continue  # lewati jika tidak sesuai struktur
        driver.quit()

    except Exception as e:
        print(f"❌ Gagal ambil dari halaman {page}: {e}")


print(f"🎯 Total URL terkumpul: {len(data)}")

# Simpan ke CSV
df = pd.DataFrame(data)
df.to_csv("data_baru.csv", index=False, encoding="utf-8-sig")
print("📁 URL listing berhasil disimpan ke 'data_baru.csv'")
