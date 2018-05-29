#!/usr/bin/env python
# coding=utf-8

import asyncio
import time


now = lambda : time.time()


async def do_something(x):
    print ('Waiting: {}'.format(x))


start = now()
coroutine = do_something(1)   # 协程对象不能直接运行
loop = asyncio.get_event_loop()
task = loop.create_task(coroutine)
print (task)
loop.run_until_complete(task)
print (task)
print ('TIME: {}', now()-start)

