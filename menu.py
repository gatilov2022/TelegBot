from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
main_menu = ReplyKeyboardMarkup(resize_keyboard=True,
                                keyboard=[
                               [
                                   KeyboardButton(text="Рандомное фото📷"),
                                   KeyboardButton(text="Рандомная гифка🌅")
                               ]
                            ]
)