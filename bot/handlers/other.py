from aiogram import types, Dispatcher
from create_bot import dp 

async def hello_in_other(message: types.Message):
    await message.reply('Hello 👋\n'
                        'I`m a bot that allows you to take the test MBTI.\n'
                        'Please send me the /start command and we will start working!\n'
                        'Or send me the /help command if you have a problem or forgot the commands.'
                        )


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(hello_in_other)