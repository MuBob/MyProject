# -*- coding:utf-8 -*-
from ScrapyNovel.books.spider_types import SpiderTypes
from ScrapyNovel.spiders.spider_base import NovelSpiderBase

#已废弃
class NovelShiZhangFuRen(NovelSpiderBase):
    # name = "NovelLWXS520"
    name=SpiderTypes.getTypeName_LWXiaoShuo520()

    def __init__(self):
        super().__init__()

    def getXpathList(self, response):
        return response.xpath('//div[@id="defaulthtml4"]/table/tbody/tr/td/div[@class="dccss"]')

    def getXpathMainInfo(self, response):
        return response.xpath('//div[@id="defaulthtml4"]/table/tbody/tr/td/div[@class="dccss"]')

    def getStrItem_Link(self, item):
        part_url = item.xpath('./a/@href').extract()[0]
        link = self.start_urls[0] + part_url
        return link

    def getStrItem_Idex(self, item):
        return item.xpath('./a/text()').extract()[0]

    def getXpathItem_Main(self, response):
        return response.xpath('//table[@class="border_l_r"]/tbody/tr/td/div')

    def getStrItem_Name(self, xpath_main):
        return xpath_main.xpath('./h2/text()').extract()[0]

    def getStrItem_Author(self, xpath_main):
        return xpath_main.xpath('./div[@class="border_b"]/text()').extract()[0]

    def getStrItem_Title(self, xpath_main):
        return xpath_main.xpath('./h1/text()').extract()[0]

    def getStrItem_Content(self, xpath_main):
        return xpath_main.xpath('./table/tbody/tr/td/div/p/text()').extract()

