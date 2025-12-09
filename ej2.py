import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
article_list = soup.find_all("span","titleline")

for article in article_list:
    title = article.find("a").get_text()
    print(title)