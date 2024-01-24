import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))

driver.get("https://google.com")
time.sleep(120)
driver.close()
driver.quit()
print("done")


