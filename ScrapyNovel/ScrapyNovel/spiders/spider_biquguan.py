# -*- coding:utf-8 -*-
from ScrapyNovel.books.spider_types import SpiderTypes
from ScrapyNovel.spiders.spider_base import NovelSpiderBase


class NovelSpider1(NovelSpiderBase):
    # name = "NovelBQG"
    name = SpiderTypes.getTypeName_BiQuGuan()

    def __init__(self):
        super().__init__()

    def getXpathList(self, response):
        return response.xpath('//div[@id="wrapper"]/div[@class="box_con"]/div[@id="list"]/dl/dd')

    def getXpathMainInfo(self, response):
        return response.xpath('//div[@id="wrapper"]/div[@class="box_con"]/div[@id="maininfo"]/div[@id="info"]')

    def getStrMainInfo_Name(self, info):
        return info.xpath('./h1/text()').extract()[0]

    def getStrMainInfo_Author(self, info):
        return info.xpath('./p/text()').extract()[0]

    def getStrItem_Link(self, item):
        part_url = item.xpath('./a/@href').extract()[0]
        link = self.urls[0] + part_url
        return link

    def getStrItem_Idex(self, item):
        return item.xpath('./a/text()').extract()[0]

    def getXpathItem_Main(self, response):
        return response.xpath('//div[@class="box_con"]')

    def getStrItem_Title(self, xpath_main):
        return xpath_main.xpath('.//div[@class="bookname"]/h1/text()').extract()[0].strip().replace('  ',
                                                                                                    '').replace(
            '\r', '').replace('\n', '').replace('\t', '')

    def getStrItem_Content(self, xpath_main):
        return xpath_main.xpath('.//div[@id="content"]/text()').extract()
