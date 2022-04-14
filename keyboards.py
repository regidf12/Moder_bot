from aiogram.types import *
from aiogram import types

button_hi = KeyboardButton('Привет!\n Спасибо за информацию')

grt_kb = ReplyKeyboardMarkup()
grt_kb.add(button_hi)

grt_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_hi)
# Кнопки для быстрого набора
hi = KeyboardButton('Привет!')
how = KeyboardButton('Как дела?')
wd = KeyboardButton('Что делаете?')
com = KeyboardButton('Зайдите пожалуйста в Discord')
buy = KeyboardButton('Пока!')
si = KeyboardButton("Sing up")
lo = KeyboardButton("Log in")

markup3 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(hi).add(how).add(wd).add(com).add(buy)

kbs = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
)
# Кнопки для панели админестратора
kbs.add(types.InlineKeyboardButton(text="Рассылка"))
kbs.add(types.InlineKeyboardButton(text="Добавить в ЧС"))
kbs.add(types.InlineKeyboardButton(text="Убрать из ЧС"))
kbs.add(types.InlineKeyboardButton(text="Статистика"))

krg = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(si).add(lo)

