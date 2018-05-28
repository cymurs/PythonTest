#-*- coding:utf-8 -*-
__author__ = 'Administrator'

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy import Request

urls_dict = [
    {'name':'binance', 'domain':'support.binance.com', 'url':'https://support.binance.com/hc/zh-cn/sections/115000106672-%E6%96%B0%E5%B8%81%E4%B8%8A%E7%BA%BF'},
    {'name':'huobipro', 'domain':'www.huobi.pro', 'url':'https://www.huobi.pro/zh-cn/notice/'}
]

class AnnouncementSpider(CrawlSpider):
    name = 'announcement'
    allowed_domains = ['support.binance.com', 'www.huobi.pro']
    start_urls = ['https://support.binance.com/hc/zh-cn/sections/115000106672-%E6%96%B0%E5%B8%81%E4%B8%8A%E7%BA%BF']

    def parse(self, response):
        print('===Spider beginning===')
        sel = Selector(response)
        parse_binance_new()

    def parse_binance_new(self, response):
        pass