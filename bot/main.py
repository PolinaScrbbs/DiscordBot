import discord
from discord.ext import commands
import config as cnfg

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def load_extensions():
    initial_extensions = ['handlers.commands', 'handlers.events']
    for extension in initial_extensions:
        await bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

async def main():
    await load_extensions()
    await bot.start(cnfg.KEY)

import asyncio
asyncio.run(main())