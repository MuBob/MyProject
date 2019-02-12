# -*- coding:utf-8 -*-
from ScrapyNovel.books.spider_types import SpiderTypes
from ScrapyNovel.spiders.spider_base import NovelSpiderBase


class NovelSpider1(NovelSpiderBase):
    # name = "NovelBookbao8"
    name = SpiderTypes.getTypeName_BookBao()

    def __init__(self):
        super().__init__()
        self.headLink="https://www.bookbao8.com"

    def getXpathList(self, response):
        return response.xpath('//div[@class="wp b2 info_chapterlist"]/ul/li')

    def getXpathMainInfo(self, response):
        return response.xpath('//div[@class="wp b2 info_chapterlist"]/ul/li')

    def getStrItem_Link(self, item):
        part_url = item.xpath('./a/@href').extract()[0]
        link = self.headLink + part_url
        return link

    def getStrItem_Idex(self, item):
        return item.xpath('./a/text()').extract()[0]

    def getXpathItem_Main(self, response):
        return response.xpath('//div[@class="bdsub"]/dl')

    def getStrItem_Name(self, xpath_main):
        return xpath_main.xpath('./dd')[0].xpath('./h1/a/text()').extract()[0]

    def getStrItem_Author(self, xpath_main):
        return xpath_main.xpath('./dd')[1].xpath('./h3/text()').extract()[0]

    def getStrItem_Title(self, xpath_main):
        return xpath_main.xpath('./dd')[0].xpath('./h1/text()').extract()[0].strip().replace('  ',
                                                                                                    '').replace(
            '\r', '').replace('\n', '').replace('\t', '')

    def getStrItem_Content(self, xpath_main):
        return xpath_main.xpath('./dd[@id="contents"]/text()').extract()
