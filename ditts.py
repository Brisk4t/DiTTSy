import discord
import os
from discord.ext import commands

intents = discord.Intents.all()
command_prefix = '//'
TOKEN = os.getenv('ONGAKU_DEV')
bot = commands.Bot(command_prefix=command_prefix, intents=intents)


for cogfile in os.listdir('cogs'):
    if cogfile.endswith(".py"):
        bot.load_extension("cogs."+ cogfile[:3])

bot.run(TOKEN)

