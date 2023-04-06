from aiogram import types, Dispatcher
from create_bot import dp 

async def hello_in_other(message: types.Message):
    await message.reply('other'
                        )


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(hello_in_other)