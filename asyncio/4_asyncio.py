import asyncio

# async & awit 关键字在Python3.5版本中正式引入，基于他编写的协程代码其实就是 上一示例 的加强版，让代码可以更加简便。
# @asyncio.coroutine
# def func1():
#     print(1)
#     yield from asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到tasks中的其他任务
#     print(2)
#
#
# @asyncio.coroutine
# def func2():
#     print(3)
#     yield from asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到tasks中的其他任务
#     print(4)
#
#
# tasks = [
#     asyncio.ensure_future(func1()),
#     asyncio.ensure_future(func2())
# ]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
import asyncio


async def func1():
    print(1)
    await asyncio.sleep(2)
    print(2)


async def func2():
    print(3)
    await asyncio.sleep(2)
    print(4)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
