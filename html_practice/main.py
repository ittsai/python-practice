# web scraping, beautiful soup
# import os (os.environ[""])
# from dotenv import load_dotenv (load .env file)

from bs4 import BeautifulSoup
import requests
STATIC_WEBSITE = "https://appbrewery.github.io/news.ycombinator.com/"

response = requests.get(STATIC_WEBSITE)
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

# Title
print(soup.title)

# article
article_tag = soup.find(name="a", class_="storylink")
print(article_tag.getText())
article_link = article_tag.get("href")
print(article_link)
article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
print(article_upvotes)
# with open("website.html") as file:#
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)
# print(soup.prettify())
# print(soup.findAll(name="a"))

# for tag in soup.findAll(name="a"):
#     print(tag.get("href"))
#
# company_url = soup.select_one(selector="p a")