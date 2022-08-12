import logging
import re
import random

from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN, SBTOKEN
from messages import MESSAGE
from keyboard import kb_menu, kb_site, kb_error, kb_close

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

PRICE = types.LabeledPrice(label='Поддержать разработчика', amount=10000)


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await bot.send_message(message.chat.id, 'Здравствуйте, ' + str(message.from_user.first_name) + MESSAGE['start'],
                           reply_markup=kb_menu)


@dp.message_handler(commands=['help'])
async def help_cmd(message: types.Message):
    await bot.send_message(message.chat.id, MESSAGE['help'])


@dp.message_handler(commands=['menu'])
async def help_cmd(message: types.Message):
    await bot.send_message(message.chat.id, 'Меню', reply_markup=kb_menu)


@dp.message_handler()
async def menu(message: types.Message):
    if message.text == 'Выделить всех пользователей':
        await bot.send_message(message.chat.id, MESSAGE['all_u'], reply_markup=kb_close)
    elif message.text == 'За ролить':
        x = random.randint(1, 100)
        await bot.send_message(message.chat.id, str(x), reply_markup=kb_close)

    elif message.text == 'Сайт':
        await bot.send_message(message.chat.id, "На нашем сайте, вы можете оформить заказ, задать вопрос или получить "
                                                "больше информации о нас.", reply_markup=kb_site)
    elif message.text == 'Поддержать разработчика':
        await bot.send_message(message.chat.id, "В данный момент оплата Юкасса не поддерживает оплату telegram")
        await bot.send_message(message.chat.id, "Реквезиты для перевода:\n"
                                                "Tinkoff, ВТБ, Сбер: "
                                                "+7-925-413-56-61", reply_markup=kb_close)
    elif message.text == 'Сообщить об ошибке':
        await bot.send_message(message.chat.id, "Заметили ошибку? Cообщите о ней разработчику <3",
                               reply_markup=kb_error)
    elif message.text == 'Убрать клавиатуру':
        await bot.send_message(message.chat.id, "Спасибо, что воспользовались клавиатурой <3",
                               reply_markup=kb_close)
    else:
        for i in MESSAGE['pattern']:
            match = re.search(i, str(message))
            if match:
                await message.delete()


@dp.message_handler()
async def process_buy_command(message: types.Message):
    await bot.send_invoice(
        message.chat.id,
        title='Поддержите разработчика',
        description='Я тоже хочу кушать',
        provider_token=SBTOKEN,
        currency='rub',
        photo_url='https://i.pinimg.com/736x/8b/08/92/8b08924c7e10c38d4a9c487a15c428d3.jpg',
        photo_height=512,
        photo_width=512,
        photo_size=512,
        is_flexible=False,
        prices=[PRICE],
        start_parameter='support_developer',
        payload='some-invoice-payload-for-our-internal-use'
    )


if __name__ == '__main__':
    executor.start_polling(dp)
