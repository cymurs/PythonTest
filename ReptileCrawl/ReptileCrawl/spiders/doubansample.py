#-*- coding:utf-8 -*-
__author__ = 'Administrator'

import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from ReptileCrawl.items import ReptilecrawlItem



class DoubanSpider(CrawlSpider):
    name = "doubanspider"
    allowed_domains = ["movie.douban.com"]
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        sel = Selector(response)
        movie_list = sel.css('#content > div > div > ol > li > div')

        for movie in movie_list:
            item = ReptilecrawlItem()
            try:
                # strip() 方法用于移除字符串头尾指定的字符（默认为空格）
                item['movie_name'] = movie.xpath('div[@class="info"]/div[1]/a/span[1]/text()').extract()[0].strip()

                pub = movie.xpath('div[@class="info"]/div[2]/p[1]/text()').extract()[0].strip().split()
                # print ','.join(pub)
                item['movie_director'] = pub[1]
                for idx in range(2, len(pub)-1):
                    if 0 == cmp(pub[idx], u"主演:"):
                        item['movie_actor'] = pub[idx+1]
                        break

                sub = movie.xpath('div[@class="info"]/div[2]/p[1]/text()').extract()[1].strip().split()
                #print ','.join(sub)
                item['movie_year'] = 0
                for idx in range(len(sub[0])-1, 0, -1):
                    if sub[0][0:idx+1].isdigit():
                        item['movie_year'] = int(sub[0][0:idx+1])
                        break
                ran = min(len(sub)-1, 7)
                for idx in range(3, ran):
                    if 0 == cmp(sub[idx], "/"):
                        item['movie_nation'] = ','.join(sub[2:idx])
                        item['movie_type'] = ','.join(sub[idx+1:])
                        break

                rat = movie.xpath('div[@class="info"]/div[2]/div[@class="star"]/span[1]/@class').extract()[0].strip().split('g')[1].split('-')[0]
                if len(rat) is 2:
                    rat = '.'.join(rat)
                item['movie_rating'] = float(rat)
                item['movie_average'] = float(movie.xpath('div[@class="info"]/div[2]/div[@class="star"]/span[2]/text()').extract()[0].strip())
                #print rat

                com = movie.xpath('div[@class="info"]/div[2]/div[@class="star"]/span[4]/text()').extract()[0].strip()
                comnum = com.find(u"人")
                item['movie_comment'] = int(com[:comnum])
                #print item['movie_comment']
                quote = movie.xpath('div[@class="info"]/div[2]/p[@class="quote"]/span/text()').extract()
                if quote:
                    item['movie_quote'] = quote[0].strip()
                else:
                    item['movie_quote'] = ''
                yield item
            except:
                print 'Meet error!!!'
                pass

        try:
            nextHref = sel.xpath('//div[@class="article"]/div[@class="paginator"]/span[@class="next"]/a/@href').extract_first()
            if nextHref:
                nextPage = nextHref.strip()
                next_url = 'https://movie.douban.com/top250' + nextPage
                yield scrapy.http.Request(next_url, callback=self.parse)
            else:
                print nextHref #None
                print 'This is last page!'
        except:
            print '==Game over=='
            pass