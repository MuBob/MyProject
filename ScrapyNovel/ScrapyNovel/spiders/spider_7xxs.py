# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
import re
from ScrapyNovel.books.spider_types import SpiderTypes
from ScrapyNovel.spiders.spider_base import NovelSpiderBase

class NovelSpider1(NovelSpiderBase):
    # name = "Novel7xxs"
    name = SpiderTypes.getTypeName_7xxs()

    def __init__(self):
        super().__init__()
        self.headLink = "http://www.7xxs.net"

    def getXpathList(self, response):
        return response.xpath('//div[@class="box_con"]/div[@id="list"]/dl/dd')

    def getXpathMainInfo(self, response):
        return response.xpath('//div[@class="box_con"]/div[@id="maininfo"]')

    def getStrMainInfo_Name(self, info):
        return info.xpath('./div[@id="intro"]/text()').extract()[0]

    def getStrMainInfo_Author(self, info):
        return info.xpath('./div[@id="info"]/p/text()').extract()[0]

    def getStrItem_Link(self, item):
        lastLink=item.xpath('./a/@href').extract()[0]
        link = self.headLink + lastLink
        return link

    def getStrItem_Idex(self, item):
        lastLink = item.xpath('./a/@href').extract()[0]
        index = re.findall(".*/(.*).html.*", lastLink)[0]
        return index

    def getXpathItem_Main(self, response):
        return response.xpath('//div[@class="content_read"]/div[@class="box_con"]')

    def getStrItem_Title(self, xpath_main):
        return xpath_main.xpath('.//div[@class="bookname"]/h1/text()').extract()[0].strip().replace('  ', '').replace('\r', '').replace('\n', '').replace('\t', '')

    def getStrItem_Content(self, xpath_main):
        return xpath_main.xpath('.//div[@id="content"]/text()').extract()
