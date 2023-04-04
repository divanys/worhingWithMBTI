from aiogram import Bot 
from aiogram.dispatcher import Dispatcher
from configure import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
