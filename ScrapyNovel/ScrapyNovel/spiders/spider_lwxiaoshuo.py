# -*- coding:utf-8 -*-
from ScrapyNovel.books.books_setting import BooksSetting

from ScrapyNovel.books.spider_types import SpiderTypes
from ScrapyNovel.spiders.spider_base import NovelSpiderBase
#已废弃
class NovelShiZhangFuRen(NovelSpiderBase):
    # name = "NovelLeWenXiaoShuo"
    name=SpiderTypes.getTypeName_LeWenXiaoShuo()

    def __init__(self):
        super().__init__()
        self.headLink = "http://www.lwxiaoshuo.com"
        self.web_head = BooksSetting.getHtml()
        self.web_last = ".html"

    def getXpathList(self, response):
        return response.xpath('//table[@style="MARGIN-BOTTOM: 10px"]/tbody')

    def getXpathMainInfo(self, response):
        return response.xpath('//table[@style="MARGIN-BOTTOM: 10px"]/tbody')

    def getStrItem_Name(self, xpath_main):
        return xpath_main.xpath('./div/h1/text()').extract()[0]

    def getStrItem_Author(self, xpath_main):
        return xpath_main.xpath('./div/div[@class="border_b"]/text()').extract()[0]

    def getStrItem_Link(self, item):
        part_url = item.xpath('.//tr/td/div[@class="dccss"]/a/@href').extract()
        link = self.headLink + part_url
        return link

    def getStrItem_Idex(self, item):
        return item.xpath('.//tr/td/div[@class="dccss"]/a/text()').extract()

    def getXpathItem_Main(self, response):
        return response.xpath('//table[@class="border_l_r"]/tbody/tr/td')

    def getStrItem_Title(self, xpath_main):
        return xpath_main.xpath('./div/h2/text()').extract()[0].strip().replace('  ',
                                                                                                    '').replace(
            '\r', '').replace('\n', '').replace('\t', '')

    def getStrItem_Content(self, xpath_main):
        return xpath_main.xpath('./table/tbody/tr/td/div/p/text()').extract()

