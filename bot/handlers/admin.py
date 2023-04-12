from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


from configure import CREATOR_CHAT_ID
from create_bot import  bot 



class Problemka(StatesGroup):
    access = State() 
    problem = State()
# Отправляем сообщение создателю бота
async def command_problem(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Ты действительно хочешь отправить сообщение о проблеме? \nОтветьте \"да\" или \"нет\".')
    await state.set_state("access")

async def y_or_no_problem(message: types.Message, state: FSMContext):
    if message.text.lower() == "да" or message.text.lower() == "yes":
        await bot.send_message(message.from_user.id, "Опиши свою проблему, а я оправлю запрос создателю, в ближайшее время он с тобой свяжется.")
        await state.set_state("problem")
    elif message.text.lower() == "нет" or message.text.lower() == "no":
        await bot.send_message(message.from_user.id, "Как хорошо, что ты разобрался в своей проблеме!")
        await state.finish()

    else:
        await message.answer("Пожалуйста, ответьте \"да\" или \"нет\".")

async def problem_send(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await bot.send_message(chat_id=CREATOR_CHAT_ID, text=f"Пользователь {user_id} написал:\n{message.text}")
    await state.finish()



def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(command_problem, commands=['problem', 'проблема'])
    dp.register_message_handler(y_or_no_problem, state="access")
    dp.register_message_handler(problem_send, state="problem")