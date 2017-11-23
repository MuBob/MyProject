import numpy
import scrapy as scrapy

from search_people.MySetting import MySetting
from search_sina.utils.HtmlManager import HtmlManager


class SinaSpider(scrapy.Spider):
    name="SinaSpider"
    start_urls = [
        HtmlManager.getSinaUrl()
    ]
    def __init__(self):
        self.sets=MySetting()
        self.url=self.start_urls[0]+"%s&page=%d";

    def start_requests(self):
        url = self.url % (self.sets.getKeyWord(), 1)
        print('start_requests: url=', url)
        yield scrapy.Request(url)


    def parse(self, response): #必需定义，解析返回结果的信息
        print('response=', response)
        xpath_lsit=response.xpath('.//div[@class="S_plc"]')
        print('listSize=',len(xpath_lsit))