from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.cotodigital3.com.ar/sitios/cdigi/")

# Wait 10 seconds until the element (search bar) is found and clickable
try:
    searchInput = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "atg_store_search_max_length")]/input[@id="atg_store_searchInput"]'))
    )
except Exception as e:
    print(e)

    
searchInput.clear()
searchInput.send_keys("gaseosa coca cola 2.5")
searchInput.click()
time.sleep(1)
searchInput.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
searchInput.send_keys(Keys.ENTER)
time.sleep(3)



driver.close()