import discord
from discord.ext import commands
import os, random
import requests


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć! Jestem botem, {bot.user}!')

@bot.command()
async def pomocy(ctx):
    await ctx.send(f'Komendy które możesz użyć: \n $hello - Bot się przywita \n $he - Easteregg \n $mem - Generacja mema (jest 7)')

@bot.command()
async def he(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    image_name = random.randint(1,7)
    with open(f'images/{image_name}.jpg', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)

bot.run("Twój discord Token")