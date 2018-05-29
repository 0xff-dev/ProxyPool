#!/usr/bin/env python
# coding=utf-8

import redis
from random import choice
from Error import PoolEmptyError
from settings import MAX_SCORE, MIN_SCORE, INITIAL_SCORE
from settings import REDIS_HOST, REDIS_PORT, REDIS_KEY, REDIS_PASSWORD


# Redis的api请参考    http://redisdoc.com/


class RedisClient(object):

    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        '''
        初始化redis缓存数据库
        :param host Redis 地址
        :param port Redis 端口
        :param password Redis 密码
        '''
        self.db = redis.StrictRedis(host=host, port=port, 
                password=password,decode_responses=True)

    def add(self, proxy, score=INITIAL_SCORE):
        '''
        向数据库添加一个代理
        '''
        if not self.db.zscore(REDIS_KEY, proxy):
            return self.db.zadd(REDIS_KEY, score, proxy)

    def random(self):
        '''
        随机获取有效的代理
        '''
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):
                return choice(result)
            else:
                raise PoolEmptyError

    def decrase(self, proxy):
        '''
        一个proxy测试失败一次，分数-1,直到咯屁
        '''
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print ('代理:{}, 当前分数: {}-1'.format(proxy, score))
            self.db.zincrby(REDIS_KEY, proxy, -1)
        else:
            print ('代理{}, 分数为0, 移除'.format(proxy))
            return self.db.zrem(REDIS_KEY, proxy)

    def exists(self, proxy):
        # 只要不存在获取的分数就是None
        return not self.db.zscore(REDIS_KEY, proxy) == None

    def max(self, proxy):
        '''
        将代理的值设置为最大
        '''
        print ('代理{}, 分数为100')
        return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)

    def count(self):
        return self.db.zcard(REDIS_KEY)

    def all(self):
        '''
        返回全部的代理(后面的测试用?)
        '''
        return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)
    
    def batch(self, start, stop):
        return self.db.zrevrange(REDIS_KEY, start, stop-1)
    
