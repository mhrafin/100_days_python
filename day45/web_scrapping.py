from bs4 import BeautifulSoup
import requests
# with open("day45/website.html") as html_file:
#     content = html_file.read()

# soup = BeautifulSoup(content, "html.parser")

response = requests.get(url="https://news.ycombinator.com/news")

html = response.text

soup = BeautifulSoup(html, "html.parser")

article_titles = []
article_links = []


articles = soup.find_all("span", class_="titleline")
for article_tag in articles:
    title = article_tag.find("a").get_text()
    article_titles.append(title)
    link = article_tag.find("a").get("href")
    article_links.append(link)
article_subline = soup.find_all("span", class_="score")
article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all("span", class_="score")]

print(article_titles)
print(article_links)
print(article_upvotes)

highest_article = article_upvotes.index(max(article_upvotes))
print()
print(article_titles[highest_article])
print(article_links[highest_article])
print(article_upvotes[highest_article])



# for link in soup.find_all("span"):
#     print(link.get("href"))
