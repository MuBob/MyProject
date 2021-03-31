# -*- coding:utf-8 -*-
import re
from ScrapyNovel.books.spider_types import SpiderTypes
from ScrapyNovel.spiders.spider_base import NovelSpiderBase

class NovelSpider1(NovelSpiderBase):
    # name = "NovelGuaZiBpi"
    name = SpiderTypes.getTypeName_GuaZiBpi()

    def __init__(self):
        super().__init__()
        self.headLink = "https://www.gzbpi.com"

    def getXpathMainInfo(self, response):
        return response.xpath('//div[@class="mu_contain"]')

    def getStrMainInfo_Name(self, info):
        return info.xpath('./div[@class="mu_h1"]/h1/text()').extract()[0]

    def getStrMainInfo_Author(self, info):
        return info.xpath('./div[@class="mu_beizhu"]/text()').extract()[0]

    def getXpathList(self, response):
        return response.xpath('//div[@class="mu_contain"]/ul[@class="mulu_list"]/li')

    def getStrItem_Link(self, item):
        lastLink=item.xpath('./a/@href').extract()[0]
        link = self.headLink + lastLink
        return link

    def getStrItem_Idex(self, item):
        lastLink = item.xpath('./a/@href').extract()[0]
        index = re.findall(".*/(.*).html.*", lastLink)[0]
        return index

    def getXpathItem_Main(self, response):
        return response.xpath('//div[@class="read"]/div[@class="read-box"]/div[@class="read-box"]/div[@class="chapter-page"]')

    def getStrItem_Title(self, xpath_main):
        return xpath_main.xpath('.//h4[@class="chaptername"]/text()').extract()[0].strip().replace('  ', '').replace('\r', '').replace('\n', '').replace('\t', '')

    def getStrItem_Author(self, xpath_main):
        return xpath_main.xpath('./p[@class="author"]/span/text()').extract()[0].strip().replace('  ', '').replace('\r', '').replace('\n', '').replace('\t', '')

    def getStrItem_Content(self, xpath_main):
        return xpath_main.xpath('.//div[@class="page-content"]/pre[@class="note PbRbuYwuzPK"]/text()').extract()
