from NovelScrapy.books.book import Book
from NovelScrapy.spiders.spider_types import SpiderTypes
class BookZhiCiZhongNian(Book):
    def getBookName(self):
        return "至此终年"

    def getHeadReg(self):
        return "id_XMjc2MjQx"

    def getHtml(self):
        return "https://www.bookbao8.com/book/201206/25/id_XMjc2MjQx.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBao()