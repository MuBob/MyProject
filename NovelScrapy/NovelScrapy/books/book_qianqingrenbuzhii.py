from NovelScrapy.NovelScrapy.books.book import Book
from NovelScrapy.NovelScrapy.spiders.spider_types import SpiderTypes

class BookQianQingRenBuZhi(Book):
    def getBookName(self):
        return "浅情人不知"

    def getHeadReg(self):
        return "id_XNDUxMDU2"

    def getHtml(self):
        return "https://www.bookbao8.com/book/201507/14/id_XNDUxMDU2.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBao()