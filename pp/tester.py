#!/usr/bin/env python
# coding=utf-8

import asyncio
import aiohttp
import time
import sys
try:
    from aiohttp import ClientError
except:
    from aiohttp import ClientProxyConnectionError as ProxyConnectionError


from  RedisClient import RedisClient
from settings import *


class Tester(object):

    def __init__(self):
        self.redis = RedisClient()

    async def test_single_proxy(self, proxy):
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy, bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://'+proxy
                print ('测试代理: {}'.format(real_proxy))
                async with session.get(TEST_URL, proxy=real_proxy, 
                        allow_redirects=False, timeout=10) as resp:
                    if resp.status in VALID_STATUS_CODE:
                        self.redis.max(proxy)
                        print ('代理{} 可用'.format(real_proxy))
                    else:
                        self.redis.decrase(proxy)
                        print ('代理{}的返回状态错误'.format(real_proxy))
            except (ClientError, aiohttp.client_exceptions.ClientConnectorError, 
                    asyncio.TimeoutError, AttributeError):
                self.redis.decrase(proxy)
                print ("代理{}请求异常".format(real_proxy))

    def run(self):
        '''
        测试主函数
        '''
        print ('开始测试')
        try:
            count = self.redis.count()
            print ('当前剩余{}个代理'.format(count))
            for i in range(0, count, BATCH_TEST_SIZE):
                start = i
                stop = min(i+BATCH_TEST_SIZE, count)
                print ('测试测范围{}-{}'.format(start, stop))
                test_proxies = self.redis.batch(start, stop)
                loop = asyncio.get_event_loop()
                tasks = [self.test_single_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks))
                sys.stdout.flush()
                time.sleep(2)
        except Exception as e:
            print ('测试异常{}'.format(e.args))

