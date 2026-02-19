import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_window_and_alert_handling(driver):
    """
    Goal: Demonstrate browser focus switching and alert management.
    """
    driver.get("https://the-internet.herokuapp.com/windows")
    wait = WebDriverWait(driver, 10)

    # --- 1. HANDLING MULTIPLE WINDOWS ---
    # Store the ID of the original window
    original_window = driver.current_window_handle

    # Click a link that opens a new tab
    driver.find_element(By.LINK_TEXT, "Click Here").click()

    # Wait for the new window to open and switch to it
    wait.until(EC.number_of_windows_to_be(2))
    
    # Loop through window handles to find the new one
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Verify we are on the new page
    assert "New Window" in driver.page_source
    print("✅ Successfully switched to New Tab")

    # Close new tab and go back to original
    driver.close()
    driver.switch_to.window(original_window)

    # --- 2. HANDLING JAVASCRIPT ALERTS ---
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    
    # Trigger a 'Confirm' alert
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    
    # Wait for the alert to appear and switch focus to it
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    
    print(f"Alert text found: {alert.text}")
    alert.accept() # Clicks 'OK'
    
    # Verify the result text on the page
    result = driver.find_element(By.ID, "result").text
    assert "You clicked: Ok" in result
    print("✅ Successfully handled JS Alert")