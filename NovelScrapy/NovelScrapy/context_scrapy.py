from scrapy import cmdline

from NovelScrapy.NovelScrapy.books.books_setting import BooksSetting

cmdline.execute("scrapy crawl "+BooksSetting.getScrapyType().split())