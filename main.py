import asyncio

from aiogram import Bot, Dispatcher, executor
from config import TOKEN_BOT
id_use_dirt = {}
len_id_use = 0
loop = asyncio.new_event_loop()
bot = Bot(TOKEN_BOT, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)
chek = {}

if __name__ == "__main__":
    from handlers import dp, send_to_admin, close_bot
    executor.start_polling(dp, on_startup=send_to_admin , on_shutdown= close_bot)
