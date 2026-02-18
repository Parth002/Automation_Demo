import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_complete_checkout_flow(driver):
    """
    Test Goal: Verify a user can successfully purchase an item.
    """
    # 1. Open the application
    driver.get("https://www.saucedemo.com/")

    # 2. Perform Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
  
    # 3. Add 'Backpack' to Cart
    
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
    
    # 4. Go to Cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # 5. Proceed to Checkout
    driver.find_element(By.ID, "checkout").click()

    # 6. Fill in Information
    driver.find_element(By.ID, "first-name").send_keys("Test")
    time.sleep(2)
    driver.find_element(By.ID, "last-name").send_keys("User")
    time.sleep(2)
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    time.sleep(2)
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)

    # 7. Finalize Purchase
    driver.find_element(By.ID, "finish").click()
    time.sleep(2)
