#!/usr/bin/env python
# coding=utf-8

import asyncio
import time


now = lambda : time.time()


async def do_something(x):
    print ('Waiting: {}'.format(x))


def callback(future):
    print ('CallBack: {}'.format(future.result()))


start = now()
coroutine = do_something(1)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)
loop.run_until_complete(task)

print ('TIME {}'.format(now()-start))
