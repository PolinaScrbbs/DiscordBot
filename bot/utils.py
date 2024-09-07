import datetime
import discord

import config as cnfg
import enums as enm

async def get_today_weekday() -> str:
    today_weekday_number = datetime.datetime.today().date().weekday()

    day_mapping = {
        0: 'ПОНЕДЕЛЬНИК',
        1: 'ВТОРНИК',
        2: 'СРЕДА',
        3: 'ЧЕТВЕРГ',
        4: 'ПЯТНИЦА',
        5: 'СУББОТА',
        6: 'ВОСКРЕСЕНЬЕ'
    }

    mapped_day = day_mapping.get(today_weekday_number, 'ПОНЕДЕЛЬНИК')

    return mapped_day

async def channel_checking(ctx) -> bool:
    res = True
    if ctx.channel.id not in cnfg.ALLOWED_CHANNELS:
        embed = discord.Embed(description=enm.BotMessages.CHANNEL_NOT_ALLOWED.value, color=cnfg.EMBED_COLOR)
        
        embed.set_footer(
            text=f"Пожалуйста, используйте бота в разрешенных каналах.",
        )
        
        await ctx.send(embed=embed)
        res = False

    return res
    