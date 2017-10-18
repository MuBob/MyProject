# -*- coding:utf-8 -*-
import scrapy
import re
from scrapy import Request
from NovelSangWu.items import NovelsangwuItem
class NovelSangWu(scrapy.spiders.Spider):
    name = "NovelSangWu"
    start_urls = [
        "http://www.sangwu.org/book/5/5952/"
    ]
    def __init__(self):
        self.headLink="http://www.sangwu.org/book/5/5952/";

    def parse(self, response):
        self.print_response(response)
        list=response.xpath('//dd')
        print("list=", list.extract())
        link = list.xpath('./a/@href').extract()
        index = list.xpath('./a/text()').extract()
        for item in range(len(link)):
            if "第" in index[item]:
                # print("index=%s, link=%s" % (index[item], link[item]))
                yield Request(self.headLink + link[item], method="GET", callback=self.parse_item)

    def parse_item(self, response):
        self.print_response(response)
        xpath_main = response.xpath('//div[@class="readmain"]')
        # print("main=", xpath_main.extract())
        item = NovelsangwuItem()
        item['name'] = xpath_main.xpath('./div[@class="bookname"]/h2/text()').extract()[0]
        item['author'] = xpath_main.xpath('./div[@class="bookname"]/h2/text()').extract()[0]
        item['title'] = xpath_main.xpath('./div[@class="bookname"]/h1/text()').extract()[0]
        item['chapter'] = re.findall(".*" + self.headLink + "(.*).htm.*", response.url)
        item['content'] = self.list2str(xpath_main.xpath('./div[@class="centent"]/text()').extract())
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
            index.replace('\u3000','').replace('\r','').replace('\xa0','')
            s=s+index
        return s
