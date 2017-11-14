# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

from ScrapyNovel.books.books_setting import BooksSetting


class ScrapynovelPipeline(object):
    def __init__(self):
        self.all = []
        abspath = os.path.abspath('.')
        self.out_file = abspath + '\\out\\' + BooksSetting.getNovelName() + ".txt"

    def process_item(self, item, spider):
        # print("item=", item)
        self.all.append(item)
        self.all.sort(key=lambda i: i['chapter'], reverse=BooksSetting.getHtmlRegOrderReverse())
        file = open(self.out_file, 'w', encoding='UTF-8')
        file.write(item['name'] + '\n\t\t' + item['author'] + '\n')
        for index in self.all:
            file.write(index['title'] + '\n')
            file.write(index['content'] + '\n\n')
        file.close()
        return item