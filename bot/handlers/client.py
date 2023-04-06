from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
import json
from aiogram.dispatcher.filters.state import State, StatesGroup

from configure import CREATOR_CHAT_ID
from create_bot import dp, bot 
from keyboards import kb_client

async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Hello 👋\n'
                        'I`m a bot that allows you to take the test MBTI.\n'
                        'Send me the /test and let`s start taking it!\n'
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
    
class Test(StatesGroup):

    for i in range(0, 70):
        exec(f"q{i} = State()")

with open('./QandA/questions.json', 'r') as f:
    questions = json.load(f)

async def cmd_start(message: types.Message):
    """
    Conversation's entry point
    """
    # Set state
    await Test.q0.set()

    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_markup.add("Да", "Нет")

    await message.answer("Пройдем тест MBTI? (Да/Нет)", reply_markup=keyboard_markup)



for i in range(0, 70):
    exec(f"async def answer_q{i}(message: types.Message, state: FSMContext):\n    async with state.proxy() as data:\n        data['q{i}'] = message.text\n        keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)\n        keyboard_markup.add(questions[{i}]['answer'][0], questions[{i}]['answer'][1])\n\n        if i == 70:\n            await Test.next()\n            await state.finish()\n            await message.answer('Спасибо за прохождение теста!')\n        else:\n            await Test.next()\n            await message.answer(f'Вопрос №{i + 1}: {questions[i]['question']}', reply_markup=keyboard_markup)")



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'начать', 'старт', 'начнём'])
    dp.register_message_handler(command_problem, commands=['problem', 'проблема'])
    dp.register_message_handler(help_message, commands=['help', 'помощь'])
    dp.register_message_handler(problem_state, state="problem")
    dp.register_message_handler(cmd_start, commands=['test', 'тест'])
    for i in range(0, 70):
        exec(f"dp.register_message_handler(answer_q{i}, state=Test.q{i})")
