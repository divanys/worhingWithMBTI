# import json
# import asyncio


# with open('./QandA/questions.json', 'r') as file:
#     questions = json.load(file)

# print(len(questions))


# async def some_async_generator():
#     for i in range(len(questions)):
#         yield i

# async def sim():
#     async for i in some_async_generator():
#         q = questions[i]['question']
#         print(q)

# asyncio.run(sim())
#     # exec(f"async def answer_q{i}(message: types.Message, state: FSMContext):\n    async with state.proxy() as data:\n        data['q{i}'] = message.text\n        keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)\n        keyboard_markup.add(questions[{i}]['answer'][0], questions[{i}]['answer'][1])\n\n        if i == 70:\n            await Test.finish()\n            await message.answer('Спасибо за прохождение теста!')\n        else:\n            await Test.next()\n            await message.answer(questions[{i}]['question'], reply_markup=keyboard_markup)")
# # @dp.message_handler(state=Test.q1)
# # async def answer_q1(message: types.Message, state: FSMContext):
# #     """
# #     Process answer for question 1
# #     """
# #     async with state.proxy() as data:
# #         data['q1'] = message.text

# #         keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# #         keyboard_markup.add(questions[0]['answer'][0], questions[0]['answer'][1])

# #         await Test.next()
# #         await message.answer(questions[0]['question'], reply_markup=keyboard_markup)
# # @dp.message_handler(state=Test.q2)
# # async def answer_q2(message: types.Message, state: FSMContext):
# #     """
# #     Process answer for question 2
# #     """
# #     async with state.proxy() as data:
# #         data['q2'] = message.text

# #         keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# #         keyboard_markup.add(questions[1]['answer'][0], questions[1]['answer'][1])

# #         await Test.next()
# #         await message.answer(questions[1]['question'], reply_markup=keyboard_markup)

# # # @dp.message_handler(state=Test.q3)
# # async def answer_q3(message: types.Message, state: FSMContext):
# #     """
# #     Process answer for question 3
# #     """
# #     async with state.proxy() as data:
# #         data['q3'] = message.text

# #         keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# #         keyboard_markup.add(questions[2]['answer'][0], questions[2]['answer'][1])

# #         await Test.next()
# #         await message.answer(questions[2]['question'], reply_markup=keyboard_markup)

# # # @dp.message_handler(state=Test.q4)
# # async def answer_q4(message: types.Message, state: FSMContext):
# #     """
# #     Process answer for question 4
# #     """
# #     async with state.proxy() as data:
# #         data['q4'] = message.text

# #         keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# #         keyboard_markup.add(questions[3]['answer'][0], questions[3]['answer'][1])

# #         await Test.next()
# #         await message.answer(questions[3]['question'], reply_markup=keyboard_markup)


# # class Mydialog(StatesGroup):
# #     YorN = State()
# #     answer1 = State()
# #     Q2 = State()



# # # async def test_state(message: types.Message, state: FSMContext):
# # #     msg = message.text
# # #     if msg.lower() == "да" or msg.lower() == "согласен" or msg.lower() == "согласна" or msg.lower() == "yes":
# # #         async for i in async_generator():            
# # #             q = questions[i]['question']
# # #             # print(q)
# # #             await bot.send_message(message.from_user.id, f'Вопрос номер {i + 1}:\n'
# # #                                                          f'{q}', reply_markup=kb_client)

# # async def test_message(message: types.Message):
# #     await bot.send_message(message.from_user.id, 'Начнём проходить наш тест?\nОтправьте "Да", если вы готовы.')

# # async def enter_test(message: types.Message, state: FSMContext):
# #     msg = message.text
# #     if msg.lower() == "да" or msg.lower() == "согласен" or msg.lower() == "согласна" or msg.lower() == "yes":
# #         await message.answer("Вы начали тестирование.")
# #         await Mydialog.YorN.set()

                             
# # async def sim():
# #     async def async_generator():
# #         for i in range(len(questions)):
# #             yield i

# #     async for j in async_generator():
# #         async def ques(message: types.Message, state: FSMContext):
# #             q = questions[j]['question']
# #             await bot.send_message(f"Вопрос №{j}:\n"
# #                                     f"{q}", reply_markup=kb_client[j])
# #             answer = message.text
# #             await state.update_data(
# #                 {"answer1": answer}
# #                     )
# #         async def 

# # async def enter_test(message: types.Message):
#     # msg = message.text
#     # if msg.lower() == "да" or msg.lower() == "согласен" or msg.lower() == "согласна" or msg.lower() == "yes":
#     #     await message.answer("Вы начали тестирование.\n"
#     #                         f"Вопрос №{async_generator(questions)}. \n\n"
#     #                         "Вы часто занимаетесь бессмысленными делами "
#     #                         "(бесцельно блуждаете по интернету, клацаете пультом телевизора, просто смотрите в потолок)?")
#     #     await Mydialog.Q1.set()

# # async def answer_q2(message: types.Message, state: FSMContext):
# #     data = await state.get_data()
# #     answer1 = data.get("answer1")
# #     answer2 = message.text
# #     await message.answer("Спасибо за ваши ответы!")
# #     await state.finish()

# for i in range(70):
#   print(
#     f"async def answer_q{i}(message: types.Message, state: FSMContext):\n"
#     f"  async with state.proxy() as data:\n"
#     f"    data['q{i}'] = message.text\n"
#     f"  keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)\n"
#     f"  keyboard_markup.add(questions[{i}]['answer'][0]}, questions[{i}]['answer'][1])\n"
#     f"  await Test.next()\n"
#     f"  await message.answer('Вопрос №{str(i)}', questions[{i}]['question'], reply_markup=keyboard_markup)\n")
# if i == 70:\n            await Test.next()\n            await state.finish()\n            await message.answer('Спасибо за прохождение теста!')


for i in range(0, 70):
    print(f"async def answer_q{i}(message: types.Message, state: FSMContext):\n    async with state.proxy() as data:\n        data['q{i}'] = message.text\n        keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)\n        keyboard_markup.add(questions[{i}]['answer'][0], questions[{i}]['answer'][1])\n\n        await Test.next()\n        await message.answer(f'Вопрос №{i + 1}: ', questions[{i}][\"question\"], reply_markup=keyboard_markup)\n")
