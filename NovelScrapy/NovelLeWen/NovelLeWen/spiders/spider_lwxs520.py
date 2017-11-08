import re

import scrapy
from scrapy import Request

from NovelScrapy.NovelLeWen.NovelLeWen.books.books_setting import BooksSetting
from SpiderLearn.item import NovelItem


class NovelShiZhangFuRen(scrapy.spiders.Spider):
    name = "NovelLWXS520"
    start_urls = [
        BooksSetting.getHtml()
    ]
    def __init__(self):
        # self.headLink="http://www.lwxiaoshuo.com"
        # self.web_head=BooksSetting.getHtml()
        # self.web_last=".html"
        pass

    def parse(self, response):
        # self.print_response(response)
        list=response.xpath('//div[@id="defaulthtml4"]/table/tbody/tr/td/div[@class="dccss"]')
        print("list=", list.extract())
        link = list.xpath('./a/@href').extract()
        index = list.xpath('./a/text()').extract()
        for item in range(len(link)):
            print("index=%s, link=%s" % (index[item], link[item]))
            yield Request(self.start_urls[0] + link[item], method="GET", callback=self.parse_item)
            # break

    def parse_item(self, response):
        # self.print_response(response)
        xpath_main = response.xpath('//table[@class="border_l_r"]/tbody/tr/td/div')
        item = NovelItem()
        item['name'] = xpath_main.xpath('./h2/text()').extract()[0]
        item['author'] = xpath_main.xpath('./div[@class="border_b"]/text()').extract()[0]
        item['title'] = xpath_main.xpath('./h1/text()').extract()[0]
        item['chapter'] = re.findall(BooksSetting.getHeadHtmlReg(), response.url)[0]
        item['content'] = self.list2str(xpath_main.xpath('./table/tbody/tr/td/div/p/text()').extract())
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
