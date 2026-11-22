#სავარჯიშო 1

import asyncio
import time


async def deliver(order, seconds):
    print(f"{order}: გაიგზავნა")
    await asyncio.sleep(seconds)
    print(f"{order}: მიტანილია")


orders = [("შეკვეთა #1", 1.0), ("შეკვეთა #2", 1.5), ("შეკვეთა #3", 2.0)]


async def main():

    start = time.perf_counter()
    for order, seconds in orders:
        await deliver(order, seconds)
    sequential_time = time.perf_counter() - start
    print(f"ზედიზედ: {sequential_time:.1f} წმ")

    start = time.perf_counter()
    await asyncio.gather(*(deliver(o, s) for o, s in orders))
    concurrent_time = time.perf_counter() - start
    print(f"ერთდროულად: {concurrent_time:.1f} წმ")

    print(f"დაჩქარება: {sequential_time / concurrent_time:.1f}x")

asyncio.run(main())


#სავარჯიშო 2

import asyncio
import time


async def square(number):
    await asyncio.sleep(1)
    return number * number


numbers = [1, 2, 3, 4, 5, 6, 7, 8]


async def main():
    start = time.perf_counter()
    squares = await asyncio.gather(*(square(n) for n in numbers))
    elapsed = time.perf_counter() - start

    for n, sq in zip(numbers, squares):
        print(f"{n}² = {sq}")
    print(f"ჯამი: {sum(squares)}")
    print(f"დრო: {elapsed:.1f} წმ")

asyncio.run(main())


#სავარჯიშო 3

import asyncio
import time


async def load_user(user_id):
    await asyncio.sleep(1) 
    return {"id": user_id, "name": f"მომხმარებელი {user_id}"}


async def main():
    start = time.perf_counter()
    users = await asyncio.gather(*(load_user(uid) for uid in (1, 2, 3)))
    print(list(users))
    print(f"დრო: {time.perf_counter() - start:.1f} წმ")

asyncio.run(main())
