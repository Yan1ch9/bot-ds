import discord
from discord.ext import commands
import random
import os
import requests
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def info(ctx):
    await ctx.send(f'Привет! Я бот для помощи в сортировке мусора \n 1) /rubbish (название продукта) - вы пишите отход, а бот выдает вам информацию, как и куда его сортировать.\n 2) /image - выдает рандомную фотограцию по загрязнению на нашей планете!')

a = ['Овощи','фрукты', 'бакалея', 'выпечка', 'мясо', 'рыба', 'яйца', 'соусы', 'полуфабрикаты', 'молоко']

@bot.command()
async def rubbish(ctx, b):
    if b in a:
        await ctx.send(f'Данный продукт надо сортировать!')
    else:
        await ctx.send(f'Этот продукт сортировать нельзя!')
    print(b)

bot.run()
