import discord
import os
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
intents = discord.Intents.all()
command_prefix = '//'
TOKEN = os.getenv('ONGAKU_DEV')
bot = commands.Bot(command_prefix=command_prefix, intents=intents)



async def load_extensions():
    for cogfile in os.listdir('cogs'):
        if cogfile.endswith(".py"):
            await bot.load_extension(f"cogs.{cogfile[:-3]}")



async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

asyncio.run(main())