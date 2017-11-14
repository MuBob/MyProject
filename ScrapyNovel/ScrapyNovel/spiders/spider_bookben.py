# -*- coding:utf-8 -*-
import re

import scrapy
from scrapy import Request

from ScrapyNovel.books.books_setting import BooksSetting
from ScrapyNovel.books.spider_types import SpiderTypes
from ScrapyNovel.items import ScrapynovelItem


class NovelSpider(scrapy.spiders.Spider):
    name=SpiderTypes.getTypeName_BookBen()
    # name = "NovelBookben"
    start_urls = [
        BooksSetting.getHtml()
    ]
    def __init__(self):
        self.headLine="http://www.bookben.com"
        pass

    def parse(self, response):
        # self.print_response(response)
        list=response.xpath('//div[@class="nylr"]/div[@class="info_views"]/ul/li[@class="n"]')
        # print("list=", list.extract())
        for item in list:
            link=item.xpath('./a/@href').extract()[0]
            index=item.xpath('./a/text()').extract()[0]
            print("index=%s, link=%s"%(index, link))
            yield Request(self.headLine+link, method="GET", callback=self.parse_item)
            # break

    def parse_item(self, response):
        # self.print_response(response)
        item = ScrapynovelItem()
        item['name'] = BooksSetting.getNovelName()
        # print('name=',item['name'])
        info = response.xpath('//div[@class="view_info"]/text()').extract()[0]
        item['author'] = re.findall(".*作者:(.*)章节列表.*",info)[0].strip().replace(' ', '')
        item['title'] = response.xpath('//div[@class="view_t"]/text()').extract()[0].strip().replace('  ', '').replace('\r', '').replace('\n', '').replace('\t', '')
        count = re.findall(BooksSetting.getHeadHtmlReg(), response.url)[0]
        if len(count)<=1:
            count='0'+count
        item['chapter'] =count
        item['content'] = self.list2str(response.xpath('//div[@class="view_content"]/div[@id="view_content_txt"]/p/text()').extract())
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
