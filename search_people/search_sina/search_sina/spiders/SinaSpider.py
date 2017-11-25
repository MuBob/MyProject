import scrapy as scrapy

from scrapy_splash import SplashRequest
from search_people.MySetting import MySetting
from search_people.search_sina.search_sina.utils.HtmlManager import HtmlManager


class SinaSpider(scrapy.Spider):
    name="SinaSpider"
    start_urls = [
        HtmlManager.getSinaUrl()
    ]
    def __init__(self):
        self.url=self.start_urls[0]+"%s&Refer=weibo_user&c=spr_sinamkt_buy_hyww_weibo_t%d"

    def start_requests(self):
        url = self.url % (HtmlManager.getSearchName(), 1)
        # url=self.start_urls[0]
        print('start_requests: url=', url)
        yield SplashRequest(url, self.parse, args={'wait': 1})


    def parse(self, response): #必需定义，解析返回结果的信息
        print('response=', response)
        #.//div[@id="pl_user_feedList"]/div[@class="WB_cardwrap S_bg2"]/div[@class="search_feed"]/div[@class="person_list_feed clearfix"]/div[@class="pl_personlist"]
        xpath_lsit = response.xpath('.//div[@class="list_person clearfix"]')
        print('xpath_extract=', xpath_lsit.extract())
        print('listSize=',len(xpath_lsit))