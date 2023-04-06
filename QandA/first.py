import json
import asyncio


with open('./QandA/questions.json', 'r') as file:
    questions = json.load(file)

print(len(questions))


async def some_async_generator():
    for i in range(len(questions)):
        yield i

async def sim():
    async for i in some_async_generator():
        q = questions[i]['question']
        print(q)

asyncio.run(sim())
