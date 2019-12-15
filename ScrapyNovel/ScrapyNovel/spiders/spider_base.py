# -*- coding:utf-8 -*-
import re

import scrapy
from scrapy import Request

from ScrapyNovel.books.books_setting import BooksSetting
from ScrapyNovel.items import ScrapynovelItem

class NovelSpiderBase(scrapy.spiders.Spider):

    def getXpathList(self, response):
        return ""

    def getXpathMainInfo(self, response):
        return ""

    def getStrMainInfo_Name(self, info):
        return ""

    def getStrMainInfo_Author(self, info):
        return ""

    def getStrItem_Link(self, item):
        return ""

    def getStrItem_Idex(self, item):
        return ""

    def getXpathItem_Main(self, response):
        return ""

    def getStrItem_Name(self, xpath_main):
        return BooksSetting.getNovelName()

    def getStrItem_Author(self, xpath_main):
        return ""

    def getStrItem_Title(self, xpath_main):
        return ""

    def getStrItem_Content(self, xpath_main):
        return ""

    start_urls = [
        BooksSetting.getHtml()
    ]

    item_author = ""
    item_name = ""

    def __init__(self):
        self.urls = self.start_urls
        self.item_name=""
        self.item_author=""
        pass

    def parse(self, response):
        # self.print_response(response)
        list = self.getXpathList(response)
        info = self.getXpathMainInfo(response)
        # print("info=", info.extract())
        self.item_name = self.getStrMainInfo_Name(info)
        self.item_author = self.getStrMainInfo_Author(info)
        for item in list:
            link = self.getStrItem_Link(item)
            print("link=", link)
            if link=='': continue
            if self.urls.__contains__(link):
                continue
            else:
                index = self.getStrItem_Idex(item)
                print("index=%s, link=%s" % (index, link))
                self.urls.append(link)
                yield Request(link, method="GET", callback=self.parse_item)
                break

    def parse_item(self, response):
        self.print_response(response)
        xpath_main = self.getXpathItem_Main(response)
        item = ScrapynovelItem()
        item['name'] = self.getStrItem_Name(xpath_main) if self.item_name.strip()=='' else self.item_name
        item['author'] = self.getStrItem_Author(xpath_main) if self.item_author.strip()=='' else self.item_author
        item['title'] = self.getStrItem_Title(xpath_main)
        count = re.findall(BooksSetting.getHeadHtmlReg(), response.url)[0]
        if len(count) <= 1:
            count = '0' + count
        item['chapter'] = count
        item['content'] = self.list2str(self.getStrItem_Content(xpath_main))
        # print("item=", item)
        yield item

    def print_response(self, response):
        current_url = response.url  # 爬取时请求的url
        body = response.body  # 返回的html
        print("request=%s, response=%s" % (current_url, body))

    def list2str(self, list):
        s = ""
        for index in list:
            # print('index=',index)
            index.replace('\u3000', '').replace('\r', '')
            s = s + index
        return s
