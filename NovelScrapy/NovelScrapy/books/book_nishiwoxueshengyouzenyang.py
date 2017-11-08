from NovelScrapy.NovelScrapy.books.book import Book
from NovelScrapy.NovelScrapy.spiders.spider_types import SpiderTypes
class BookNiShiWoXueShengYouZenYang(Book):
    def getBookName(self):
        return "你是我学生又怎样"

    def getHeadReg(self):
        return "id_XMjkzMTM3"

    def getHtml(self):
        return "https://www.bookbao8.com/book/201209/25/id_XMjkzMTM3.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBao()