# -*- coding:utf-8 -*-
import re

import scrapy
from scrapy import Request

from NovelScrapy.NovelJJWXC.NovelJJWXC.book.books_setting import BooksSetting
from NovelScrapy.NovelJJWXC.NovelJJWXC.items import NoveljjwxcItem


class NovelSpider1(scrapy.spiders.Spider):
    name = "NovelJinJiangWenXueWang"
    start_urls = [
        BooksSetting.getHtml()
    ]
    def __init__(self):
        # self.headLink="http://www.jjwxc.net/onebook.php";
        pass

    def parse(self, response):
        # self.print_response(response)
        list=response.xpath('//table[@class="cytable"]/tbody/tr[@itemprop="chapter"]')
        # print("list=", list.extract())
        for item in list:
            link=item.xpath('./td/span[@itemprop="headline"]/div[@style="float:left"]/a/@href').extract()[0]
            index=item.xpath('./td/span[@itemprop="headline"]/div[@style="float:left"]/a/text()').extract()[0]
            print("index=%s, link=%s"%(index, link))
            yield Request(link, method="GET", callback=self.parse_item)
            # break

    def parse_item(self, response):
        # self.print_response(response)
        xpath_main = response.xpath('//table[@id="oneboolt"]')
        item = NoveljjwxcItem()
        item['name'] = xpath_main.xpath('.//td[@class="noveltitle"]/h1/a/span/text()').extract()[0].strip().replace('  ', '').replace('\r', '').replace('\n', '').replace('\t', '')
        print('name=',item['name'])
        item['author'] = xpath_main.xpath('.//td[@class="noveltitle"]/a/text()').extract()[0]
        item['title'] = xpath_main.xpath('.//div[@class="noveltext"]/div')[1].xpath('./h2/text()').extract()[0]
        count = re.findall(BooksSetting.getHeadHtmlReg(), response.url)[0]
        if len(count)<=1:
            count='0'+count
        item['chapter'] =count
        item['content'] = self.list2str(xpath_main.xpath('.//div[@class="noveltext"]/text()').extract())
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
