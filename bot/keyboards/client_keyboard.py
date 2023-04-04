from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

but1 = KeyboardButton('/start')
but2 = KeyboardButton('/second')
but3 = KeyboardButton('/key3')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(but1).insert(but2).add(but3)