# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import os

import time
import xlrd
import xlwt

from net.scrapy_patch_job.location.gaode_api import GaoDeApi
from net.scrapy_patch_job.scrapy_patch_job.filter import Filter


class ScrapyPatchJobPipeline(object):
    def __init__(self):
        time_format = time.strftime('%Y_%m_%d', time.localtime(time.time()))
        absPath = os.path.abspath('..')
        # self.file_name=absPath+'/scrapy_patch_job/zhaopin.xls'
        self.file_name =absPath + '/scrapy_patch_job/招聘(知春路地铁站五公里内)_' + time_format + '.xls'
        self.excel_row=0
        self.excel_column=0
        self.excel_work = xlwt.Workbook(encoding='utf-8')
        self.excel_sheet = self.excel_work.add_sheet(sheetname="table")
        self.excel_sheet.write(self.excel_row, 0, '职位')
        self.excel_sheet.write(self.excel_row, 1, '公司')
        self.excel_sheet.write(self.excel_row, 2, '城市')
        self.excel_sheet.write(self.excel_row, 3, '工作地点')
        self.excel_sheet.write(self.excel_row, 4, '职位详情页链接')
        self.excel_sheet.write(self.excel_row, 5, '发布时间')
        self.excel_sheet.write(self.excel_row, 6, '薪资水平')
        self.excel_sheet.write(self.excel_row, 7, '待遇')
        self.excel_sheet.write(self.excel_row, 8, '详情描述')
        self.excel_work.save(self.file_name)
        self.cur_next()

        self.gaode=GaoDeApi()
        self.my_position=self.gaode.getPosition("知春路地铁站")
        self.my_range=5*1000 #(米)

        self.filter=Filter()


    def process_item(self, item, spider):
        is_in_range = self.gaode.isInRange(self.my_position, self.my_range, self.gaode.getPosition(item['location']))
        # is_title = self.filter.filterTitle(item['title'])
        is_title = self.filter.filterTitleOut(item['title'])
        is_location = self.filter.filterLocation(item['location'])
        is_money = self.filter.filterMoney(item['money'])
        is_treatment = self.filter.filterTreatment(item['treatment'])
        is_description = self.filter.filterDescription(item['description'])

        if is_in_range&is_title&is_location&is_money&is_treatment&is_description:
        # if is_title&is_location&is_money&is_treatment&is_description:
            self.excel_sheet.write(self.excel_row, 0, item['title'])
            self.excel_sheet.write(self.excel_row, 1, item['company'])
            self.excel_sheet.write(self.excel_row, 2, item['city'])
            self.excel_sheet.write(self.excel_row, 3, item['location'])
            self.excel_sheet.write(self.excel_row, 4, item['detailLink'])
            self.excel_sheet.write(self.excel_row, 5, item['publishTime'])
            self.excel_sheet.write(self.excel_row, 6, item['money'])
            self.excel_sheet.write(self.excel_row, 7, item['treatment'])
            self.excel_sheet.write(self.excel_row, 8, item['description'])
        else:
            self.excel_sheet.write(self.excel_row, 0, item['title'])
            self.excel_sheet.write(self.excel_row, 4, item['detailLink'])
        self.excel_work.save(self.file_name)
        self.cur_next()
        return item

    def spider_closed(self, spider):
        pass

    def cur_next(self):
        self.excel_row += 1
        self.excel_column = 0