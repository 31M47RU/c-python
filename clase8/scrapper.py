import requests
from bs4 import BeautifulSoup

url = "https://www.infodolar.com/"


def get_dollar_price(type):
    # Send a GET request to the website
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all elements with class name "colCompraVenta"
    elements = soup.find_all(class_="colCompraVenta")

    if type == "compra":
        return elements[0].text.strip().split("\n")[0]
    elif type == "venta":
        return elements[1].text.strip().split("\n")[0]
