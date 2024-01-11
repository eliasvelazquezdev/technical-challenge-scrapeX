from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to execute when this script is run instead of imported
def main_greeting():
    return "Executing script"

def get_product_info(product: str) -> dict:
    """
    Takes a string with a product name and searches for it on a supermarket website.

    Returns a dictionary with product name, description, price, category, url and picture url after scraping the website.
    """    

    driver = webdriver.Chrome()
    driver.get("https://www.cotodigital3.com.ar/sitios/cdigi/")
    
    # Try to get search bar element
    try:
        # Wait 10 seconds until the element (search bar) is found and clickable
        searchInput = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "atg_store_search_max_length")]/input[@id="atg_store_searchInput"]'))
        )

        # Search product
        searchInput.clear()
        searchInput.send_keys(product)
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

    driver.close()

    return {
        "name" : product_name,
        "description" : product_description,
        "price" : product_price,
        "category" : product_category,
        "picture" : product_picture_url,
        "url" : product_url,
    }

if __name__ == "__main__":
    main_greeting()