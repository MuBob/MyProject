# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovellewenItem(scrapy.Item):
    name = scrapy.Field()
    author=scrapy.Field()
    chapter=scrapy.Field()
    title=scrapy.Field()
    content=scrapy.Field()