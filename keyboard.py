from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

notif = 'Выделить всех пользователей'
roll = 'За ролить'
site = 'Сайт'
buy = 'Поддержать разработчика'
error = 'Сообщить об ошибке'
site_blur_but = InlineKeyboardButton('White-prince', url="https://white-prince.github.io/Homepage/")
error_blur_but = InlineKeyboardButton('Сообщить об ошибке', url="https://t.me/white_prince_0")

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).row(notif, roll).add(site).row(buy, error)
kb_site = InlineKeyboardMarkup().add(site_blur_but)
kb_error = InlineKeyboardMarkup().add(error_blur_but)
kb_close = types.ReplyKeyboardRemove()

