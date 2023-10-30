import discord
from discord.ext import commands
from forex_python.converter import CurrencyRates
from scrapper import get_dollar_price

# Define the intents for the bot
intents = discord.Intents.all()
# Create a bot instance and specify the command prefix and intents
bot = commands.Bot(
    command_prefix="!",
    description="Convertidor de Dolar a Pesos argentinos y viceversa",
    intents=intents,
)

# Create a CurrencyRates instance
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


# Event to run when the bot is ready
@bot.event
async def on_ready():
    print(f"Bot is ready. Connected to {len(bot.guilds)} servers.")


@bot.event
async def on_message(message):
    # print("message: ", message)
    # print(f"USER - {message.author} texted - {message.content}")
    await bot.process_commands(message)


# Command to convert ARS to USD
@bot.command()
async def to_usd(ctx, amount: float = 0):
    print("Command received")
    if amount != 0:
        result = convert_ars_usd(amount)
        await ctx.send(f"**{amount}** ARS son **{result}** USD.")
    else:
        await ctx.send(f"""
----------
**!to_usd __amount__**
----------
"""
)


# Command to convert USD to ARS
@bot.command()
async def to_ars(ctx, amount: float = 0):
    print("Command received")
    if amount != 0:
        result = convert_usd_ars(amount)
        await ctx.send(f"**{amount}** USD son **{result}** ARS.")
    else:
        await ctx.send(f"""
----------
**!to_ars __amount__**
----------
"""
)


@bot.command()
async def say_hello(ctx):
    print("Command received")
    await ctx.send("Hola Mundo!")

@bot.command()
async def dolar(ctx):
    print("Command received")
    await ctx.send(f"El dolar blue esta\nCompra: {get_dollar_price('compra')}\nVenta: {get_dollar_price('venta')}")

# Run the bot with your bot token
bot.run("MTE2ODMxNDg4NjAzNjY1MjIxMg.G6VtGN.IWqLbHhABFIRm2Gzo13zew9idbdy_R0ktJPnf0")
