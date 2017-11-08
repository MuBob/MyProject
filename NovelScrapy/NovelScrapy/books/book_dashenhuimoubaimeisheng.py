from NovelScrapy.NovelScrapy.books.book import Book
from NovelScrapy.NovelScrapy.spiders.spider_types import SpiderTypes
class BookDaShenHuiMouBaiMeiShen(Book):
    def getBookName(self):
        return "大神回眸百媚生"

    def getHeadReg(self):
        return "id_XNDUxNTgy"

    def getHtml(self):
        return "https://www.bookbao8.com/book/201507/15/id_XNDUxNTgy.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBao()