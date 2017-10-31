# -*- coding:utf-8 -*-
import re

import scrapy
from scrapy import Request

from NovelScrapy.NovelMaoPu.NovelMaoPu.items import NovelmaopuItem
from NovelScrapy.NovelMaoPu.NovelMaoPu.maopu_setting import MaoPuSetting


class NovelSpider(scrapy.spiders.Spider):
    name = "NovelMaoPu"
    start_urls = [
        MaoPuSetting.getHtml()
    ]
    def __init__(self):
        self.headLink=self.start_urls[0]

    def parse(self, response):
        # self.print_response(response)
        list=response.xpath('//div[@class="mu_contain"]/ul[@class="mulu_list"]/li')
        # print("list=", list.extract())
        for item in list:
            link=item.xpath('./a/@href').extract()[0]
            # index=re.findall("(.*).html", link)[0]
            print("link=%s"%(self.headLink+link))
            yield Request(self.headLink+link, method="GET", callback=self.parse_item)
            # break

    def parse_item(self, response):
        # self.print_response(response)
        xpath_main = response.xpath('//div[@id="content"]')
        item = NovelmaopuItem()
        item['title'] = xpath_main.xpath('./h1/text()').extract()[0]
        item['name'] =item['title']
        item['author'] = item['title']
        count = re.findall(MaoPuSetting.getHeadHtmlReg(), response.url)[0]
        if len(count)<=1:
            count='0'+count
        item['chapter'] =count
        item['content'] = self.list2str(xpath_main.xpath('./div[@class="chapter-content"]/text()').extract())
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
