# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class ScrapyPatchJobItem(scrapy.Item):
    # define the fields for your item here like:
    title = Field()# 职位名称
    company = Field()#公司名称
    city = Field() #所在城市
    location = Field()# 工作地点
    detailLink = Field()  # 职位详情页链接
    publishTime = Field()  # 发布时间
    money=Field()  #薪资水平
    treatment = Field()#待遇
    description = Field()#详情描述
