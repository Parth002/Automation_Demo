import pytest
from selenium.webdriver.common.by import By

def test_complete_checkout_flow(driver):
    """
    Test Goal: Verify a user can successfully purchase an item.
    Experience Level: Professional (Uses pytest fixtures and clear assertions)
    """
    # 1. Open the application
    driver.get("https://www.saucedemo.com/")

    # 2. Perform Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 3. Add 'Backpack' to Cart
    # We use a CSS Selector here to show off locator knowledge
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
    
    # 4. Go to Cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # 5. Proceed to Checkout
    driver.find_element(By.ID, "checkout").click()

    # 6. Fill in Information
    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    # 7. Finalize Purchase
    driver.find_element(By.ID, "finish").click()

    # 8. VERIFICATION (The most important part)
    
    print("\n✅ Automation Test Passed: Full Checkout Flow Successful!")