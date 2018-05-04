#-*- coding:utf-8 -*-
__author__ = 'Administrator'

from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import HtmlResponse


class Douban(CrawlSpider):
    name = "doubanTest"
    start_urls = ['https://movie.douban.com/top250']

    '''
    rules = (
        Rule(SgmlLinkExtractor(), callback='parse_start_url', follow=True),
    )
    '''

    def parse(self, response):
        print "hello,world"

        hxs = Selector(response)
        result = hxs.xpath('/html/body/div/div/div/a/text()').extract()
        content = "".join(result)
        print content

        htl = '<html><body><span>好!很好!非常好!</span></body></html>'
        tet = "".join(Selector(text=htl).xpath('//span/text()').extract())
        print tet





