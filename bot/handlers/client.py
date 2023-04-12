from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
import json
from aiogram.dispatcher.filters.state import State, StatesGroup
import aiogram 
from create_bot import bot 

async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет 👋\n'
                        'Я бот, который позволяет вам пройти тест MBTI.\n'
                        'Пришлите мне /тест, и начнем проходить тест прямо сейчас!\n'
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
    
with open("./QandA/questions.json", "r") as f:
    questions = json.load(f)

question_index = 0

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


async def question(message: aiogram.types.Message, state: FSMContext):
    if message.text in [answer for question in questions for answer in question["answer"]]:
        global question_index
        question_index += 1
        await message.answer(text = "Вопрос №" + str(question_index + 1) + ":")

        # Проверяем, есть ли еще вопросы в списке
        if question_index < len(questions):
            # Получаем следующий вопрос из списка по индексу
            question = questions[question_index]

            keyboard = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
            for answer in range(len(question["answer"])):
                keyboard.add(aiogram.types.KeyboardButton(question["answer"][answer]))

            await message.answer(question["question"], reply_markup=keyboard)
            await Test.question.set()

        else:
            await message.answer("Тест закончен! Спасибо за участие!", reply_markup=aiogram.types.ReplyKeyboardRemove())
            await state.finish()

    elif message.text.lower() == "stop" or message.text.lower() == "стоп" or message.text.lower() == "прекратить" or message.text.lower() == "end":
            await message.answer("Тестирование прервано.", reply_markup=aiogram.types.ReplyKeyboardRemove())
            await state.finish()
    else:
        await message.answer("Пожалуйста, выберите один из вариантов ответа на клавиатуре.")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'начать', 'старт', 'начнём'])
    dp.register_message_handler(help_message, commands=['help', 'помощь'])
    dp.register_message_handler(test, commands=['test', 'тест'], state=None)
    dp.register_message_handler(ready, state = Test.ready)
    dp.register_message_handler(question, state = Test.question)
