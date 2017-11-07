# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import xlwt
from operator import attrgetter, itemgetter

from pip._vendor.requests.packages import chardet

from NovelScrapy.Novel2kxs.Novel2kxs.books.books_setting import BooksSetting


class NovelyanyangPipeline(object):
    def __init__(self):
        self.all = []
        abspath = os.path.abspath(".")
        self.out_file = abspath + '\\out\\'+BooksSetting.getNovelName()
        pass

    def process_item(self, item, spider):
        # print("item=", item)
        self.all.append(item)
        # print("before sort list=", self.all[0])
        self.all.sort(key=lambda i: i["chapter"], reverse=False)
        # print("after sort list=", self.all[0])
        file = open(self.out_file, 'w', encoding='UTF-8')
        for index in self.all:
            # print('index=', index)
            file.write(index['title'])
            file.write(index['content'] + '\n\n\n')
        file.close()
        return item
