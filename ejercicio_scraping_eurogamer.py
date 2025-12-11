# Hacer scrapping the https://eurogamer.es
# Obtener un CSV con fecha, titular y tipo de contenido
# Obtener 50 noticias

import requests
from bs4 import BeautifulSoup
import csv
import time

s = requests.Session()

# soup = BeautifulSoup(response.text, "html.parser")
# print(article_list)

with open('./games.csv', "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)        
    for page in range(1,3):
        url = f"https://www.eurogamer.es/archive?page={page}"
        response = s.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        article_list = soup.find_all("div","archive__details")
        # print(article_list)
        for quote in article_list:
            fecha = quote.find("time","archive__date").get_text()
            titulo = quote.find("h2", "archive__title").get_text().strip()
            tipo = quote.find("div", "archive__type").get_text().strip()
            # print("Artículo")
            # print(f"fecha: {fecha}")
            # print(f"titulo: {titulo}")
            # print(f"tipo: {tipo}")
            if titulo.find("|") != -1:
                titulo = titulo.split("|")[1].strip()
            writer.writerow([fecha,titulo,tipo])
        time.sleep(0.5)