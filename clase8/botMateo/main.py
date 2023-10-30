import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import time

token = ""

intents = discord.Intents.all()
bot = commands.Bot(
    command_prefix="!",
    description="Bot para obtener las últimas noticias del momento",
    intents=intents,
)

url = "https://www.lanacion.com.ar/"

def getNoticias():
    response = requests.get(url)
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

@bot.command()
async def n(ctx, numero=None):
    print("comando recibido")
    noticias = getNoticias()

    if numero is not None and numero.isnumeric() and 1 <= int(numero) <= 5:
        # Obtén la noticia específica según el número proporcionado
        index = int(numero) - 1
        if index < len(noticias):
            tTexto, tLink = noticias[index]
            punto = tTexto.find(".")
            if punto != -1:
                title = tTexto[:punto + 1]
                descr = tTexto[punto + 1:]
            else:
                title = tTexto
                descr = ""
            link = f"{url}{tLink}"
            mensajeFinal = f"> ## [{title}]({link})\n * _{descr}_\n"
            await ctx.send(mensajeFinal)
    else:
        for tTexto, tLink in noticias:
            punto = tTexto.find(".")
            if punto != -1:
                title = tTexto[:punto + 1]
                descr = tTexto[punto + 1:]
            else:
                title = tTexto
                descr = ""
            link = f"{url}{tLink}"
            mensajeFinal = f"> ## [{title}]({link})\n * _{descr}_\n"
            await ctx.send(mensajeFinal)
        time.sleep(0.5)

@bot.event
async def on_ready():
    print(f"\nBot is ready. Connected to {len(bot.guilds)} servers.")

bot.run(token)
