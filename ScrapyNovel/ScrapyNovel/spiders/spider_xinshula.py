import re

import scrapy
from scrapy import Request

from ScrapyNovel.items import ScrapynovelItem
from ScrapyNovel.books.books_setting import BooksSetting
from ScrapyNovel.books.spider_types import SpiderTypes


class NovelXinShuLa(scrapy.spiders.Spider):
    name= SpiderTypes.getTypeName_XinShuLa()
    start_urls = [
        BooksSetting.getHtml()
    ]
    def __init__(self):
        self.headLink=BooksSetting.getHtml()
        pass

    def parse(self, response):
        # self.print_response(response)
        list=response.xpath('//div[@class="bookcontent"]/dl/dd')
        # print("list=", list.extract())
        link = list.xpath('./a/@href').extract()
        index = list.xpath('./a/text()').extract()
        for item in range(len(link)):
            # print("index=%s, link=%s" % (index[item], self.start_urls[0] + link[item]))
            yield Request(self.start_urls[0] + link[item], method="GET", callback=self.parse_item)

    def parse_item(self, response):
        self.print_response(response)
        xpath_main = response.xpath('//body[@id="bgdiv"]')
        item = ScrapynovelItem()
        item['name'] = xpath_main.xpath('./div[@class="top"]/div[@class="top_left"]/a/strong/text()').extract()[0]
        item['author'] = xpath_main.xpath('./div[@class="top"]/div[@class="top_left"]/a/text()').extract()[2]
        item['title'] = xpath_main.xpath('./div[@class="chapter_title"]/h1/text()').extract()[0]
        item['chapter'] = re.findall(BooksSetting.getHeadHtmlReg(), response.url)[0]
        item['content'] = self.list2str(xpath_main.xpath('./div[@id="content"]/text()').extract())
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
            index.replace('\u3000','').replace('\r','').replace('\xa0','')
            s=s+index
        return s
