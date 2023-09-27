from aiogram import types, Dispatcher
# from create_bot import dp
import string, json

#@dp.message_handler()
async def cenz_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
    .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Не матерись!')
        await message.delete()

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(cenz_send)