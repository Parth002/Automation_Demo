import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Setup: Initialize the browser
    driver = webdriver.Chrome()
    driver.implicitly_wait(10) # Modern wait strategy
    driver.maximize_window()
    
    yield driver # This is where the test happens
    
    # Teardown: Close the browser after the test is done
    driver.quit()