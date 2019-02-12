# -*- coding:utf-8 -*-
from ScrapyNovel.books.spider_types import SpiderTypes
from ScrapyNovel.spiders.spider_base import NovelSpiderBase


class NovelSpider1(NovelSpiderBase):
    # name = "NovelQiShuLou"
    name = SpiderTypes.getTypeName_QiShuLou()

    def __init__(self):
        super().__init__()

    def getXpathList(self, response):
        return response.xpath('//div[@id="content-list"]/div[@class="book-list clearfix"]/ul/li')

    def getXpathMainInfo(self, response):
        return response.xpath('//div[@id="content-list"]/div[@class="book-intro clearfix"]/div[@class="book-describe"]')

    def getStrMainInfo_Name(self, info):
        return info.xpath('./h1/text()').extract()[0]

    def getStrMainInfo_Author(self, info):
        return info.xpath('./p/text()').extract()[0]

    def getStrItem_Link(self, item):
        return item.xpath('./a/@href').extract()[0]

    def getStrItem_Idex(self, item):
        return item.xpath('./a/text()').extract()[0]

    def getXpathItem_Main(self, response):
        return response.xpath('//div[@id="pagewrap"]/article[@class="post clearfix"]')

    def getStrItem_Title(self, xpath_main):
        return xpath_main.xpath('.//header[@class="post-header clearfix"]/h1/text()').extract()[0].strip().replace('  ', '').replace('\r', '').replace('\n', '').replace('\t', '')

    def getStrItem_Content(self, xpath_main):
        return xpath_main.xpath('.//text()').extract()
