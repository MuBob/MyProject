import numpy
import scrapy as scrapy

from search_people.MySetting import MySetting


class SinaSpider(scrapy.Spider):
    name="SinaSpider"
    start_urls = [
        "http://s.weibo.com/"
    ]
    def __init__(self):
        self.sets=MySetting()
        self.url="http://s.weibo.com/user/%s&Refer=weibo_user&c=spr_sinamkt_buy_hyww_weibo_t%d";

    def start_requests(self):
        url = self.url % (self.sets.getKeyWord(), 105)
        print('start_requests: url=', url)
        yield scrapy.Request(url)


    def parse(self, response): #必需定义，解析返回结果的信息
        print('response=', response)
        print("response main=", response.xpath('//body').extract())
        xpath_lsit=response.xpath('//body').extract()
        print('listSize=',len(xpath_lsit))