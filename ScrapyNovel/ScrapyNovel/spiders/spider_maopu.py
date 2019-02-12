# -*- coding:utf-8 -*-
from ScrapyNovel.books.spider_types import SpiderTypes
from ScrapyNovel.spiders.spider_base import NovelSpiderBase

class NovelSpider(NovelSpiderBase):
    # name = "NovelMaoPu"
    name= SpiderTypes.getTypeName_MaoPu()

    def __init__(self):
        super().__init__()
        self.headLink="https://www.bookbao8.com"

    def getXpathList(self, response):
        return response.xpath('//div[@class="mu_contain"]/ul[@class="mulu_list"]/li')

    def getXpathMainInfo(self, response):
        return response.xpath('//div[@class="wp b2 info_chapterlist"]/ul/li')

    def getStrItem_Link(self, item):
        part_url = item.xpath('./a/@href').extract()[0]
        link = self.start_urls[0] + part_url
        return link

    def getStrItem_Idex(self, item):
        return ""

    def getXpathItem_Main(self, response):
        return response.xpath('//div[@id="content"]')

    def getStrItem_Name(self, xpath_main):
        return xpath_main.xpath('./h1/text()').extract()[0]

    def getStrItem_Author(self, xpath_main):
        return xpath_main.xpath('./h1/text()').extract()[0]

    def getStrItem_Title(self, xpath_main):
        return  xpath_main.xpath('./h1/text()').extract()[0]

    def getStrItem_Content(self, xpath_main):
        return xpath_main.xpath('./div[@class="chapter-content"]/text()').extract()

