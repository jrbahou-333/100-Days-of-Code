from bs4 import BeautifulSoup
import requests

request = requests.get("https://www.goldbet.com.au/Racing/Thoroughbreds/Wyong/R2/346628")
website = request.text

soup = BeautifulSoup(website, "html.parser")

odds_tags = soup.find_all("a", role="button")

odds_list = [odds_tag.getText() for odds_tag in odds_tags]

horse_tags =  soup.findAll("div", class_="title")
horses = [horse_tag.find("span", class_="name").getText() for horse_tag in horse_tags]
print (odds_list)
print(horses)

odds_list = odds_list[33::1]

odds = []
for odd in odds_list:
    try:
        odd = float(odd)

    except:
        pass

    else:
        odds.append(odd)

print (odds)

