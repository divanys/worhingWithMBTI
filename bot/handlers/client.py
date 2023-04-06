from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
import json

from configure import CREATOR_CHAT_ID
from create_bot import dp, bot 
from keyboards import kb_client

async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Hello 👋\n'
                        'I`m a bot that allows you to take the test MBTI.\n'
                        'Send me the /test and let`s start taking it!'
                        'Or send me the /help command if you have a problem or forgot the commands.')
    except:
        await message.reply('Общайтесь в ЛС:\n'
                            't.me/Myers_Briggs_Typology_bot')


# Отправляем сообщение создателю бота
async def command_problem(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Опиши свою проблему, а я оправлю запрос создателю, в ближайшее время он с тобой свяжется.')
    await state.set_state("problem")

async def problem_state(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await bot.send_message(chat_id=CREATOR_CHAT_ID, text=f"Пользователь {user_id} написал:\n{message.text}")
    await state.finish()


async def help_message(message: types.Message):
    await message.reply("Перечень команд для твоей помощи:\n"
                        "   /start - Начало бота. Приветствие. \n"
                        "   /help - помощь по командам. \n"
                        "   /problem - написать о проблеме создателю.")
    
with open('./QandA/questions.json', 'r') as file:
    questions = json.load(file)

async def test_message(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Начнём проходить наш тест?\nОтправьте "Да", если вы готовы.')
    await state.set_state("test")

async def some_async_generator():
    for i in range(len(questions)):
        yield i

# async def some_async_function():
#     async for i in some_async_generator():
#         print(i)

async def test_state(message: types.Message, state: FSMContext):
    msg = message.text
    if msg == "Да":
        async for i in some_async_generator():            
            q = i['question']
            # print(q)
            await bot.send_message(message.from_user.id, f'Вопрос номер {i + 1}:\n'
                                                            f'{q}', reply_markup=kb_client)
            await state.finish()



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'начать', 'старт', 'начнём'])
    dp.register_message_handler(command_problem, commands=['problem', 'проблема'])
    dp.register_message_handler(help_message, commands=['help', 'помощь'])
    dp.register_message_handler(problem_state, state="problem")
    dp.register_message_handler(test_message, commands=['test', 'тест'])
    dp.register_message_handler(test_state, state='test')
