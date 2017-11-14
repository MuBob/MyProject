# -*- coding:utf-8 -*-
import re

import scrapy
from ScrapyNovel.items import ScrapynovelItem
from scrapy import Request

from ScrapyNovel.books.books_setting import BooksSetting
from ScrapyNovel.books.spider_types import SpiderTypes


class NovelSpider1(scrapy.spiders.Spider):
    name = SpiderTypes.getTypeName_YueDu163()
    # name = "NovelYueDu163"
    start_urls = [
        BooksSetting.getHtml()
    ]
    def __init__(self):
        self.headLink="http://yuedu.163.com"
        self.author=""
        self.name=""

    def parse(self, response):
        self.print_response(response)
        xpath_main=response.xpath('//div[@class="g-mn"]')
        self.author=xpath_main.xpath('./div[@class="m-bookdetail"]/div[@class="f-fl"]/h3/span/a/text()').extract()[0]
        self.name=xpath_main.xpath('./div[@class="m-bookdetail"]/div[@class="f-fl"]/h3/@title').extract()[0]
        # list=xpath_main.xpath('./div[@class="m-directory m-directory-bookdetail"]/div[@class="directory j-directory-wrap"]/ul/li')
        list = xpath_main.xpath('./div/div/ul')
        print("list=", list.extract())
        for item in list:
            link=item.xpath('./a/@href').extract()[0]
            index=item.xpath('./a/text()').extract()[0]
            # print("index=%s, link=%s"%(index, link))
            yield Request(self.headLink+link, method="GET", callback=self.parse_item)
            break

    def parse_item(self, response):
        # self.print_response(response)
        xpath_main = response.xpath('//div[@class="article J_Article"]/div[@class="portrait-page-box J_PortraitMoveBox"]/div[@class="article-content"]/div[@class="ne-content J_NEContent"]')
        item = ScrapynovelItem()
        item['name'] = self.name
        item['author'] = self.author
        item['title'] = xpath_main.xpath('./h1/text()').extract()[0]
        count = re.findall(BooksSetting.getHeadHtmlReg(), response.url)[0]
        if len(count)<=1:
            count='0'+count
        item['chapter'] =count
        item['content'] = self.list2str(xpath_main.xpath('./p/text()').extract())
        # print("item=", item)
        yield item


    def print_response(self, response):
        current_url = response.url  # 爬取时请求的url
        body = response.body  # 返回的html
        print("request=%s, response=%s" % (current_url, body))

    def list2str(self, list):
        s="/t"
        for index in list:
            # print('index=',index)
            index.replace('\u3000','').replace('\r','')
            s=s+index+"\n\t"
        return s
