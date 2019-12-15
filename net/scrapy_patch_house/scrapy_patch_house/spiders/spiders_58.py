import scrapy

from net.scrapy_patch_house.scrapy_patch_house.items import ScrapyPatchHouseItem
from net.scrapy_patch_house.scrapy_patch_house.setting.html_setting import HtmlSetting
from net.util.str_util import StrUtil


class Fang58Spider(scrapy.Spider):
    name = "Fang58Spider" #必需定义，名字，这个spider的标识
    start_urls = [
        "http://bj.58.com/chuzu/"
    ] #必需定义，一个url列表，spider从这些网页开始抓取

    def start_requests(self):
        for i in range(HtmlSetting.getPageCount()):
            # url="http://sou.zhaopin.com/jobs/searchresult.ashx?jl=北京&kw=Android&sg=4a10f88d651f4219819604a1f028639a&sm=0&p=%d"%(i)
            url=HtmlSetting.getRequestUrlFormat()%(i+1)
            print('start_requests: current i=%d, url=%s'%(i, url))
            yield scrapy.Request(url)

    def parse(self, response): #必需定义，解析返回结果的信息
        tables = response.xpath('//ul[@class="listUl"]/li')
        print('parse():response=',len(tables))
        for table in tables:
            detailLink=table.xpath('.//div[@class="des"]/h2/a/@href').extract()
            if len(detailLink)>0:
                print("request detail Link=", detailLink[0])
                yield scrapy.Request(detailLink[0], callback=self.parse_item)
                # break

    def parse_item(self, response):
        item = ScrapyPatchHouseItem()
        try:
            xpath_main = response.xpath('//div[@class="main-wrap"]')
            item["detailLink"] = str(response)
            item["title"] = xpath_main.xpath('.//div[@class="house-title"]/h1/text()').extract()[0]
            xpath_money = xpath_main.xpath(
                './/div[@class="house-basic-info"]/div[@class="house-basic-right fr"]/div[@class="house-basic-desc"]/div[@class="house-desc-item fl c_333"]/div[@class="house-pay-way f16"]/span[@class="c_ff552e"]//text()').extract()
            item["rentMoney"] = xpath_money[0] + xpath_money[1]
            item["rentType"] = xpath_main.xpath(
                './/div[@class="house-basic-info"]/div[@class="house-basic-right fr"]/div[@class="house-basic-desc"]/div[@class="house-desc-item fl c_333"]/div[@class="house-pay-way f16"]/span[@class="c_333"]/text()').extract()[
                0]
            xpath_list = xpath_main.xpath(
                './/div[@class="house-basic-info"]/div[@class="house-basic-right fr"]/div[@class="house-basic-desc"]/div[@class="house-desc-item fl c_333"]/ul[@class="f14"]//li')
            item["lease"] = xpath_list[0].xpath('.//span/text()').extract()[1].strip()
            item["types"] = xpath_list[1].xpath('.//span/text()').extract()[1].strip().replace('  ', '').replace('\r',
                                                                                                                 '').replace(
                '\n', '').replace('\t', '').replace('\xa0', '')
            item["floor"] = xpath_list[2].xpath('.//span/text()').extract()[1].strip().replace('\r', '').replace('\n',
                                                                                                                 '').replace(
                '\t', '').replace('\xa0', '')
            item["residential"] = StrUtil.list2Str(xpath_list[3].xpath('.//span/a/text()').extract(), ";")
            # item["area"] = xpath_list[4].xpath('.//span/a[@class="c_333 ah"]/text()').extract()
            item["area"] = xpath_list[4].xpath('string(.)').extract()[0].replace('所属区域：', '').strip().replace('\r',
                                                                                                              '').replace(
                '\n', '').replace('\t', '').replace('\xa0', '').replace('  ', '')
            add_list = xpath_list[5].xpath('.//span[@class="dz"]/text()').extract()
            item["address"] = StrUtil.list2Str(add_list, "")
            xpath_contactor = xpath_main.xpath(
                './/div[@class="house-basic-info"]/div[@class="house-basic-right fr"]/div[@class="house-basic-desc"]/div[@class="house-agent-info fr"]')
            item["contactor"] = xpath_contactor.xpath('.//p[@class="agent-name f16 pr"]/a/text()').extract()[0] + \
                                xpath_contactor.xpath('.//p[@class="agent-subgroup f12"]/text()').extract()[0]
            item["phone"] = xpath_main.xpath(
                './/div[@class="house-basic-info"]/div[@class="house-basic-right fr"]/div[@class="house-fraud-tip"]/div[@class="house-chat-phone"]/span[@class="house-chat-txt"]/text()').extract()[
                0]
            xpath_description = xpath_main.xpath('.//div[@class="house-detail-desc"]//ul[@class="introduce-item"]')
            item["description"] = StrUtil.list2Str(
                xpath_description.xpath('.//span[@class="a2"]').xpath('string(.)').extract(), "")
        except:
            print("Exception occur! response=", response.__str__())


        yield item




