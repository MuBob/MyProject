# -*- coding:utf-8 -*-
from ScrapyNovel.books.spider_types import SpiderTypes
from ScrapyNovel.spiders.spider_base import NovelSpiderBase


class NovelSpider1(NovelSpiderBase):
    # name = "NovelShuXiangGe"
    name = SpiderTypes.getTypeName_ShuXiangGe()

    def __init__(self):
        super().__init__()

    def getXpathMainInfo(self, response):
        return response.xpath('//div[@class="mu_contain"]/div[@class="info"]/div[@class="book"]')

    def getStrMainInfo_Name(self, info):
        return info.xpath('./h1/a/text()').extract()[0]

    def getStrMainInfo_Author(self, info):
        return info.xpath('./dl/dt/text()').extract()[0]

    def getXpathList(self, response):
        return response.xpath('//div[@class="warpper"]/div[@class="mu_contain"]/ul[@class="mulu_list"]/li')

    def getStrItem_Link(self, item):
        part_url = item.xpath('./a/@href').extract()[0]
        link = self.urls[0] + part_url
        return link

    def getStrItem_Idex(self, item):
        return item.xpath('./a/text()').extract()[0]

    def getXpathItem_Main(self, response):
        return response.xpath('//table[@id="content"]/tbody/tr/td')

    def getStrItem_Title(self, xpath_main):
        return xpath_main.xpath('./h1/text()').extract()[0]\
            .strip()\
            .replace('  ','')\
            .replace('\r', '')\
            .replace('\n', '')\
            .replace('\t', '')

    def getStrItem_Content(self, xpath_main):
        return xpath_main.xpath('./div[@id="htmlContent"]/text()').extract()
