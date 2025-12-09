# import feedparser
import requests
import xml.etree.ElementTree as et

url = "https://feeds.bbci.co.uk/news/rss.xml"
response = requests.get(url)
content = response.content
print(content)
feed = et.parse(content)
# feed = feedparser.parse(url)

for article in feed.entries[:5]:
    print(f"-{article.published}: {article.title} -> ({article.link})")

