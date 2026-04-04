from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("/Users/jackbahou/Applications/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")


content_tag = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]')
dates_tags = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last > div > ul > li > time")
events_tags = content_tag.find_elements(By.TAG_NAME, "a")

print(dates_tags)
dates = [date.get_attribute("datetime")[:-15] for date in dates_tags]
print(dates)
events = [event.text for event in events_tags]
events = events[1::]

event_dict = {}

for event in events:
    event_index = events.index(event)
    event_dict[event_index] = {}
    event_dict[event_index]["time"] = dates[event_index]
    event_dict[event_index]["name"] = event

print(event_dict)


driver.quit()