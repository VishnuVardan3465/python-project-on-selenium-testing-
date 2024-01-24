import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))

#driver.get("https://google.com")
#googlesearchbox = driver.find_element(By.ID,"APjFqb")
#googlesearchbox.send_keys("cgi")
#googlesearchbox.send_keys(Keys.RETURN)
#driver.find_element(By.NAME,"btnK").click()
#time.sleep(3)
#print("done")
driver.get("https://trytestingthis.netlify.app/")
driver.find_element(By.ID,"fname").send_keys("vishnu")
time.sleep(2)
driver.find_element(By.ID,"lname").send_keys("vardan")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
time.sleep(5)


