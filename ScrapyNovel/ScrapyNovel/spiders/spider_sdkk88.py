# -*- coding:utf-8 -*-
import re
from ScrapyNovel.books.books_setting import BooksSetting
from ScrapyNovel.books.spider_types import SpiderTypes
from ScrapyNovel.spiders.spider_base import NovelSpiderBase


class NovelSpider1(NovelSpiderBase):
    # name = "NovelSDKK88"
    name = SpiderTypes.getTypeName_SDKK88()

    def __init__(self):
        super().__init__()
        self.headLink = "http://www.sbkk88.com"

    def getXpathList(self, response):
        return response.xpath('//div[@class="mingzhuMain"]/div[@class="mingzhuLeft"]/ul[@class="leftList"]/li')

    def getXpathMainInfo(self, response):
        return response.xpath('//div[@class="mingzhuMain"]/div[@class="mingzhuLeft"]/ul[@class="leftList"]/li')

    def getStrMainInfo_Name(self, info):
        extract_author = info.xpath(
            '//div[@class="mingzhuMain"]/div[@class="mingzhuLeft"]/div[@class="mingzhuTitle"]/h1/text()').extract()[0]
        find_author = re.findall(".*：(.*)", extract_author)[0]
        if len(find_author) > 0:
            author = find_author
        else:
            author = extract_author
        return author

    def getStrItem_Link(self, item):
        part_url = item.xpath('./a/@href').extract()[0]
        link = self.headLink + part_url
        return link

    def getStrItem_Idex(self, item):
        return item.xpath('./a/text()').extract()[0]

    def getXpathItem_Main(self, response):
        return response

    def getStrItem_Author(self, xpath_main):
        return xpath_main.xpath('./dd')[1].xpath('./h3/text()').extract()[0]

    def getStrItem_Title(self, xpath_main):
        return xpath_main.xpath('//div[@id="f_title1"]/h1/text()').extract()[0]

    def getStrItem_Content(self, xpath_main):
        return xpath_main.xpath('//div[@id="f_content1"]/div[@id="f_article"]/p/text()').extract()

