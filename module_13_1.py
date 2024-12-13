import time
import asyncio
from asyncio import run


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for oto in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {oto} шар')
    print(f'Силач {name} закончил соревнования.')

async def main():
    print('Старт')
    first_start = asyncio.create_task(start_strongman('Pasha', 3))
    second_start = asyncio.create_task(start_strongman('Denis', 4))
    third_start = asyncio.create_task(start_strongman('Apollon', 5))
    await first_start
    await second_start
    await third_start
    print('Финал')


if __name__ == '__main__':
    asyncio.run(main())