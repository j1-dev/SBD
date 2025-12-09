# Hacer scrapping the https://eurogamer.es
# TIENE TRUCO
# Obtener un CSV con fecha, titular y tipo de contenido
# Obtener 50 noticias
# Revisar bien el contenido y el HTML de la página
# Ser responsable (aplicar delay entre peticiones, no petar demasiado)

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
            # print(f"autor: {autor}")
            # print(f"tipo: {tipo}")
            writer.writerow([fecha,titulo,tipo])
        time.sleep(0.5)