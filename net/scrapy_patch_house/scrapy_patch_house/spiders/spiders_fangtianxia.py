import scrapy

from net.scrapy_patch_house.scrapy_patch_house.items import ScrapyPatchHouseItem
from net.scrapy_patch_house.scrapy_patch_house.setting.html_setting import HtmlSetting
from net.util.str_util import StrUtil


class Fang58Spider(scrapy.Spider):
    name = "FangTianXiaSpider" #必需定义，名字，这个spider的标识
    start_urls = [
        "http://zu.fang.com/"
    ] #必需定义，一个url列表，spider从这些网页开始抓取

    def start_requests(self):
        for i in range(HtmlSetting.getPageCount()):
            url=HtmlSetting.getFangTXUrlFormat()%(i+1)
            print('start_requests: current i=%d, url=%s'%(i, url))
            yield scrapy.Request(url)
            break

    def parse(self, response): #必需定义，解析返回结果的信息
        tables = response.xpath('//div[@id="houselistbody"]/div[@id="listBox"]/div[@class="houseList"]/dl[@class="list hiddenMap rel"]/dd[@class="info rel"]')
        print('parse():response=',len(tables))
        for table in tables:
            detailLink=table.xpath('.//p[@class="title"]/a/@href').extract()
            if len(detailLink)>0:
                detail_link = self.start_urls[0]+detailLink[0]
                print("request detail Link=", detail_link)
                yield scrapy.Request(detail_link, callback=self.parse_item)
                break

    def parse_item(self, response):
        item = ScrapyPatchHouseItem()
        try:
            xpath_main = response.xpath('//div[@class="tab-cont clearfix"]')
            item["detailLink"] = str(response)
            item["title"] = xpath_main.xpath('.//div[@class="title"]/text()').extract()[0]
            xpath_money = xpath_main.xpath(
                './/div[@class="tab-cont-right"]/div[@class="tr-line clearfix zf_new_title"]/div[@class="trl-item sty1"]')
            item["rentMoney"] = xpath_money.xpath('./i/text()').extract()[0]
            item["rentType"] = xpath_money.xpath('./text()').extract()[0]
            xpath_list = xpath_main.xpath('.//div[@class="tab-cont-right"]/div[@class="tr-line clearfix"]/div')
            item["lease"] = xpath_list[0].xpath('./div[@class="tt"]/text()').extract()[0].strip()
            item["types"] = xpath_list[1].xpath('./div[@class="tt"]/text()').extract()[0].strip()
            item["area"] = xpath_list[2].xpath('./div[@class="tt"]/text()').extract()[0].strip()
            item["floor"] = xpath_list[3].xpath('./div[@class="tt"]/text()').extract()[0].strip() \
                            + ";" \
                            + xpath_list[4].xpath('./div[@class="tt"]/text()').extract()[0].strip()
            xpath_address_list = xpath_main.xpath(
                './/div[@class="tab-cont-right"]/div[@class="tr-line"]/div[@class="trl-item2 clearfix"]')
            item["residential"] = StrUtil.list2Str(
                xpath_address_list[0].xpath('./div[@class="rcont"]/a/text()').extract(), ";")
            len_address_list = len(xpath_address_list)
            item["address"] = StrUtil.list2Str(
                xpath_address_list[len_address_list - 1].xpath('./div[@class="rcont"]/a/text()').extract(), ";")

            xpath_contactor = xpath_list.xpath('./div[@class="tjcont-list clearfix"]/div[@class="tjcont-list-c "]')
            item["contactor"] = \
                xpath_contactor.xpath(
                    './div[@class="tjcont-list-cline1 "]/span[@class="zf_jjname"]/a/text()').extract()[0]
            item["phone"] = xpath_main.xpath('.//div[@class="tjcont-list-cline3 font16"]/text()').extract()[0]
            xpath_description = xpath_main.xpath(
                './/div[@class="content-item fydes-item"]//div[@class="fyms_con floatl gray3"]')
            item["description"] = StrUtil.list2Str(xpath_description.xpath('./br/text()').extract(), "")
        except:
            print("Exception occur! response=", response.__str__())


        yield item




