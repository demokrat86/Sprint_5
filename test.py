from selenium import webdriver

# Для Chrome
driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.quit()

# Для Firefox
driver = webdriver.Firefox()
driver.get("https://www.google.com")
driver.quit()
