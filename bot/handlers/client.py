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


async def help_message(message: types.Message):
    await message.reply("Перечень команд для твоей помощи...\n"
                        "/start - Начало бота. Приветствие. 1️⃣\n"
                        "/help - помощь по командам. 2️⃣\n"
                        )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'начать', 'старт', 'начнём'])
    dp.register_message_handler(command_second, commands=['second'])
    dp.register_message_handler(help_message, commands=['help', 'помощь'])
