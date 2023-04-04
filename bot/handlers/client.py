from aiogram import Dispatcher, types
from create_bot import dp, bot 
from keyboards import kb_client

async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Принял запрос start', reply_markup=kb_client)
    except:
        await message.reply('Общайтесь в ЛС: \nt.me/Myers_Briggs_Typology_bot')

async def command_second(message: types.Message):
    await bot.send_message(message.from_user.id, 'получил команду номер 2')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help', 'помощь', 'начать', 'старт', 'начнём'])
    dp.register_message_handler(command_second, commands=['second'])
