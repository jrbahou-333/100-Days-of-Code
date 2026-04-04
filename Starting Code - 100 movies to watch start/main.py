import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

request = requests.get(URL)
web_page = request.text

soup = BeautifulSoup(web_page, "html.parser")

film_tags = soup.find_all(name="h3", class_="title")

film_list = [film_tag.getText() for film_tag in film_tags]

film_list = film_list[::-1]

with open("film_data_new", "w") as f:
    for film in film_list:
        f.write(film + "\n")
