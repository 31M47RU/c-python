import requests
from bs4 import BeautifulSoup

### NOTICIAS ###
url_lanacion  = "https://www.lanacion.com.ar/"

def getNoticias():
    response = requests.get(url_lanacion)
    soup = BeautifulSoup(response.text, 'html.parser')

    noticias = []

    for data_pos_value in ["0301", "0302", "0303", "0304", "0305"]:
        selector = f"article[data-pos='{data_pos_value}'] a"
        enlaces_articulos = soup.select(selector)
        
        for enlace in enlaces_articulos:
            title_text = enlace.text
            title_link = enlace['href']
            noticias.append((title_text, title_link))
    
    return noticias



### DOLAR ###
url_dolarhoy = "https://www.dolarhoy.com/"

def get_dollar_price(type):
    response = requests.get(url_dolarhoy)

    soup = BeautifulSoup(response.text, "html.parser")

    a_tag = soup.find("a", text="Dólar blue")

    if a_tag:
        values_div = a_tag.find_next("div", class_="values")
        compra_div = values_div.find("div", class_="compra")
        venta_div = values_div.find("div", class_="venta")

        if type == "compra":
            compra_valor = compra_div.find("div", class_="val").text
            return compra_valor
        elif type == "venta":
            venta_valor = venta_div.find("div", class_="val").text
            return venta_valor
    else:
        return "No se encontró la etiqueta <a> con el texto 'Dólar blue'"

