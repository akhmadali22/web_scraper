from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

url = "https://www.properti123.com/properti-jual?post_date=DESC&free_text=jakarta&listing_type=SALE&property_type=rumah"
driver.get(url)

# Tunggu sampai <li class="listing-item"> muncul
WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.listing-item"))
)

listings = driver.find_elements(By.CSS_SELECTOR, "li.listing-item")

# Print isi HTML dari satu listing
for i, listing in enumerate(listings[:1]):
    print("----- LISTING HTML -----")
    print(listing.get_attribute("innerHTML"))

driver.quit()