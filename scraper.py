from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.cotodigital3.com.ar/sitios/cdigi/")

# Try to get search bar element
try:
    # Wait 10 seconds until the element (search bar) is found and clickable
    searchInput = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "atg_store_search_max_length")]/input[@id="atg_store_searchInput"]'))
    )

    #Search product
    searchInput.clear()
    searchInput.send_keys("gaseosa coca cola 2.5")
    searchInput.click()
    time.sleep(1)
    searchInput.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    searchInput.send_keys(Keys.ENTER)
    time.sleep(3)
except Exception as e:
    print(e)

    
try:
    # Get product's info box and click on it to go to product detail page
    product_info_box = driver.find_element(By.XPATH, '//span[contains(@class, "span_productName")]').click()
    time.sleep(3)

    product_name = driver.find_element(By.XPATH, '//h1[contains(@class, "product_page")]').get_attribute("innerHTML").strip()

    product_description = driver.find_element(By.XPATH, '//p[@id= "txtComentario"]').get_attribute("innerHTML").strip()
    
    product_price = driver.find_element(
        By.XPATH, 
        '(//span[contains(@class, "atg_store_productPrice")])[1]/span[contains(@class, "atg_store_newPrice")]'
    ).get_attribute('innerHTML').strip()

    product_category = driver.find_element(By.XPATH, '//div[@id= "atg_store_breadcrumbs"]/a[last()]/p').get_attribute("innerHTML").strip()

    product_picture_url = driver.find_element(By.XPATH, '//img[contains(@class, "zoomImg")]').get_attribute("src")

    product_url = driver.current_url
except Exception as e:
    print("Error!", e)


print(product_name)
print(product_description)
print(product_price)
print(product_category)
print(product_picture_url)
print(product_url)

driver.close()