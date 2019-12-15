import scrapy

from net.scrapy_patch_job.scrapy_patch_job.items import ScrapyPatchJobItem
from scrapy_splash import SplashRequest


class JobSpider(scrapy.Spider):
    name = "ZhiLianZhaoPin" #必需定义，名字，这个spider的标识
    allowed_domains = ["zhaopin.com"]
    start_urls = [
        "http://www.zhaopin.com"
        ,"http://sou.zhaopin.com/jobs/searchresult.ashx?jl=北京"
        # ,"http://sou.zhaopin.com/jobs/searchresult.ashx?jl=北京&kw=文员&sm=0&p=1"
    ] #必需定义，一个url列表，spider从这些网页开始抓取

    def start_requests(self):
        for i in range(10):
            # url="http://sou.zhaopin.com/jobs/searchresult.ashx?jl=北京&kw=Android Framework&sm=0&p=%d"%(i)
            url="http://sou.zhaopin.com/jobs/searchresult.ashx?pageSize=60&jl=北京&kw=文员&kt=3&p=%d"%(i)
            print('start_requests: current i=%d, url=%s'%(i, url))
            yield SplashRequest(url)
            break

    # 必需定义，解析返回结果的信息\
    def parse(self, response): #必需定义，解析返回结果的信息
        #tables = response.xpath('.//div[@id="listContent"]')
        tables = response.xpath('.//div[@class = "contentpile"]')
        print('parse():response=',tables.extract())
        for table in tables:
            detailLink=table.xpath('.//div[@class="infoBox"]/div[@class="itemBox nameBox"]/div[@class="jobName"]/a/@href').extract()
            if len(detailLink)>0:
                print("request detail Link=", detailLink[0])
                yield scrapy.Request(detailLink[0], callback=self.parse_item)
                break

    def parse_item(self, response):
        item = ScrapyPatchJobItem()
        print("cur table=%s"%(response.extract()))
        item["title"] = response.xpath('.//div[@class="inner-left fl"]/h1/text()').extract()[0].strip()
        item["company"] = response.xpath('.//div[@class="inner-left fl"]/h2/a/text()').extract()[0].strip()
        xpath_company_detail_li = response.xpath('.//div[@class="terminalpage-right"]/div[@class="company-box"]/ul[@class="terminal-ul clearfix terminal-company mt20"]/li')
        xpath_company_detail_value = xpath_company_detail_li.xpath('.//strong/text()').extract()
        xpath_company_detail_key = xpath_company_detail_li.xpath('.//span/text()').extract()
        index_value=0
        for index_key in range(len(xpath_company_detail_key)):
            key=xpath_company_detail_key[index_key]
            value=xpath_company_detail_value[index_value]
            if "规模" in key:
                item["company_detail_size"] = value.strip()
            elif "性质" in key:
                item["company_detail_nature"]=value.strip()
            elif "地址" in key:
                item["company_detail_address"] = value.strip()
            elif "行业" in key:
                index_value-=1
            elif "主页" in key:
                index_value-=1
            index_value+=1


        item["money"] = response.xpath('.//div[@class="terminalpage-left"]/ul/li/strong/text()').extract()[0].strip()
        item["city"] = response.xpath('.//div[@class="terminalpage-left"]/ul/li/strong/a/text()').extract()[0].strip()
        item["treatment"] = response.xpath('.//div[@class="inner-left fl"]/div[@class="welfare-tab-box"]/span/text()').extract()
        item["publishTime"] = response.xpath('.//div[@class="terminalpage-left"]/ul/li/strong/span/text()').extract()[0].strip()
        try:
            item["location"] = response.xpath('.//div[@class="terminalpage-left"]/div[@class="terminalpage-main clearfix"]/div[@class="tab-cont-box"]/div[@class="tab-inner-cont"]/h2/text()').extract()[0].strip()
        except IndexError:
            item["location"] = item["city"]
        item["detailLink"] = response.xpath('/html/head/link[@rel="canonical"]/@href').extract()[0].strip()
        item["description"] = response.xpath('.//div[@class="terminalpage-left"]/div[@class="terminalpage-main clearfix"]/div[@class="tab-cont-box"]/div[@class="tab-inner-cont"]/p/text()').extract()
        item["description"] = self.list2Str(list=item["description"]).strip().replace('\r','').replace('\n','').replace('\t','')
        item["treatment"] = self.list2Str(list=item["treatment"], splite="；").strip()
        # print("item=", item)
        yield item


    def list2Str(self, list, splite=""):
        desc = ""
        for str in list:
            desc += str+splite
        return desc

