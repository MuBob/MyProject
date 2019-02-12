# -*- coding:utf-8 -*-
from ScrapyNovel.books.spider_types import SpiderTypes
from ScrapyNovel.spiders.spider_base import NovelSpiderBase


class NovelXinShuLa(NovelSpiderBase):
    # name="NovelXinShuLa"
    name= SpiderTypes.getTypeName_XinShuLa()

    def __init__(self):
        super().__init__()

    def getXpathList(self, response):
        return response.xpath('//div[@class="bookcontent"]/dl/dd')

    def getXpathMainInfo(self, response):
        return response.xpath('//div[@class="bookcontent"]/dl/dd')

    def getStrItem_Link(self, item):
        part_url = item.xpath('./a/@href').extract()[0]
        link = self.start_urls[0] + part_url
        return link

    def getStrItem_Idex(self, item):
        return item.xpath('./a/text()').extract()

    def getXpathItem_Main(self, response):
        return response.xpath('//body[@id="bgdiv"]')

    def getStrItem_Name(self, xpath_main):
        return xpath_main.xpath('./div[@class="top"]/div[@class="top_left"]/a/strong/text()').extract()[0]

    def getStrItem_Author(self, xpath_main):
        return xpath_main.xpath('./div[@class="top"]/div[@class="top_left"]/a/text()').extract()[2]

    def getStrItem_Title(self, xpath_main):
        return xpath_main.xpath('./div[@class="chapter_title"]/h1/text()').extract()[0]

    def getStrItem_Content(self, xpath_main):
        return xpath_main.xpath('./div[@id="content"]/text()').extract()

