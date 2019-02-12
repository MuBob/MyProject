# -*- coding:utf-8 -*-
from ScrapyNovel.books.spider_types import SpiderTypes
from ScrapyNovel.spiders.spider_base import NovelSpiderBase


class NovelSpider1(NovelSpiderBase):
    # name = "NovelYueDu163"
    name = SpiderTypes.getTypeName_YueDu163()

    def __init__(self):
        super().__init__()
        self.headLink = "http://yuedu.163.com"

    def getXpathList(self, response):
        return self.getXpathMainInfo(response).xpath('./div/div/ul')

    def getXpathMainInfo(self, response):
        return response.xpath('//div[@class="g-mn"]')

    def getStrMainInfo_Name(self, info):
        return info.xpath('./div[@class="m-bookdetail"]/div[@class="f-fl"]/h3/@title').extract()[0]

    def getStrMainInfo_Author(self, info):
        return info.xpath('./div[@class="m-bookdetail"]/div[@class="f-fl"]/h3/span/a/text()').extract()[0]

    def getStrItem_Link(self, item):
        part_url = item.xpath('./a/@href').extract()[0]
        link = self.headLink + part_url
        return link

    def getStrItem_Idex(self, item):
        return item.xpath('./a/text()').extract()[0]

    def getXpathItem_Main(self, response):
        return response.xpath(
            '//div[@class="article J_Article"]/div[@class="portrait-page-box J_PortraitMoveBox"]/div[@class="article-content"]/div[@class="ne-content J_NEContent"]')

    def getStrItem_Title(self, xpath_main):
        return xpath_main.xpath('./h1/text()').extract()[0].strip().replace('  ',
                                                                            '').replace(
            '\r', '').replace('\n', '').replace('\t', '')

    def getStrItem_Content(self, xpath_main):
        return xpath_main.xpath('./p/text()').extract()
