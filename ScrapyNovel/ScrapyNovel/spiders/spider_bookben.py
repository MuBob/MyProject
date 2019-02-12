# -*- coding:utf-8 -*-
import re
from ScrapyNovel.books.books_setting import BooksSetting
from ScrapyNovel.books.spider_types import SpiderTypes
from ScrapyNovel.spiders.spider_base import NovelSpiderBase

#待使用
class NovelSpider(NovelSpiderBase):
    # name = "NovelBookben"
    name = SpiderTypes.getTypeName_BookBen()

    def __init__(self):
        super().__init__()

    def getXpathList(self, response):
        return ""

    def getXpathMainInfo(self, response):
        return ""
    def getStrItem_Link(self, item):
        return ""

    def getStrItem_Idex(self, item):
        return ""
    def getStrMainInfo_Name(self, info):
        return ""
    def getStrMainInfo_Author(self, info):
        return ""
    def getXpathItem_Main(self, response):
        return ""
    def getStrItem_Title(self, xpath_main):
        return ""
    def getStrItem_Content(self, xpath_main):
        return ""