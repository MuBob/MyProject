# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyPatchHouseItem(scrapy.Item):
    # define the fields for your item here like:
    title=scrapy.Field() #标题
    rentMoney=scrapy.Field() #租金
    rentType=scrapy.Field() #租金支付周期
    lease = scrapy.Field() #租赁方式
    types = scrapy.Field()  #房屋类型
    floor=scrapy.Field() #朝向楼层
    residential=scrapy.Field() #住宅小区
    area=scrapy.Field() #所属区域
    address=scrapy.Field() #详细地址
    contactor=scrapy.Field() #联系人
    phone=scrapy.Field() #联系方式
    description=scrapy.Field() #详情描述
    detailLink=scrapy.Field() #具体链接

    pass
