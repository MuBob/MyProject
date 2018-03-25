# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

import xlwt

from search_people.search_sina.search_sina.filters import SinaFilters
from search_people.search_sina.search_sina.utils.HtmlManager import HtmlManager


class SearchSinaPipeline(object):
    def __init__(self):
        absPath = os.path.abspath('..')
        # self.file_name=absPath+'/scrapy_patch_job/zhaopin.xls'
        self.file_name = absPath + '/search_sina/out/新浪搜人_' + HtmlManager.getSearchName() + '.xls'
        self.excel_row = 0
        self.excel_work = xlwt.Workbook(encoding='utf-8')
        self.excel_sheet = self.excel_work.add_sheet(sheetname="table")
        self.excel_sheet.write(self.excel_row, 0, '名字')
        self.excel_sheet.write(self.excel_row, 1, '性别')
        self.excel_sheet.write(self.excel_row, 2, '地址')
        self.excel_sheet.write(self.excel_row, 3, '主页链接')
        self.excel_sheet.write(self.excel_row, 4, '关注量')
        self.excel_sheet.write(self.excel_row, 5, '粉丝量')
        self.excel_sheet.write(self.excel_row, 6, '微博量')
        self.excel_sheet.write(self.excel_row, 7, '个人信息')
        self.excel_sheet.write(self.excel_row, 8, '所有标签')
        self.excel_work.save(self.file_name)
        self.cur_next()
        self.filter=SinaFilters()


    def process_item(self, item, spider):

        self.excel_sheet.write(self.excel_row, 0, item['name'])
        self.excel_sheet.write(self.excel_row, 1, item['sex'])
        self.excel_sheet.write(self.excel_row, 2, item['address'])
        if self.filter.filterSexIn(item['sex'])&self.filter.filterAddresIn(item['address']):
            self.excel_sheet.write(self.excel_row, 3, item['detail_link'])
        self.excel_sheet.write(self.excel_row, 4, item['number_guan_zhu'])
        self.excel_sheet.write(self.excel_row, 5, item['number_fen_si'])
        self.excel_sheet.write(self.excel_row, 6, item['number_wei_bo'])
        self.excel_sheet.write(self.excel_row, 7, item['info'])
        self.excel_sheet.write(self.excel_row, 8, item['label'])
        self.excel_work.save(self.file_name)
        self.cur_next()
        return item


    def cur_next(self):
        self.excel_row += 1