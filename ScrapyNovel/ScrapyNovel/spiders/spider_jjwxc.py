# -*- coding:utf-8 -*-
from ScrapyNovel.books.spider_types import SpiderTypes
from ScrapyNovel.spiders.spider_base import NovelSpiderBase

class NovelSpider1(NovelSpiderBase):
    # name = "NovelJJWXC"
    name = SpiderTypes.getTypeName_JJWXC()
    def __init__(self):
        super().__init__()

    def getXpathList(self, response):
        return response.xpath('//table[@class="cytable"]/tbody/tr[@itemprop="chapter"]')

    def getXpathMainInfo(self, response):
        return response.xpath('//table[@class="cytable"]/tbody/tr[@itemprop="chapter"]')

    def getStrItem_Name(self, xpath_main):
        return xpath_main.xpath('.//td[@class="noveltitle"]/h1/a/span/text()').extract()[0].strip().replace('  ', '').replace('\r', '').replace('\n', '').replace('\t', '')

    def getStrItem_Author(self, xpath_main):
        return xpath_main.xpath('.//td[@class="noveltitle"]/a/text()').extract()[0]

    def getStrItem_Link(self, item):
        try:
            url=item.xpath('./td/span[@itemprop="headline"]/div[@style="float:left"]/a/@href').extract()[0]
        except:
            url=""
        return url

    def getStrItem_Idex(self, item):
        return item.xpath('./td/span[@itemprop="headline"]/div[@style="float:left"]/a/text()').extract()[0]

    def getXpathItem_Main(self, response):
        return response.xpath('//table[@id="oneboolt"]')

    def getStrItem_Title(self, xpath_main):
        return xpath_main.xpath('.//div[@class="noveltext"]/div')[1].xpath('./h2/text()').extract()[0].strip().replace('  ',
                                                                                                    '').replace(
            '\r', '').replace('\n', '').replace('\t', '')

    def getStrItem_Content(self, xpath_main):
        return xpath_main.xpath('.//div[@class="noveltext"]/text()').extract()


