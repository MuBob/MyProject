# -*- coding:utf-8 -*-
import re

import scrapy
from scrapy import Request

from ScrapyNovel.books.books_setting import BooksSetting
from ScrapyNovel.items import ScrapynovelItem

from ScrapyNovel.books.spider_types import SpiderTypes


class NovelSpider1(scrapy.spiders.Spider):
    # name = "NovelWenXueM"
    name = SpiderTypes.getTypeName_XS74()
    start_urls = [
        BooksSetting.getHtml()
    ]
    item_author=""
    item_name=""
    def __init__(self):
        # self.headLink="https://www.xs74.com/novel/taweianyeersheng/";
        pass

    def parse(self, response):
        # self.print_response(response)
        list=response.xpath('//div[@class="box_con"]/div[@id="list"]/dl/dd')
        info=response.xpath('//div[@class="box_con"]/div[@id="maininfo"]/div[@id="info"]')
        global item_name
        item_name=info.xpath('./h1/text()').extract()[0]
        global item_author
        item_author=info.xpath('./p/text()').extract()[0]
        # print("list=", list.extract())
        for item in list:
            link=item.xpath('./a/@href').extract()[0]
            index = item.xpath('./a/text()').extract()[0]
            print("index=%s, link=%s"%(index, link))
            yield Request(link, method="GET", callback=self.parse_item)
            # break

    def parse_item(self, response):
        # self.print_response(response)
        xpath_main = response.xpath('//div[@class="content_read"]/div[@id="box_con"]')
        item = ScrapynovelItem()
        item['name'] = item_name
        print('name=',item['name'])
        item['author'] = item_author
        item['title'] = xpath_main.xpath('.//div[@class="bookname"]/h1/text()').extract()[0].strip().replace('  ', '').replace('\r', '').replace('\n', '').replace('\t', '')
        count = re.findall(BooksSetting.getHeadHtmlReg(), response.url)[0]
        if len(count)<=1:
            count='0'+count
        item['chapter'] =count
        item['content'] = self.list2str(xpath_main.xpath('.//div[@id="content"]/text()').extract())
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
