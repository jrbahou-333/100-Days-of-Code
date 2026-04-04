from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from threading import Timer
import time

service = Service("/Users/jackbahou/Applications/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/cookieclicker/")


def purchase_upgrade():
    try:
        available_list = driver.find_elements(By.CLASS_NAME, "product.unlocked.enabled")
        available_list[-1].click()

    except:
        pass

    Timer(5, purchase_upgrade).start()


time.sleep(5)
english = driver.find_element(By.ID, "langSelect-EN")
english.click()
time.sleep(5)

purchase_upgrade()

cookie = driver.find_element(By.ID, "bigCookie")

while True:
    cookie.click()



