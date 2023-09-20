from aiogram import types, Dispatcher
from create_bot import bot
from keyboards.client_key import kb_client


# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет! \nЧто хочешь узнать о какаошной?', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/crekdoo_bot')

# @dp.message_handler(commands=['Режим_работы'])


async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Круглосуточно')

# @dp.message_handler(commands=['Адрес'])


async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Чебуречная, 44')

'''#@dp.message_handler()
async def echo_send(message: types.Message):
    if message.reply(message.text):

        await message.answer('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/crekdoo_bot')'''

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Адрес'])

    #  dp.register_message_handler(echo_send)
