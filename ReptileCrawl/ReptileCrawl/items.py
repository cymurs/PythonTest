# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ReptilecrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_name = scrapy.Field()      #电影名
    movie_director = scrapy.Field()  #电影导演
    movie_actor = scrapy.Field()     #电影主演
    movie_year = scrapy.Field()      #上映日期
    movie_nation = scrapy.Field()    #上映国家
    movie_type = scrapy.Field()      #电影类型
    movie_rating = scrapy.Field()    #电影星级
    movie_average = scrapy.Field()   #电影评分
    movie_comment = scrapy.Field()   #电影评论数
    movie_quote = scrapy.Field()     #经典台词
