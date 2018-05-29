#!/usr/bin/env python
# coding=utf-8

import asyncio
import time


now = lambda : time.time()


async def do(x: int):
    print ('Waiting: {}'.format(x))


async def main():
    c1 = do(1)
    c2 = do(2)
    c3 = do(3)

    tasks = [
        asyncio.ensure_future(c1),
        asyncio.ensure_future(c2),
        asyncio.ensure_future(c3)
    ]
    return await asyncio.wait(tasks)
    # return await asyncio.gether(*tasks)

start = now()
loop = asyncio.get_event_loop()
done, pending = loop.run_until_complete(main())
for task in done:
    print ('Task:', task)

# results = loop.run_until_complete(main())
# for result in results:
#     print ('Task: ', result.result())

