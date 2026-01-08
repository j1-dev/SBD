import requests
import re
import hashlib
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

URL_BASE = "https://books.toscrape.com/"
GBP_A_EUR = 1.17

MAPA_VALORACION = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

Base = declarative_base()

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True)

    libros = relationship("Libro", back_populates="categoria")

class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    precio_eur = Column(Float)
    disponible = Column(Boolean)
    unidades = Column(Integer)
    valoracion = Column(Integer)
    hash = Column(String, unique=True)

    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    categoria = relationship("Categoria", back_populates="libros")

def limpiar_titulo(titulo):
    return re.sub(r'[",:\.\s]', '', titulo.upper())

def generar_hash(titulo):
    return hashlib.sha256(limpiar_titulo(titulo).encode()).hexdigest()

motor = create_engine("sqlite:///libros.db")
Sesion = sessionmaker(bind=motor)
sesion = Sesion()
s = requests.Session()

url_pagina = "catalogue/page-1.html"

while url_pagina:
    sopa = BeautifulSoup(
        s.get(URL_BASE + url_pagina).text, "html.parser"
    )

    for libro in sopa.select(".product_pod"):
        url_detalle = URL_BASE + "catalogue/" + libro.h3.a["href"].replace("../", "")
        sopa_detalle = BeautifulSoup(s.get(url_detalle).text, "html.parser")

        titulo = sopa_detalle.h1.text.strip()
        hash_libro = generar_hash(titulo)

        if sesion.query(Libro).filter_by(hash=hash_libro).first():
            continue  # evitar duplicados

        texto_precio = sopa_detalle.select_one(".price_color").text
        precio_gbp = float(re.search(r"\d+\.\d+", texto_precio).group())
        precio_eur = round(precio_gbp * GBP_A_EUR, 2)

        texto_disponibilidad = sopa_detalle.select_one(".availability").text.strip()
        disponible = "In stock" in texto_disponibilidad
        unidades = int(re.search(r"\d+", texto_disponibilidad).group())

        texto_valoracion = sopa_detalle.select_one("p.star-rating")["class"][1]
        valoracion = MAPA_VALORACION[texto_valoracion]

        nombre_categoria = sopa_detalle.select(".breadcrumb li a")[2].text.strip()
        categoria = sesion.query(Categoria).filter_by(nombre=nombre_categoria).first()

        if not categoria:
            categoria = Categoria(nombre=nombre_categoria)
            sesion.add(categoria)
            sesion.commit()

        libro_db = Libro(
            titulo=titulo,
            precio_eur=precio_eur,
            disponible=disponible,
            unidades=unidades,
            valoracion=valoracion,
            hash=hash_libro,
            categoria=categoria
        )

        sesion.add(libro_db)
        sesion.commit()

    boton_siguiente = sopa.select_one(".next a")
    url_pagina = boton_siguiente["href"] if boton_siguiente else None

print("✅ ETL avanzado completado")