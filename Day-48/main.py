from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("/Users/jackbahou/Applications/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.com.au/Instant-Pot-112-0098-01-Multi-Use-Stainless/dp/B08P2ZTTG7/ref=asc_df_B08P2ZTTG7/?tag=googleshopdsk-22&linkCode=df0&hvadid=463522673025&hvpos=&hvnetw=g&hvrand=1795880845763828232&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9069101&hvtargid=pla-1066028009245&psc=1")
parent_tag = driver.find_element(By.CLASS_NAME,'nav-logo-sprites' )
print(parent_tag)




# whole browser
driver.quit()

# one tab
# driver.close()