from scrapy import cmdline

# from ScrapyNovel.books.books_setting import BooksSetting
# cmd=("scrapy crawl "+BooksSetting.getScrapyType()).split()
# cmdline.execute(cmd)
cmdline.execute(("scrapy crawl NovelBookbao8").split())