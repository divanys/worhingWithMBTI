import json
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

with open('worhingWithMBTI/QandA/questions.json', 'r') as file:
    questions = json.load(file)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
for question in questions:
    q = question['question']
    a1 = question['answer'][0]
    a2 = question['answer'][1]
    kb_client.add(KeyboardButton(a1), KeyboardButton(a2))