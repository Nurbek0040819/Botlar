import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import BotCommand

from config import BOT_TOKEN
from handlers.comman_handlers import command_router
from handlers.massage_handler import massage_router

async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
    await bot.set_my_commands(
        commands = [
            BotCommand(command="start", description="Start/boshlash bot"),
            BotCommand(command="help", description="sizga qanday yordam kerak bot"),
            BotCommand(command="new", description="new yangilik")
                    ]

    )
    dp = Dispatcher()
    dp.include_routers(command_router, massage_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")