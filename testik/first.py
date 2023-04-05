import json

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Load JSON data
with open('worhingWithMBTI/testik/data.json', 'r') as f:
    data = json.load(f)

# Create buttons
buttons = []
for item in data:
    button = InlineKeyboardButton(text=item['answer'])
    buttons.append(button)

# Create keyboard
keyboard = InlineKeyboardMarkup(row_width=1)
print(keyboard.add(*buttons))