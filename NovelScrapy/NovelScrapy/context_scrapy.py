from scrapy import cmdline

from NovelScrapy.NovelScrapy.books.books_setting import BooksSetting

cmd=("scrapy crawl "+BooksSetting.getScrapyType()).split()
cmdline.execute(cmd)