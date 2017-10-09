import asyncio


@asyncio.coroutine
def hello():
    print('hello asyncio')
    # 异步调用asyncio.sleep(1)
    yield from asyncio.sleep(1)  # 耗时1秒的IO操作
    print('hello again')


# 获取EventLoop
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
