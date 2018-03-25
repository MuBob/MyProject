import scrapy as scrapy
from PIL import Image

from scrapy_splash import SplashRequest
from search_people.MySetting import MySetting
from search_people.search_sina.search_sina.items import SearchSinaItem
from search_people.search_sina.search_sina.utils.HtmlManager import HtmlManager


class SinaSpider(scrapy.Spider):
    name="SinaSpider"
    start_urls = [
        HtmlManager.getSinaUrl(),
        HtmlManager.getSinaLoginUrl()
    ]
    def __init__(self):
        self.url=self.start_urls[0]+"%s& display = 0 & retcode = 6102 & page = %d"

    def start_requests(self):
        url = HtmlManager.getSinaLoginUrl()
        print('login url=', url)
        yield SplashRequest(url, self.parse_login, args={'wait': 5})

    def attempt_login(self):
        url=HtmlManager.getSinaLoginUrl()
        print('login url=', url)
        yield SplashRequest(url, self.parse_login, args={'wait': 5})

    def parse_login(self, response):
        print('response=', response)


    def attempt_search(self):
        for i in range(3):
            url = self.url % (HtmlManager.getSearchName(),i+1)
            # url=self.start_urls[0]
            print('start_requests: url=', url)
            yield SplashRequest(url, self.parse_search, args={'wait': 3})

    def parse_search(self, response): #必需定义，解析返回结果的信息
        print('response=', response)
        xpath_lsit = response.xpath('.//div[@id="pl_user_feedList"]/div[@class="WB_cardwrap S_bg2"]/div[@class="search_feed"]/div[@class="person_list_feed clearfix"]/div[@class="pl_personlist"]/div[@class="list_person clearfix"]')
        print('xpath_extract=', xpath_lsit.extract())
        print('listSize=',len(xpath_lsit))
        if(len(xpath_lsit)<=0):
            return
        for xpath_item in xpath_lsit:
            item=SearchSinaItem()
            xpath_detail=xpath_item.xpath('./div[@class="person_detail"]')
            item['name']=xpath_detail.xpath('./p[@class="person_name"]/a[@class="W_texta W_fb"]/@title').extract()[0]
            item['sex'] = xpath_detail.xpath('./p[@class="person_addr"]/span/@title').extract()[0]
            item['address'] = xpath_detail.xpath('./p[@class="person_addr"]/span/text()').extract()[0]
            item['detail_link']=xpath_detail.xpath('./p[@class="person_addr"]/a/@href').extract()[0]
            item['number_guan_zhu'] = xpath_detail.xpath('./p[@class="person_num"]/span/a/text()').extract()[0]
            item['number_fen_si'] = xpath_detail.xpath('./p[@class="person_num"]/span/a/text()').extract()[1]
            item['number_wei_bo'] = xpath_detail.xpath('./p[@class="person_num"]/span/a/text()').extract()[2]
            item['info'] = xpath_detail.xpath('./div[@class="person_info"]/p/text()')
            if len(item['info'])>0:
                item['info']=item['info'].extract()[0].strip().replace('\r', '').replace('\n', '').replace('\t', '')
            item['label'] = xpath_detail.xpath('./p[@class="person_label"]/text()')
            if len(item['label'])>0:
                item['label']=self.list2Str(item['label'].extract()).strip().replace('\r', '').replace('\n', '').replace('\t', '')
            yield item

    def list2Str(self, list, splite=""):
        desc = ""
        for str in list:
            desc += str+splite
        return desc

