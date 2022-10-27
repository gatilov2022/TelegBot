import giphypop

from main import bot, dp

from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ContentTypes, InlineKeyboardMarkup, InlineKeyboardButton
from config import admin_id
from menu import main_menu

g = giphypop.Giphy(api_key="qt9I33YkXf2Jrk8D8mC63ZjrqNAfI5uQ")



async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="я заработал")


async def close_bot(dp):
    await bot.send_message(chat_id=admin_id, text= "я упал")


@dp.message_handler(Command("start"))
async def start(message: Message):
    await message.answer(text="Этот бот умеет:")
    await message.answer(text="Присылать рандомные фото📷\nРандомные гифки🌅\nПолучать из геометки ссылку на прогноз погоды☔", reply_markup=main_menu)

@dp.message_handler(Text("Рандомная гифка🌅"))
async def gif_rand(message: Message):
    await message.answer(text=get_random_gif())

@dp.message_handler(Command("random_gif"))
async def gif_rand(message: Message):
    await message.answer(text=get_random_gif())

@dp.message_handler(Command("random_photo"))
async def photo_rand(message: Message):
    await message.answer_photo(photo=get_random_gif())

@dp.message_handler(Text("Рандомное фото📷"))
async def photo_rand(message: Message):
    await message.answer_photo(photo=get_random_gif())

@dp.message_handler(content_types=ContentTypes.LOCATION)
async def send(message: Message):
    loc = "https://yandex.ru/pogoda/details?lat=" + str(message.location.latitude) + "&lon=" + str(message.location.longitude)
    inline = InlineKeyboardMarkup()
    inline.add(InlineKeyboardButton('Жмяк', url=loc))
    await message.answer(text="Сайт с погодой", reply_markup=inline)

def get_random_gif():
    n = g.random_gif()
    return(n.get("url"))
