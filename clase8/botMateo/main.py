import discord
from discord.ext import commands
import time
import asyncio
from forex_python.converter import CurrencyRates
from scrapper import *

token_ = "TOKEN.MTE2ODMzMDE2MTM3MzA3MzQyOA.GDUwJd.97VUeN7CWDBpZtnHHFQLN4EPjUodYaL1yxCRfY"
token = token_.replace("TOKEN.", "")

intents = discord.Intents.all()
bot = commands.Bot(
    command_prefix="!",
    description="Bot multifuncion",
    intents=intents,
)

c = CurrencyRates()

def convert_ars_usd(amount = 0):
    venta = get_dollar_price("venta")
    venta_value = float(venta.split(" ")[1].replace(",", "."))
    result = amount / venta_value
    return round(result, 2)

def convert_usd_ars(amount = 0):
    compra = get_dollar_price("compra")
    compra_value = float(compra.split(" ")[1].replace(",", "."))
    result = amount * compra_value
    return round(result, 2)

async def send_news_daily():
    channel_name = "general"
    channel = discord.utils.get(bot.get_all_channels(), name=channel_name)

    if channel is None:
        print(f"No se pudo encontrar el canal con el nombre '{channel_name}'. Asegúrate de que el bot tenga acceso al canal.")
        return

    while True:
        await asyncio.sleep(86400)

        noticias = getNoticias()

        for tTexto, tLink in noticias:
            punto = tTexto.find(".")
            if punto != -1:
                title = tTexto[:punto + 1]
                descr = tTexto[punto + 1:]
            else:
                title = tTexto
                descr = ""
            link = f"{url_dolarhoy}{tLink}"
            mensajeFinal = f"> ## [{title}]({link})\n * _{descr}_\n"

            await channel.send(mensajeFinal)

@bot.command()
async def n(ctx, numero=None):
    print("comando recibido")
    noticias = getNoticias()

    if numero is not None and numero.isnumeric() and 1 <= int(numero) <= 5:
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
            link = f"{url_lanacion}{tLink}"
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
            link = f"{url_lanacion}{tLink}"
            mensajeFinal = f"> ## [{title}]({link})\n * _{descr}_\n"
            await ctx.send(mensajeFinal)
        time.sleep(0.5)

@bot.command()
async def dolar(ctx):
    print("Command received")
    await ctx.send(f"El dolar blue esta\nCompra: {get_dollar_price('compra')}\nVenta: {get_dollar_price('venta')}")

@bot.event
async def on_ready():
    print(f"\nBot is ready. Connected to {len(bot.guilds)} servers.")
    bot.loop.create_task(send_news_daily())

bot.run(token)