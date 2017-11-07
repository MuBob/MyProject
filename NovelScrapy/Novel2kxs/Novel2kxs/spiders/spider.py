import re

import scrapy
from scrapy import Request

from NovelScrapy.Novel2kxs.Novel2kxs.books.books_setting import BooksSetting
from SpiderLearn.item import NovelItem


class NovelYanYang(scrapy.spiders.Spider):
    name = "Novel2KXS"
    start_urls = [
        BooksSetting.getHtml()
    ]
    def __init__(self):
        # self.headLink="http://www.2kxs.com/xiaoshuo/66/66675/";
        pass

    def parse(self, response):
        # self.print_response(response)
        list=response.xpath('//dl[@class="book"]/dd')
        # print("list=", list.extract())
        link = list.xpath('./a/@href').extract()
        index = list.xpath('./a/text()').extract()
        for item in range(len(link)):
            # print("index=%s, link=%s" % (index[item], link[item]))
            yield Request(self.start_urls[0] + link[item], method="GET", callback=self.parse_item)

    def parse_item(self, response):
        # self.print_response(response)
        xpath_main = response.xpath('//div[@id="box"]')
        item = NovelItem()
        item['name'] = xpath_main.xpath('./p[@class="Text"]/a/text()').extract()[0]
        item['author'] = xpath_main.xpath('./p[@class="summary"]/a/text()').extract()[0]
        item['title'] = xpath_main.xpath('./h2/text()').extract()[0]
        item['chapter'] = re.findall(BooksSetting.getHeadHtmlReg(), response.url)[0]
        item['content'] = self.list2str(xpath_main.xpath('./p[@class="Text"]/text()').extract())
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
