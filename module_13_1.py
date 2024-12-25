import asyncio

ball = 5
async def start_strongman(name, power):
    
    print(f'Силач {name} начал соревнования.')

    #Начало цикла соревнований
    for i in range(5):
        #поднятие шаров от 1 до 5
        await asyncio.sleep(ball / power)
        print(f'Силач {name} поднял шар {i+1}.')

    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3
    #«await» чтобы программа не завершалась, пока задачи не отработают

asyncio.run(start_tournament())
#«start_tournament» запускаем через «asyncio.run» для запуска асинхронного потока