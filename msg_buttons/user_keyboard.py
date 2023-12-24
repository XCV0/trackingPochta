from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types


kb_user_functions = ["Добавить трек номер", "Список моих посылок", "Удалить посылку"]


def generate_usermenu_kb():
    global kb_user_functions
    builder = ReplyKeyboardBuilder()
    for i in kb_user_functions:
        builder.add(types.KeyboardButton(text=i))
    builder.adjust(2)

    return builder.as_markup(resize_keyboard=True)
