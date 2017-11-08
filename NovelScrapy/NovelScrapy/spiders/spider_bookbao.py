# -*- coding:utf-8 -*-
import re

import scrapy
from scrapy import Request

from NovelScrapy.NovelScrapy.spiders.spider_types import SpiderTypes
from NovelScrapy.ScrapyBookbao.ScrapyBookbao.boobbao_setting import BookbaoSetting


class NovelSpider1(scrapy.spiders.Spider):
    name = SpiderTypes.getTypeName_BookBao()
    start_urls = [
        BookbaoSetting.getHtml()
    ]
    def __init__(self):
        self.headLink="https://www.bookbao8.com";

    def parse(self, response):
        # self.print_response(response)
        list=response.xpath('//div[@class="wp b2 info_chapterlist"]/ul/li')
        print("list=", list.extract())
        for item in list:
            link=item.xpath('./a/@href').extract()[0]
            index=item.xpath('./a/text()').extract()[0]
            # print("index=%s, link=%s"%(index, link))
            yield Request(self.headLink+link, method="GET", callback=self.parse_item)
            # break

    def parse_item(self, response):
        # self.print_response(response)
        xpath_main = response.xpath('//div[@class="bdsub"]/dl')
        item = NovelItem()
        item['name'] = xpath_main.xpath('./dd')[0].xpath('./h1/a/text()').extract()[0]
        item['author'] = xpath_main.xpath('./dd')[1].xpath('./h3/text()').extract()[0]
        item['title'] = xpath_main.xpath('./dd')[0].xpath('./h1/text()').extract()[0]
        count = re.findall(BookbaoSetting.getHeadHtmlReg(), response.url)[0]
        if len(count)<=1:
            count='0'+count
        item['chapter'] =count
        item['content'] = self.list2str(xpath_main.xpath('./dd[@id="contents"]/text()').extract())
        # print("item=", item)
        yield item


    def print_response(self, response):
        current_url = response.url  # 爬取时请求的url
        body = response.body  # 返回的html
        print("request=%s, response=%s" % (current_url, body))

    def list2str(self, list):
        s=""
        for index in list:
            # print('index=',index)
            index.replace('\u3000','').replace('\r','')
            s=s+index
        return s
