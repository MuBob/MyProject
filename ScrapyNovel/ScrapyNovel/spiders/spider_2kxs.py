# -*- coding:utf-8 -*-

from ScrapyNovel.books.books_setting import BooksSetting
from ScrapyNovel.books.spider_types import SpiderTypes
from ScrapyNovel.spiders.spider_base import NovelSpiderBase


class NovelYanYang(NovelSpiderBase):
    # name = "Novel2KXS"
    name= SpiderTypes.getTypeName_2KXiaoShuo()

    def __init__(self):
        super().__init__()
        self.headLink="http://www.2kxs.com"

    def getXpathList(self, response):
        return response.xpath('//dl[@class="book"]/dd')

    def getXpathMainInfo(self, response):
        return response.xpath('//div[@id="bookinfo"]/div[@id="title"]')

    def getStrMainInfo_Name(self, info):
        return info.xpath('./h1/text()').extract()[0]

    def getStrMainInfo_Author(self, info):
        return info.xpath('./address[@class="author"]/a/text()').extract()[0]

    def getStrItem_Link(self, item):
        try:
            part_url = item.xpath('./a/@href').extract()[0]
        except:
            part_url=""
        if part_url.__contains__(BooksSetting.getHtmlLast()):
            link = self.urls[0] + part_url
        else:
            link=""
        return link

    def getStrItem_Idex(self, item):
        return item.xpath('./a/text()').extract()[0]

    def getXpathItem_Main(self, response):
        return response.xpath('//div[@id="box"]')

    def getStrItem_Title(self, xpath_main):
        return xpath_main.xpath('./h2/text()').extract()[0].strip().replace('  ',
                                                                                                    '').replace(
            '\r', '').replace('\n', '').replace('\t', '')

    def getStrItem_Content(self, xpath_main):
        return xpath_main.xpath('./p[@class="Text"]/text()').extract()
