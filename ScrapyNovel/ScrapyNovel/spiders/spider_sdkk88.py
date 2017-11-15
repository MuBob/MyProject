# -*- coding:utf-8 -*-
import re

import scrapy
from scrapy import Request

from ScrapyNovel.items import ScrapynovelItem
from ScrapyNovel.books.books_setting import BooksSetting
from ScrapyNovel.books.spider_types import SpiderTypes


class NovelSpider1(scrapy.spiders.Spider):
    name = SpiderTypes.getTypeName_SDKK88()
    # name = "NovelSDKK88"
    start_urls = [
        BooksSetting.getHtml()
    ]
    def __init__(self):
        self.headLink="http://www.sbkk88.com"
        self.author=""

    def parse(self, response):
        # self.print_response(response)
        list=response.xpath('//div[@class="mingzhuMain"]/div[@class="mingzhuLeft"]/ul[@class="leftList"]/li')
        extract_author = response.xpath(
            '//div[@class="mingzhuMain"]/div[@class="mingzhuLeft"]/div[@class="mingzhuTitle"]/h1/text()').extract()[0]
        find_author = re.findall(".*：(.*)", extract_author)[0]
        if len(find_author)>0:
            self.author=find_author
        else:
            self.author=extract_author
        print("list=", list.extract())
        for item in list:
            link=item.xpath('./a/@href').extract()[0]
            index=item.xpath('./a/text()').extract()[0]
            print("index=%s, link=%s"%(index, link))
            yield Request(self.headLink+link, method="GET", callback=self.parse_item)
            # break

    def parse_item(self, response):
        # self.print_response(response)
        item = ScrapynovelItem()
        item['name'] = BooksSetting.getNovelName()
        item['author'] = self.author
        item['title'] = response.xpath('//div[@id="f_title1"]/h1/text()').extract()[0]
        count = re.findall(BooksSetting.getHeadHtmlReg(), response.url)[0]
        item['chapter'] =count
        item['content'] = self.list2str(response.xpath('//div[@id="f_content1"]/div[@id="f_article"]/p/text()').extract())
        print("item=", item)
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
