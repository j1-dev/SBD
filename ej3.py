import requests
from bs4 import BeautifulSoup
import csv
import time

url = "https://quotes.toscrape.com/page/"
s = requests.Session()

# soup = BeautifulSoup(response.text, "html.parser")
# print(article_list)

with open('./quotes.csv', "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)        
    for page in range(1,11):
        url = f"https://quotes.toscrape.com/page/{page}"
        response = s.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        quote_list = soup.find_all("div","quote")
        for quote in quote_list:
            texto = quote.find("span","text").get_text()
            autor = quote.find("small", "author").get_text()
            tags = quote.find_all("a", "tag")
            tags_text = []
            for tag in tags:
                tags_text.append(tag.get_text())
            # print("QUOTE")
            # print(f"texto: {texto}")
            # print(f"autor: {author}")
            # print(f"tags: {tags_text}")
            # print(texto,autor,tags_text)
            writer.writerow([texto,autor,tags_text])
        time.sleep(0.5)