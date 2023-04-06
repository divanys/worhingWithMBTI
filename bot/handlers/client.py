from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from configure import CREATOR_CHAT_ID
from create_bot import dp, bot 
from keyboards import kb_client

async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Hello 👋\n'
                        'I`m a bot that allows you to take the test MBTI.\n'
                        'Or send me the /help command if you have a problem or forgot the commands.', reply_markup=kb_client)
    except:
        await message.reply('Общайтесь в ЛС:\n'
                            't.me/Myers_Briggs_Typology_bot')

async def command_problem(message: types.Message, state: FSMContext):
    # Отправляем сообщение создателю бота
    await bot.send_message(message.from_user.id, 'Опиши свою проблему, а я оправлю запрос создателю, в ближайшее время он с тобой свяжется.')
    await state.set_state("problem")

async def problem_state(message: types.Message, state: FSMContext):
    # Получаем id пользователя из состояния
    user_id = message.from_user.id

    # Отправляем сообщение создателю бота с текстом проблемы и id пользователя
    await bot.send_message(chat_id=CREATOR_CHAT_ID, text=f"Пользователь {user_id} написал:\n{message.text}")

    # Сбрасываем состояние
    await state.finish()

async def help_message(message: types.Message):
    await message.reply("Перечень команд для твоей помощи:\n"
                        "   /start - Начало бота. Приветствие. \n"
                        "   /help - помощь по командам. \n"
                        "   /problem - написать о проблеме создателю.")

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'начать', 'старт', 'начнём'])
    dp.register_message_handler(command_problem, commands=['problem', 'проблема'])
    dp.register_message_handler(help_message, commands=['help', 'помощь'])
    dp.register_message_handler(problem_state, state="problem")