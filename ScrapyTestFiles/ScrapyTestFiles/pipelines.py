# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os


class ScrapytestfilesPipeline(object):

    def __init__(self):
        self.all = []
        self.abspath = os.path.abspath('.')

    def process_item(self, item, spider):
        # print("item=", item)
        out_file = self.abspath + '\\out\\' + item['title'] + ".txt"
        # print("out_file=%s", out_file)
        file = open(out_file, 'w', encoding='UTF-8')
        file.write(item['link'] + '\n')
        file.write(item['title'] + '\n')
        file.write(item['content'] + '\n\n')
        file.close()
        return item