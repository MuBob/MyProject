# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
from operator import attrgetter

from pip._vendor.requests.packages import chardet

class NovelmdscrapyPipeline(object):
    def __init__(self):
        self.all = []
        self.out_file = 'E:/Users/Administrator/PycharmProjects/MyProject/ScrapyNovel/ScrapyNovel/out/output.txt'
        # os.mknod(self.out_file)
        pass

    def process_item(self, item, spider):
        print("item=", item)
        self.all.append(item)
        # sorted(self.all, key=attrgetter('chapter'), reverse=True)
        file = open(self.out_file, 'w', encoding='UTF-8')
        for index in self.all:
            file.write(index['title'] + '\n')
            file.write(index['content'] + '\n\n')
        file.close()
        return item
