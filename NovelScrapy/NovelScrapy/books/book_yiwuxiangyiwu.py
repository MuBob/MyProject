from NovelScrapy.NovelScrapy.books.book import Book
from NovelScrapy.NovelScrapy.spiders.spider_types import SpiderTypes
class BookYiWuXiangYiWu(Book):
    def getBookName(self):
        return "一物降一物"

    def getHeadReg(self):
        return "id_XMjI3MTAz"

    def getHtml(self):
        return "https://www.bookbao8.com/book/201201/17/id_XMjI3MTAz.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBao()