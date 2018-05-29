#!/usr/bin/env python
# coding=utf-8


import time
from multiprocessing import Process
from pp.getter import Getter
from pp.tester import Tester
from pp.RedisClient import RedisClient
from pp import settings


class Scheduler():

    def schedule_tester(self, cycle=settings.TESTER_CYCLE):
        '''
        定时测试代理
        '''
        tester = Tester()
        while True:
            print ('测试开始运行')
            tester.run()
            time.sleep(cycle)


    def schedule_getter(self, cycle=settings.GETTER_CYCLE):
        '''
        定时抓取
        '''
        getter = Getter()
        while True:
            getter.run()
            time.sleep(cycle)
    
    def schedule_api(self):
        app.run(settings.API_HOST, settings.API_port)

    def run(self):
        print ('开启代理池')
        if settings.TESTER_ENABLE:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()
        if settings.GETTER_ENABLE:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()
        if settings.API_ENABLE:
            api_process = Process(target=self.schedule_api)

