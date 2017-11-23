# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SearchSinaItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  #名字
    sex= scrapy.Field()  #性别
    address = scrapy.Field()  #地址
    detail_link=scrapy.Field()  #主页链接
    number_guan_zhu=scrapy.Field()
    number_fen_si=scrapy.Field()
    number_wei_bo=scrapy.Field()
    info=scrapy.Field()  #个人信息
    label=scrapy.Field()  #所有标签
    pass
