import discord
from discord.ext import commands

import config as cnfg
import enums as enm
import utils as ut

class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='пары')
    async def schedule(self, ctx, param: str = None):
        await ctx.message.delete()
        if await ut.channel_checking(ctx):
            if param:
                if param.lower() == "все":
                    embed = discord.Embed(title=":calendar_spiral: \u200B **Расписание на всю неделю**\n", color=cnfg.EMBED_COLOR)
                    for day in enm.Schedule:
                        embed.add_field(name=f"\u200B\n**{day.name.capitalize()}**", value=day.value, inline=False)
                    await ctx.send(embed=embed)
                else:
                    try:
                        day_enum = enm.Schedule[param.upper()]
                        embed = discord.Embed(title=f":calendar_spiral: \u200B **Расписание на {day_enum.name.capitalize()}**\n", description=day_enum.value, color=cnfg.EMBED_COLOR)
                        await ctx.send(embed=embed)
                    except KeyError:
                        await ctx.send("Неправильный день недели! Введите день на русском: Понедельник, Вторник, и т.д.")
            else:
                mapped_day = await ut.get_today_weekday()
                try:
                    day_schedule = enm.Schedule[mapped_day]
                    embed = discord.Embed(title=f":calendar_spiral: \u200B **Расписание на {mapped_day.capitalize()}**\n", description=day_schedule.value, color=cnfg.EMBED_COLOR)
                    await ctx.send(embed=embed)
                except KeyError:
                    await ctx.send("Ошибка в расписании для сегодняшнего дня.")


    @commands.command(name='hit')
    async def hit(self, ctx, member: discord.Member):
        await ctx.message.delete()
        await ctx.send(f'{ctx.author.mention} ударил {member.mention}!')

    @commands.command(name='kiss')
    async def kiss(self, ctx, member: discord.Member):
        await ctx.message.delete()
        await ctx.send(f'{ctx.author.mention} поцеловал {member.mention}!')


async def setup(bot):
    await bot.add_cog(GeneralCommands(bot))