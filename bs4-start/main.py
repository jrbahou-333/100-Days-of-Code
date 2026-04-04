from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
YC_web_page = response.text

soup = BeautifulSoup(YC_web_page, "html.parser")
article_tags = soup.find_all("a", class_="titlelink")

article_texts = []
article_links = []

for tag in article_tags:
    article_texts.append(tag.getText())
    article_links.append(tag.get("href"))

article_scores = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]


# print(article_texts)
# print(article_links)
# print(article_scores)

index = article_scores.index(max(article_scores))

print(article_texts[index], article_links[index], article_scores[index])








# with open("website.html", "r") as f:
#     content = f.read()
#
# soup = BeautifulSoup(content, "html.parser")

