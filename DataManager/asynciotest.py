import asyncio

async def fun1():
    print(123456)
    await asyncio.sleep(3)
    print(7891011)

asyncio.run(fun1())