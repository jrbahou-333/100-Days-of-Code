from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

#Writing our First Selenium Python Test
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
web = "https://www.bet365.com.au/#/AS/B36/"
path = '/Users/jackbahou/Downloads/chromedriver'
driver.get(web)


# #Make ChromeDriver click a button
# time.sleep(15) #add implicit wait, if necessary
# accept = driver.find_element_by_xpath('//*[@id="_evidon-accept-button"]')
# accept.click()

#Initialize your storage
teams = []
x12 = [] #3-way
odds_events = []

#scroll down to the bottom to load upcoming matches (update 2: not necessary anymore)
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#time.sleep(3) #add implicit wait to let the driver load the elements of the upcoming matches section.

#select only upcoming matches box
box = driver.find_element_by_xpath('//div[contains(@testid, "Program_SELECTION")]') #update 3
#Looking for 'sports titles'
sport_title = box.find_elements_by_class_name('SportTitle-styles-sport')

for sport in sport_title:
    # selecting only football
    if sport.text == 'Football':
        parent = sport.find_element_by_xpath('./..') #immediate parent node
        grandparent = parent.find_element_by_xpath('./..') #grandparent node = the whole 'football' section
        #Looking for single row events
        single_row_events = grandparent.find_elements_by_class_name('EventRow-styles-event-row')
        #Getting data
        for match in single_row_events:
            #'odd_events'
            odds_event = match.find_elements_by_class_name('EventOddGroup-styles-odd-groups')
            odds_events.append(odds_event)
            # Team names
            for team in match.find_elements_by_class_name('EventTeams-styles-titles'):
                teams.append(team.text)
        #Getting data: the odds
        for odds_event in odds_events:
            for n, box in enumerate(odds_event):
                rows = box.find_elements_by_xpath('.//*')
                if n == 0:
                    x12.append(rows[0].text)

driver.quit()
#Storing lists within dictionary
dict_gambling = {'Teams': teams, '1x2': x12}
#Presenting data in dataframe
df_gambling = pd.DataFrame.from_dict(dict_gambling)
print(df_gambling)