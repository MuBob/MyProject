# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import xlwt

from net.scrapy_patch_house.scrapy_patch_house.setting.html_setting import HtmlSetting
from net.util.gaode_api import GaoDeApi
from net.scrapy_patch_house.scrapy_patch_house.setting.filter import Filter


class ScrapyPatchHousePipeline(object):
    def __init__(self):
        self.excel_row=0
        self.excel_column=0
        self.excel_work = xlwt.Workbook(encoding='utf-8')
        self.excel_sheet = self.excel_work.add_sheet(sheetname="table")
        self.excel_sheet.write(self.excel_row, 0, '标题')
        self.excel_sheet.write(self.excel_row, 1, '租金')
        self.excel_sheet.write(self.excel_row, 2, '支付周期')
        self.excel_sheet.write(self.excel_row, 3, '租赁方式')
        self.excel_sheet.write(self.excel_row, 4, '房屋类型')
        self.excel_sheet.write(self.excel_row, 5, '朝向楼层')
        self.excel_sheet.write(self.excel_row, 6, '住宅小区')
        self.excel_sheet.write(self.excel_row, 7, '所属区域')
        self.excel_sheet.write(self.excel_row, 8, '详细地址')
        self.excel_sheet.write(self.excel_row, 9, '联系人')
        self.excel_sheet.write(self.excel_row, 10, '联系方式')
        self.excel_sheet.write(self.excel_row, 11, '详情描述')
        self.excel_sheet.write(self.excel_row, 12, '具体链接')
        self.excel_work.save(HtmlSetting.getSaveFileName())
        self.cur_next()

        self.gaode=GaoDeApi()
        self.my_position=self.gaode.getPosition("北京市海淀区北科大厦")
        self.my_range=5*1000 #(米)

        self.filter=Filter()
    def process_item(self, item, spider):
        print('item=', item)
        try:
            is_in_range = self.gaode.isInRange(self.my_position, self.my_range, self.gaode.getPosition(item['residential']))
            is_lean_in = self.filter.filtLeanIn(item['lease'])
            is_lean_in = True
            is_money = self.filter.filtMoney(item['rentMoney'])
            if is_in_range&is_lean_in & is_money:
                self.excel_sheet.write(self.excel_row, 0, item['title'])
                self.excel_sheet.write(self.excel_row, 1, item['rentMoney'])
                self.excel_sheet.write(self.excel_row, 2, item['rentType'])
                self.excel_sheet.write(self.excel_row, 3, item['lease'])
                self.excel_sheet.write(self.excel_row, 4, item['types'])
                self.excel_sheet.write(self.excel_row, 5, item['floor'])
                self.excel_sheet.write(self.excel_row, 6, item['residential'])
                self.excel_sheet.write(self.excel_row, 7, item['area'])
                self.excel_sheet.write(self.excel_row, 8, item['address'])
                self.excel_sheet.write(self.excel_row, 9, item['contactor'])
                self.excel_sheet.write(self.excel_row, 10, item['phone'])
                self.excel_sheet.write(self.excel_row, 11, item['description'])
                self.excel_sheet.write(self.excel_row, 12, item['detailLink'])
            else:
                self.excel_sheet.write(self.excel_row, 0, item['title'])
                self.excel_sheet.write(self.excel_row, 1, item['rentMoney'])
                self.excel_sheet.write(self.excel_row, 12, item['detailLink'])
        except:
            print("catch exception! row=",self.excel_row)
        self.excel_work.save(HtmlSetting.getSaveFileName())
        self.cur_next()
        return item

    def spider_closed(self, spider):
        pass

    def cur_next(self):
        self.excel_row += 1
        self.excel_column = 0
