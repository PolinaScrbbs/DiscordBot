import discord
from discord.ext import commands

import config as cnfg

class EventHandlers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(cnfg.WELCOME_CHANNEL_ID)
        if channel:
            await channel.send(f'Привет, {member.mention}! Добро пожаловать на сервер!')

async def setup(bot):
    await bot.add_cog(EventHandlers(bot))