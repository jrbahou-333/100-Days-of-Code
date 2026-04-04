from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("/Users/jackbahou/Applications/chromedriver")
driver = webdriver.Chrome(service=service)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# articles_tag = driver.find_element(By.CSS_SELECTOR, "#articlecount > a")
# english = driver.find_element(By.LINK_TEXT, "English")
# search_tag = driver.find_element(By.NAME, "search")
# search_tag.send_keys("Python")
# search_tag.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Jim")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Bob")

email = driver.find_element(By.NAME, "email")
email.send_keys("JimBob@gmail.gey")

sign_up = driver.find_element(By.CSS_SELECTOR, "form > button")
sign_up.click()









