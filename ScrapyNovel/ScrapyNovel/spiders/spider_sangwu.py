# -*- coding:utf-8 -*-
from ScrapyNovel.books.spider_types import SpiderTypes
from ScrapyNovel.spiders.spider_base import NovelSpiderBase


class NovelSangWu(NovelSpiderBase):
    # name = "NovelSangWu"
    name = SpiderTypes.getTypeName_SangWu()
    start_urls = [
        "http://www.sangwu.org/book/5/5952/"
    ]

    def __init__(self):
        super().__init__()

    def getXpathList(self, response):
        return response.xpath('//dd')

    def getXpathMainInfo(self, response):
        return response.xpath('//div[@class="wp b2 info_chapterlist"]/ul/li')

    def getStrItem_Link(self, item):
        part_url = item.xpath('./a/@href').extract()
        link = self.start_urls[0] + part_url
        return link

    def getStrItem_Idex(self, item):
        return item.xpath('./a/text()').extract()

    def getXpathItem_Main(self, response):
        return response.xpath('//div[@class="readmain"]')

    def getStrItem_Name(self, xpath_main):
        return xpath_main.xpath('./div[@class="bookname"]/h2/text()').extract()[0]

    def getStrItem_Author(self, xpath_main):
        return xpath_main.xpath('./div[@class="bookname"]/h2/text()').extract()[0]

    def getStrItem_Title(self, xpath_main):
        return xpath_main.xpath('./div[@class="bookname"]/h1/text()').extract()[0]

    def getStrItem_Content(self, xpath_main):
        return xpath_main.xpath('./div[@class="centent"]/text()').extract()

