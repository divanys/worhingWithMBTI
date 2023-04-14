from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
import json
from aiogram.dispatcher.filters.state import State, StatesGroup
import aiogram 
import asyncio

from WhoAreYou import who_are_you
from create_bot import bot 
from . import createDB

async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет 👋\n'
                        'Я бот, который позволяет вам пройти тест MBTI.\n'
                        'Пришлите мне /test, и начнем проходить тест прямо сейчас!\n'
                        'Или пришлите мне команду /help, если у вас возникла проблема или вы забыли команды.')
    except:
        await message.reply('Общайтесь в ЛС:\n'
                            't.me/Myers_Briggs_Typology_bot')


async def help_message(message: types.Message):
    await message.reply("Перечень команд для твоей помощи:\n"
                        "   /start - Начало бота. Приветствие. \n"
                        "   /help - помощь по командам. \n"
                        "   /problem - написать о проблеме создателю.\n"
                        "   /test - начало тестирования.")
    
with open("/home/divan/гетБрейнсИТолькоУдалиЯТебzУдалюСЛицаЗемли/forJobasyncpython/workingWithMBTI/QandA/questions.json", "r") as f:
    questions = json.load(f)

question_index = 0
result_test_text, result_test = [], []
class Test(StatesGroup):
    ready = State() # waiting for user's readiness
    question = State() # waiting for user's answer


async def test(message: aiogram.types.Message):
    await message.answer("Вы готовы пройти тест? Ответьте \"да\" или \"нет\".\nЕсли в процессе теста вы захотите его прекратить, отправьте \"стоп\".")
    await Test.ready.set()

async def ready(message: aiogram.types.Message, state: FSMContext):

    if message.text.lower() == "да" or message.text.lower() == "yes":
        question = questions[question_index]
        keyboard = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)

        for answer in range(len(question["answer"])):
            keyboard.add(aiogram.types.KeyboardButton(question["answer"][answer]))

        await message.answer("Вопрос №1:")
        await message.answer(question["question"], reply_markup=keyboard)
        await Test.question.set()

    elif message.text.lower() == "нет" or message.text.lower() == "no":
        await message.answer("Тестирование прервано.", reply_markup=aiogram.types.ReplyKeyboardRemove())
        await state.finish()

    else:
        await message.answer("Пожалуйста, ответьте \"да\" или \"нет\".")

class Date(StatesGroup):
    surname = State()
    name = State()
    email = State() 
    registered = State()

lst_data_user = []


async def question(message: aiogram.types.Message, state: FSMContext):
    if message.text in [answer for question in questions for answer in question["answer"]]:
        global question_index
        question_index += 1
        
        # Проверяем, есть ли еще вопросы в списке
        if question_index < len(questions):
           
            # Получаем следующий вопрос из списка по индексу
            question = questions[question_index]
            await message.answer(text = "Вопрос №" + str(question_index + 1) + ":")
            keyboard = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
            for answer in range(len(question["answer"])):
                keyboard.add(aiogram.types.KeyboardButton(question["answer"][answer]))
            
            await message.answer(question["question"], reply_markup=keyboard)
            await Test.question.set()
            result_test_text.append(message.text)
            
        else:
            await message.answer("Тест закончен! Спасибо за участие!", reply_markup=aiogram.types.ReplyKeyboardRemove())
            lst_data_user.append(message.from_user.id)
            result_test_text.append(message.text)

            for answer in range(len(questions)):
                if result_test_text[answer] == questions[answer]["answer"][0]:
                    result_test.append(1)
                else:
                    result_test.append(0)

            await state.finish()

            await message.answer("Результаты вашего теста:\n" + str(who_are_you(result_test)) + "\nПожалуйста, введите свою фамилию.")
            await Date.surname.set()
            lst_data_user.append(who_are_you(result_test)[0][0])
            lst_data_user.append(who_are_you(result_test)[0][1])
            question_index = 0
            result_test_text.clear()

    elif message.text.lower() == "stop" or message.text.lower() == "стоп" or message.text.lower() == "прекратить" or message.text.lower() == "end":
            await message.answer("Тестирование прервано.", reply_markup=aiogram.types.ReplyKeyboardRemove())
            await state.finish()
            question_index = 0
            result_test_text.clear()
            result_test.clear()
            
    else:
        await message.answer("Пожалуйста, выберите один из вариантов ответа на клавиатуре.")



async def send_surname(message: aiogram.types.Message):
    lst_data_user.append(message.text)
    await Date.name.set()
    await message.answer("Отправьте своё имя.")

async def send_name(message: aiogram.types.Message, state: FSMContext):
    lst_data_user.append(message.text)
    await Date.email.set()
    await message.answer("А теперь отправьте свою почту.")

db = createDB.Database()
db.create_table_user()
db.create_table_results()

with open("/home/divan/гетБрейнсИТолькоУдалиЯТебzУдалюСЛицаЗемли/forJobasyncpython/workingWithMBTI/QandA/personalType.json", "r") as f:
    personal_type = json.load(f)

async def send_email(message: aiogram.types.Message, state: FSMContext):
    lst_data_user.append(message.text)
    print(lst_data_user)
    if db.check_user_exists(message.from_user.id):
        await message.answer("Пользователь уже зарегистрирован.\nЖелаете изменить свои данные?")
        await Date.registered.set()
    else:
        await message.answer("Спасибо за предоставленные данные!")
        await state.finish()
        db.insert_user(*lst_data_user)
        db.insert_results(abbreviation=who_are_you(result_test)[0][0], personality_type=personal_type[f"{who_are_you(result_test)[0][0]}"],
                          e_i=who_are_you(result_test)[1][0], s_n=who_are_you(result_test)[1][1],
                          t_f=who_are_you(result_test)[1][2], j_p=who_are_you(result_test)[1][3],
                          total=who_are_you(result_test)[0][1], id_user=message.from_user.id)
        lst_data_user.clear()
        result_test.clear()


async def send_registered(message: aiogram.types.Message, state: FSMContext):
    if (message.text.lower() == "yes" or message.text.lower() == "да"):
        db.update_user(*lst_data_user)
        db.insert_results(abbreviation=who_are_you(result_test)[0][0], personality_type=personal_type[f"{who_are_you(result_test)[0][0]}"],
                          e_i=who_are_you(result_test)[1][0], s_n=who_are_you(result_test)[1][1],
                          t_f=who_are_you(result_test)[1][2], j_p=who_are_you(result_test)[1][3],
                          total=who_are_you(result_test)[0][1], id_user=message.from_user.id)
        lst_data_user.clear()
        result_test.clear()
        await message.answer(f"Данные пользователя с id {message.from_user.id} обновлены!")
    elif  message.text.lower() == "нет" or message.text.lower() == "no":
        lst_data_user.clear()
        result_test.clear()

        await message.answer(f"Данные пользователя с id {message.from_user.id} остались неизменны.")
    await state.finish()



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'начать', 'старт', 'начнём'])
    dp.register_message_handler(help_message, commands=['help', 'помощь'])
    dp.register_message_handler(test, commands=['test', 'тест'], state=None)
    dp.register_message_handler(ready, state = Test.ready)
    dp.register_message_handler(question, state = Test.question)
    dp.register_message_handler(send_surname, state = Date.surname)
    dp.register_message_handler(send_name, state = Date.name)
    dp.register_message_handler(send_email, state = Date.email)
    dp.register_message_handler(send_registered, state = Date.registered)

