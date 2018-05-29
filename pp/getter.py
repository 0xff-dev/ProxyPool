#!/usr/bin/env python
# coding=utf-8


from pp.tester import Tester
from pp.RedisClient import RedisClient
from pp.Crawler import Crawler
from pp import settings
import sys


class Getter(object):
    
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()

    def is_over_threshold(self):
        '''
        判断是否超出了抓取的限制
        '''
        if self.redis.count >= settings.POOL_UPPER_THRESHOLD:
            return True
        return False

    def run(self):
        print ('开始抓取')
        if not self.is_over_threshold():
            for callback_label in range(self.crawler.__CrawlFuncCont__):
                callback = self.crawler.__CrawlFuncCont__[callback_label]
                proxies = self.crawler.get_proxies(callback)
                sys.stdout.flush()
                for proxy in proxies:
                    self.redis.add(proxy)

