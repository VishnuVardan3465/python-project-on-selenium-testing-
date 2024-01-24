import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()


def test_google_search(driver):

    driver.get("https://google.com")
    googlesearchbox = driver.find_element(By.ID,"APjFqb")
    googlesearchbox.send_keys("CTS")
    googlesearchbox.send_keys(Keys.RETURN)
    time.sleep(2)
    print("test successful")
