import re

import scrapy
from scrapy import Request

from SpiderLearn.item import NovelItem


class NovelShiZhangFuRen(scrapy.spiders.Spider):
    name = "NovelShiZhangFuRen"
    start_urls = [
        "http://www.lwxiaoshuo.com/20/20621/.html"
    ]
    def __init__(self):
        self.headLink="http://www.lwxiaoshuo.com"
        self.web_head="http://www.lwxiaoshuo.com/20/20621/"
        self.web_last=".html"

    def parse(self, response):
        # self.print_response(response)
        list=response.xpath('//table[@style="MARGIN-BOTTOM: 10px"]/tbody')
        # print("list=", list.extract())
        link = list.xpath('.//tr/td/div[@class="dccss"]/a/@href').extract()
        index = list.xpath('.//tr/td/div[@class="dccss"]/a/text()').extract()
        for item in range(len(link)):
            if "第" in index[item]:
                print("index=%s, link=%s" % (index[item], link[item]))
                yield Request(self.headLink + link[item], method="GET", callback=self.parse_item)
                # break

    def parse_item(self, response):
        # self.print_response(response)
        xpath_main = response.xpath('//table[@class="border_l_r"]/tbody/tr/td')
        item = NovelItem()
        item['name'] = xpath_main.xpath('./div/h1/text()').extract()[0]
        item['author'] = xpath_main.xpath('./div/div[@class="border_b"]/text()').extract()[0]
        item['title'] = xpath_main.xpath('./div/h2/text()').extract()[0]
        item['chapter'] = re.findall(".*"+self.web_head+"(.*)"+self.web_last+".*", response.url)[0]
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
