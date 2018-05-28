#!/usr/bin/env python
# coding=utf-8


# Redis
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = 'proxy'


# 代理分数
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10


# 返回的状态码
VALID_STATUS_CODES = [200, 302]


# 代理池ip数量
POOL_UPPER_THRESHOLD = 50000


# 检查周期
TESTER_CYCLE = 20
# 抓取的周期
GETTER_CYCLE = 300


# 测试API, 一会配置爬哪个抓那个



# API配置
API_HOST = '0.0.0.0'
API_PORT = 5555


# 开关?
TESTER_ENABLE = True
GETTER_ENABLE = True
API_ENABLE = True


# 最大的批测试数量
BATCH_TEST_SIZE = 10

