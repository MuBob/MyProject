# -*- coding:utf-8 -*-
import re
from ScrapyNovel.books.spider_types import SpiderTypes
from ScrapyNovel.spiders.spider_base import NovelSpiderBase

class NovelSpider1(NovelSpiderBase):
    # name = "NovelGuaZiBpi"
    name = SpiderTypes.getTypeName_YanQingKu()

    def __init__(self):
        super().__init__()
        self.headLink = "http://www.yqk.net/yanqing"

    def getXpathMainInfo(self, response):
        return response.xpath('//div[@class="base"]')

    def getStrMainInfo_Name(self, info):
        return info.xpath('./p/strong/a/text()').extract()[0]

    def getStrMainInfo_Author(self, info):
        return info.xpath('./p/a/text()').extract()[0]

    def getXpathList(self, response):
        return response.xpath('//dl[@class="chapter"]/dd')

    def getStrItem_Link(self, item):
        lastLink=item.xpath('./a/@href').extract()[0]
        return lastLink

    def getStrItem_Idex(self, item):
        lastLink = item.xpath('./a/@href').extract()[0]
        index = re.findall("(.*).html.*", lastLink)[0]
        return index

    def getXpathItem_Main(self, response):
        return response.xpath('//div[@class="main"]')

    def getStrItem_Title(self, xpath_main):
        title = xpath_main.xpath('.//div[@class="title"]/text()').extract()[0].strip().replace('  ', '').replace('\r', '').replace('\n', '').replace('\t', '')
        lastIndex = title.find("作者")
        return title[0:lastIndex]

    def getStrItem_Author(self, xpath_main):
        title = xpath_main.xpath('.//div[@class="title"]/text()').extract()[0].strip().replace('  ', '').replace('\r', '').replace('\n', '').replace('\t', '')
        lastIndex = title.find("作者")
        if lastIndex > 0:
            length = len(title)
            return title[lastIndex:length]
        else:
            return ""
    def getStrItem_Content(self, xpath_main):
        return xpath_main.xpath('.//div[@class="content"]//text()').extract()
