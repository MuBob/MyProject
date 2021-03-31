import re

import scrapy
from scrapy import Request

from ScrapyTestFiles.items import ScrapytestfilesItem


class SpiderBase(scrapy.spiders.Spider):
    name = "TestFile"
    start_urls = [
        "https://www.examw.com/xinli/sanji_moniti/indexA6.html",
        "https://www.examw.com/xinli/sanji_moniti/indexA5.html",
        "https://www.examw.com/xinli/sanji_moniti/indexA4.html",
        "https://www.examw.com/xinli/sanji_moniti/indexA3.html",
        "https://www.examw.com/xinli/sanji_moniti/indexA2.html",
        "https://www.examw.com/xinli/sanji_moniti",
    ]
    def __init__(self):
        self.urls = self.start_urls
        pass

    def parse(self, response):
        self.print_response(response)
        list = self.getXpathList(response)
        for item in list:
            link = self.getStrItem_Link(item)
            print("link=", link)
            if link.startswith(self.getHtml()):
                link=link
            else:
                link=self.getHtml()+link
            if link=='': continue
            if self.urls.__contains__(link):
                continue
            else:
                yield scrapy.Request(link, method="GET", callback=self.parse_detail)
                # break

    def parse_detail(self, response):
        self.print_response(response)
        xpath_main = self.getXpathItem_Main(response)
        # print("xpath_main=", xpath_main.extract())
        item = ScrapytestfilesItem()

        item['link'] = response.url
        item['title'] = self.getStrItem_Title(xpath_main)
        item['content'] = self.list2str(self.getStrItem_Content(xpath_main))
        # item['content'] = self.getStrItem_Content(xpath_main)
        # print("item=", item)
        yield item

    def print_response(self, response):
        current_url = response.url  # 爬取时请求的url
        body = response.body  # 返回的html
        print("request=%s, response=%s" % (current_url, body))

    def list2str(self, list):
        s = ""
        answers=[]
        for index in list:
            # print('index=',index)
            # index=index.replace('\u3000', '').replace('\r', '')
            index=index.replace('\u3000\u3000', '\t')
            index =index.replace('\u3000', ' ')
            index =index.replace('\u2002', ' ')
            if index.find('答案')>=0:
                answers.append(index)
            else:
                s = s +'\r'+ index
        s = s + '\r\n\n'
        for answer in answers:
            s = s + '\t' + answer
        return s


    def getHtml(self):
        return "https://www.examw.com/"

    def getXpathList(self, response):
        return response.xpath('//div[@class="newsMain"]/ul[@class="publist newsList"]/li')

    def getStrItem_Link(self, item):
        lastLink=item.xpath('./a/@href').extract()[0]
        return lastLink

    def getXpathItem_Main(self, response):
        return response.xpath('//div[@class="clearfix inforBox"]/div[@class="newsLeft fl"]/div[@class="newsDetail"]')

    def getStrItem_Title(self, xpath_main):
        title = xpath_main.xpath('./div[@class="newsTitle"]/h1/h1/text()').extract()[0].strip().replace('  ', '').replace('\r', '').replace('\n', '').replace('\t', '')
        return title

    def getStrItem_Content(self, xpath_main):
        return xpath_main.xpath('./div[@class="newsbox"]/div[@class="newsCon"]/p/text()').extract()




