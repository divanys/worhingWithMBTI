from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
import json
from aiogram.dispatcher.filters.state import State, StatesGroup
import aiogram 
import asyncio
import re

from WhoAreYou import who_are_you
from create_bot import bot 
from . import createDB

db = createDB.Database()
db.create_table_user()
db.create_table_results()

async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет 👋\n'
                        'Я бот, который позволяет вам пройти тест MBTI.\n'
                        'Пришлите мне /test, и начнем проходить тест прямо сейчас!\n'
                        'Или пришлите мне команду /help, если у вас возникла проблема или вы забыли команды.')
        await asyncio.sleep(0.2)
        
    except:
        await message.reply('Общайтесь в ЛС:\n'
                            't.me/Myers_Briggs_Typology_bot')


async def help_message(message: types.Message):
    await message.reply("Перечень команд для твоей помощи:\n"
                        "   /start - Начало бота. Приветствие. \n"
                        "   /help - помощь по командам. \n"
                        "   /problem - написать о проблеме создателю.\n"
                        "   /test - начало тестирования.")
    await asyncio.sleep(0.2)

with open("./QandA/questions.json", "r") as f:
    questions = json.load(f)

# result_test_text, result_test = [], []
class Test(StatesGroup):
    ready = State() # waiting for user's readiness
    question = State() # waiting for user's answer


async def test(message: aiogram.types.Message):
    await message.answer("Вы готовы пройти тест? Ответьте \"да\" или \"нет\".\nЕсли в процессе теста вы захотите его прекратить, отправьте \"стоп\".")
    await Test.ready.set()
    await asyncio.sleep(0.2)

# class 

async def ready(message: aiogram.types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_index'] = 0

    if message.text.lower() == "да" or message.text.lower() == "yes":
        async with state.proxy() as data:
            question = questions[data['question_index']]
            keyboard = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
            for answer in range(len(question["answer"])):
                keyboard.add(aiogram.types.KeyboardButton(question["answer"][answer]))
            await message.answer("Вопрос №1:")
            await message.answer(question["question"], reply_markup=keyboard)
            data['question_index'] += 1
        await Test.question.set()
    elif message.text.lower() == "нет" or message.text.lower() == "no":
        await message.answer("Тестирование прервано.", reply_markup=aiogram.types.ReplyKeyboardRemove())
        await state.finish()
    else:
        await message.answer("Пожалуйста, ответьте \"да\" или \"нет\".")
        await asyncio.sleep(0.2)
class Date(StatesGroup):
    surname = State()
    name = State()
    email = State() 
    registered = State()

# lst_data_user = []
with open("./QandA/personalType.json", "r") as f:
    personal_type = json.load(f)

db.create_table_answers()

async def question(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text in [answer for question in questions for answer in question["answer"]]:
            if data['question_index'] < len(questions):
                
                question = questions[data['question_index']]
                db.insert_answers(message.from_user.id, data['question_index'], 
                                  questions[data['question_index'] - 1]["question"], message.text)
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                for answer in range(len(question["answer"])):
                    keyboard.add(types.KeyboardButton(question["answer"][answer]))
                await message.answer(f"Вопрос №{data['question_index'] + 1}:")
                await message.answer(question["question"], reply_markup=keyboard)
                data['question_index'] += 1
                print(data['question_index'], data['question_index'])
                
            else:
                print(data['question_index'])
                await state.finish()
                # db.insert_user_id(message.from_user.id)
                db.insert_answers(message.from_user.id, data['question_index'], 
                                  questions[data['question_index'] - 1]["question"], message.text)
                for answer in range(len(questions)):
                    if db.select_answers_answer(message.from_user.id, answer + 1)[0][0] == questions[answer]["answer"][0]:
                        db.insert_answers_o_or_z(message.from_user.id, answer + 1, 1)
                    else:
                        db.insert_answers_o_or_z(message.from_user.id, answer + 1, 0)
                db.insert_user_result(message.from_user.id, who_are_you())
                await message.answer("Краткие результаты вашего теста:\n"
                                    "Ваш тип личности: "
                                    "; \nяркость выражения вашего типа: " + "/70.\n" +
                                    "Для получения полного результата теста, вам необходимо зарегистрироваться.\nПожалуйста, введите свою фамилию.")
                await Date.surname.set()
                lst_data_user.append(who_are_you(result_test)[0][0])
                lst_data_user.append(who_are_you(result_test)[0][1])
                result_test_text.clear()
                await asyncio.sleep(0.2)

        elif message.text.lower() == "stop" or message.text.lower() == "стоп" or message.text.lower() == "прекратить" or message.text.lower() == "end":
                await message.answer("Тестирование прервано.", reply_markup=aiogram.types.ReplyKeyboardRemove())
                await state.finish()
                result_test_text.clear()
                result_test.clear()
        else:
            await message.answer("Пожалуйста, выберите один из вариантов ответа на клавиатуре.")
        await asyncio.sleep(0.2)



async def send_surname(message: aiogram.types.Message):
    lst_data_user.append(message.text)
    await Date.name.set()
    await message.answer("Отправьте своё имя.")
    await asyncio.sleep(0.2)

async def send_name(message: aiogram.types.Message, state: FSMContext):
    lst_data_user.append(message.text)
    await Date.email.set()
    await message.answer("А теперь отправьте свою почту.")
    await asyncio.sleep(0.2)





def check_email(text):
    # Паттерн для проверки адреса электронной почты
    pattern = r"[a-zA-Z0-9._%±]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    match = re.search(pattern, text)
    # Если найдено совпадение, то это адрес электронной почты
    if match:
        return True
    else:
        return False
    
async def send_email(message: aiogram.types.Message, state: FSMContext):
    if not check_email(message.text):
        await message.answer("Адрес электронной почты не найден!\nПожалуйста, введите действительный адрес!")
        await asyncio.sleep(0.2)

    else:
        lst_data_user.append(message.text)
        if db.check_user_exists(message.from_user.id):
            await message.answer("Пользователь уже зарегистрирован.\nЖелаете изменить свои данные?\nОтветьте \"да\" или \"нет\"")
            await Date.registered.set()
        else:
            res = who_are_you(result_test)
            db.insert_user(*lst_data_user)
            db.insert_results(abbreviation=res[0][0], personality_type=personal_type[f"{res[0][0]}"],
                            e_i=res[1][0], s_n=res[1][1],
                            t_f=res[1][2], j_p=res[1][3],
                            total=res[0][1], id_user=message.from_user.id)
            lst_data_user.clear()
            result_test.clear()
            await asyncio.sleep(0.2)
            await message.answer("Спасибо за предоставленные данные!")
            await message.answer(f"Ваш тип личности - это {db.select_results(message.from_user.id)[-1][1]}.\n"
                                 f"По шкале E-I вы набрали баллов: {db.select_results(message.from_user.id)[-1][2]}\n"
                                 f"По шкале S-N вы набрали баллов: {db.select_results(message.from_user.id)[-1][3]}\n"
                                 f"По шкале T-F вы набрали баллов: {db.select_results(message.from_user.id)[-1][4]}\n"
                                 f"По шкале J-P вы набрали баллов: {db.select_results(message.from_user.id)[-1][5]}\n"
                                 "Сейчас я пришлю файл с более подробной информацией о вашем типе личности!.."
                                 )
            with open(f"./Keirsi/{db.select_results(message.from_user.id)[-1][0]}.pdf", 'rb') as file:
                await bot.send_document(message.from_user.id, file)
            await state.finish()
            


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
        await message.answer(f"Ваш тип личности - это {db.select_results(message.from_user.id)[-1][1]}.\n"
                                 f"По шкале E-I вы набрали баллов: {db.select_results(message.from_user.id)[-1][2]}\n"
                                 f"По шкале S-N вы набрали баллов: {db.select_results(message.from_user.id)[-1][3]}\n"
                                 f"По шкале T-F вы набрали баллов: {db.select_results(message.from_user.id)[-1][4]}\n"
                                 f"По шкале J-P вы набрали баллов: {db.select_results(message.from_user.id)[-1][5]}\n"
                                 "Сейчас я пришлю файл с более подробной информацией о вашем типе личности!.."
                                 )
        with open(f"./Keirsi/{db.select_results(message.from_user.id)[-1][0]}.pdf", 'rb') as file:
            await bot.send_document(message.from_user.id, file)
        await state.finish()
        await asyncio.sleep(0.2)

    elif  message.text.lower() == "нет" or message.text.lower() == "no":
        lst_data_user.clear()
        result_test.clear()
        await message.answer(f"Данные пользователя с id {message.from_user.id} остались неизменны.")
        await state.finish()
        await asyncio.sleep(0.2)

    else:
        await message.answer("Пожалуйста, ответьте \"да\" или \"нет\".")
        await asyncio.sleep(0.2)



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

