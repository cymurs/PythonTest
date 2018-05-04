#-*- coding:utf-8 -*-
__author__ = 'Administrator'

from scrapy import cmdline

# cmdline.execute("scrapy crawl doubanspider -o movies.json".split())
cmdline.execute("scrapy crawl doubanspider".split())