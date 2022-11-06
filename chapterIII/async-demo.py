import time

import asyncio


async def fun1():
    print("hello I’m chong")
    await asyncio.sleep(3)
    print("chong is over")


async def fun2():
    print("hello I’m chong")
    await asyncio.sleep(3)
    print("chong is over")


async def main():
    # 第一种使用
    # f1 =fun1()
    # await f1
    # 第二种 推荐
    task = [
        asyncio.create_task(fun1()),
        asyncio.create_task(fun2())
    ]
    await asyncio.wait(task)


if __name__ == '__main__':
    asyncio.run(main())
