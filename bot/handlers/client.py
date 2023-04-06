from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
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
    
# with open('./QandA/questions.json', 'r') as file:
#     questions = json.load(file)
class Test(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()

with open('./QandA/questions.json', 'r') as f:
    questions = json.load(f)

# @dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    """
    Conversation's entry point
    """
    # Set state
    await Test.q1.set()

    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_markup.add("Да", "Нет")

    await message.answer("Пройдем тест MBTI? (Да/Нет)", reply_markup=keyboard_markup)

# @dp.message_handler(state=Test.q1)
async def answer_q1(message: types.Message, state: FSMContext):
    """
    Process answer for question 1
    """
    async with state.proxy() as data:
        data['q1'] = message.text

        keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard_markup.add(questions[0]['answer'][0], questions[0]['answer'][1])

        await Test.next()
        await message.answer(questions[0]['question'], reply_markup=keyboard_markup)

# @dp.message_handler(state=Test.q2)
async def answer_q2(message: types.Message, state: FSMContext):
    """
    Process answer for question 2
    """
    async with state.proxy() as data:
        data['q2'] = message.text

        keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard_markup.add(questions[1]['answer'][0], questions[1]['answer'][1])

        await Test.next()
        await message.answer(questions[1]['question'], reply_markup=keyboard_markup)

# @dp.message_handler(state=Test.q3)
async def answer_q3(message: types.Message, state: FSMContext):
    """
    Process answer for question 3
    """
    async with state.proxy() as data:
        data['q3'] = message.text

        keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard_markup.add(questions[2]['answer'][0], questions[2]['answer'][1])

        await Test.next()
        await message.answer(questions[2]['question'], reply_markup=keyboard_markup)

# @dp.message_handler(state=Test.q4)
async def answer_q4(message: types.Message, state: FSMContext):
    """
    Process answer for question 4
    """
    async with state.proxy() as data:
        data['q4'] = message.text

        keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard_markup.add(questions[3]['answer'][0], questions[3]['answer'][1])

        await Test.next()
        await message.answer(questions[3]['question'], reply_markup=keyboard_markup)


# class Mydialog(StatesGroup):
#     YorN = State()
#     answer1 = State()
#     Q2 = State()



# # async def test_state(message: types.Message, state: FSMContext):
# #     msg = message.text
# #     if msg.lower() == "да" or msg.lower() == "согласен" or msg.lower() == "согласна" or msg.lower() == "yes":
# #         async for i in async_generator():            
# #             q = questions[i]['question']
# #             # print(q)
# #             await bot.send_message(message.from_user.id, f'Вопрос номер {i + 1}:\n'
# #                                                          f'{q}', reply_markup=kb_client)

# async def test_message(message: types.Message):
#     await bot.send_message(message.from_user.id, 'Начнём проходить наш тест?\nОтправьте "Да", если вы готовы.')

# async def enter_test(message: types.Message, state: FSMContext):
#     msg = message.text
#     if msg.lower() == "да" or msg.lower() == "согласен" or msg.lower() == "согласна" or msg.lower() == "yes":
#         await message.answer("Вы начали тестирование.")
#         await Mydialog.YorN.set()

                             
# async def sim():
#     async def async_generator():
#         for i in range(len(questions)):
#             yield i

#     async for j in async_generator():
#         async def ques(message: types.Message, state: FSMContext):
#             q = questions[j]['question']
#             await bot.send_message(f"Вопрос №{j}:\n"
#                                     f"{q}", reply_markup=kb_client[j])
#             answer = message.text
#             await state.update_data(
#                 {"answer1": answer}
#                     )
#         async def 

# async def enter_test(message: types.Message):
    # msg = message.text
    # if msg.lower() == "да" or msg.lower() == "согласен" or msg.lower() == "согласна" or msg.lower() == "yes":
    #     await message.answer("Вы начали тестирование.\n"
    #                         f"Вопрос №{async_generator(questions)}. \n\n"
    #                         "Вы часто занимаетесь бессмысленными делами "
    #                         "(бесцельно блуждаете по интернету, клацаете пультом телевизора, просто смотрите в потолок)?")
    #     await Mydialog.Q1.set()

# async def answer_q2(message: types.Message, state: FSMContext):
#     data = await state.get_data()
#     answer1 = data.get("answer1")
#     answer2 = message.text
#     await message.answer("Спасибо за ваши ответы!")
#     await state.finish()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'начать', 'старт', 'начнём'])
    dp.register_message_handler(command_problem, commands=['problem', 'проблема'])
    dp.register_message_handler(help_message, commands=['help', 'помощь'])
    dp.register_message_handler(problem_state, state="problem")
    dp.register_message_handler(cmd_start, commands=['test', 'тест'])
    dp.register_message_handler(answer_q1, state=Test.q1)
    dp.register_message_handler(answer_q2, state=Test.q2)
    dp.register_message_handler(answer_q3, state=Test.q3)
    dp.register_message_handler(answer_q4, state=Test.q4)
