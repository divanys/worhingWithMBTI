import re
from aiogram import types, Dispatcher

def check_swear_word(text):
    # Паттерн для проверки на мат
    pattern = re.compile(r"\b(ху[ийяеё]|еба[нтуьвш]|бля[дть]|пизд[еуао]|ёб[аыу])\w*\b", re.IGNORECASE)
    match = re.search(pattern, text)
    # Если найдено совпадение, то это мат
    if match:
        return True
    else:
        return False

async def hello_in_other(message: types.Message):
    if check_swear_word(message.text):
        await message.reply("Вы использовали матерные слова!")
        await message.delete()
    else:
        await message.reply('Хэй! нажми команду /help.\n' 
                            'Там тебе откроются все команды, которыми я обладаю.\n' 
                            'И не пиши глупостей!')

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(hello_in_other)
