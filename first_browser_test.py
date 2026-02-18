from selenium import webdriver

# 1. Initialize the "Driver" (This opens the browser)
driver = webdriver.Chrome()

# 2. Go to a website
driver.get("https://www.google.com")

# 3. Get the title of the page
page_title = driver.title

# 4. The Assertion (The 'Check' step)
if "Google" in page_title:
    print("TEST PASSED: The title is correct!")
else:
    print("TEST FAILED: Title is wrong.")

# 5. Close the browser
driver.quit()