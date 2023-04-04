from aiogram import types, Dispatcher
from create_bot import dp 

async def command_in_other(message: types.Message):
    await message.reply('ne materites deti')


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(command_in_other)