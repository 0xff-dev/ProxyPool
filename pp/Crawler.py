#!/usr/bin/env python
# coding=utf-8

import re
import requests
from utils import get_page
from pyquery import PyQuery as pq


class ProxyMetaClass(type):

    def __new__(cls, name, bases, attrs):
        count = 0
        attrs = ['__CrawlFunc__'] = []
        for key, value in attrs.items():
            if 'crawl_' in key:
                attrs['__CrawlFunc__'].append(key)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)

    
class Crawler(object, metaclass=ProxyMetaClass):

    def get_proxies(self, callback):
        proxies = []
        for proxy in eval('self.{}()'.format(callback)):
            print ('获取到代理')
            proxies.append(proxy)
        return proxies

    def crawl_daili66(self, page_count=4):
        '''
        获取代理66
        '''
        url = 'https://66ip.cn/{}.html'
        # 抓取4页
        urls = [url.format(page) for page in range(1, page_count+1)]
        for url in urls:
            print ('Crawing', url)
            html = get_page(url)
            if html:
                doc = pq(html)
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])

    def crawl_ip3366(self):
        
        for page in range(1, 5):
            html = get_page('http://www.ip3366.net/free/?page={}'.format(page))
            ip_address = re.compile('<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
            re_ip_address = ip_address.findall(html)
            for address, port in re_ip_address:
                result = address+':'+port
                yield result.replace(' ', '')
    
    def crawl_kuaidaili(self):
        for page in range(1, 5):
            start_url = 'https://www.kuaidaili.com/free/inha/{}/'.format(i)
            html = get_page(start_url)
            if html:
                ip_address = re.compile('<td data-title="IP">(.*?)</td>')
                re_ip_address = ip_address.findall(html) 
                port = re.compile('<td data-title="PORT">(.*?)</td>')
                re_port port.findall(html)
                for address, port in zip(re_ip_address, re_port):
                    address_port = address+':'+port
                    yield address_port.replace(' ', '')

    def crawl_xicidaili(self):
        for i in range(1, 3):
            start_url = 'http://www.xicidaili.com/nn/{}'.format(i)
            headers = {
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Cookie':'_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWRjYzc5MmM1MTBiMDMzYTUzNTZjNzA4NjBhNWRjZjliBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUp6S2tXT3g5a0FCT01ndzlmWWZqRVJNek1WanRuUDBCbTJUN21GMTBKd3M9BjsARg%3D%3D--2a69429cb2115c6a0cc9a86e0ebe2800c0d471b3',
                'Host':'www.xicidaili.com',
                'Referer':'http://www.xicidaili.com/nn/3',
                'Upgrade-Insecure-Requests':'1',
            }
            html = get_page(start_url, options=headers)
            if html:
                find_trs = re.compile('<tr class.*?>(.*?)</tr>', re.S)
                trs = find_trs.findall(html)
                for tr in trs:
                    find_ip = re.compile('<td>(\d+\.\d+\.\d+\.\d+)</td>')
                    re_ip_address = find_ip.findall(tr)
                    find_port = re.compile('<td>(\d+)</td>')
                    re_port = find_port.findall(tr)
                    for address,port in zip(re_ip_address, re_port):
                        address_port = address+':'+port
                        yield address_port.replace(' ','')
