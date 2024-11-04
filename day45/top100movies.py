import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
html = response.text

soup = BeautifulSoup(html, "html.parser")

movie_names = [movie.get_text() for movie in soup.find_all("h3", class_="title")]
movie_names.reverse()
print(movie_names)

with open("day45/Top 100 Movies.txt", mode="w") as file:
    file.writelines([f"{movie}\n" for movie in movie_names])

