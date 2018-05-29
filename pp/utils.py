#!/usr/bin/env python
# coding=utf-8

import requests
from requests.exceptions import ConnectionError


base_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Sccept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
}

def get_page(url, options={}):
    headers = dict(base_headers, **options)
    print ('抓取', url)
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            print ('抓取成功')
            return resp.text
    except ConnectionError as e:
        print ('抓取失败{}'.format(e.args))
        return None
    
