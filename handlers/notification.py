import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot

# 719370351


async def standup():
    ADMIN_ID = "719370351"
    await bot.send_message(
        chat_id=ADMIN_ID,
        text='Не забудь написать стендап'
    )


async def scheduler():
    aioschedule.every().days.at("11:41").do(standup)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2) 
