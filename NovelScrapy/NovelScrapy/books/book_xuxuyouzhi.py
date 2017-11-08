from NovelScrapy.NovelScrapy.books.book import Book
from NovelScrapy.NovelScrapy.spiders.spider_types import SpiderTypes
class BookXuXuYouZhi(Book):
    def getBookName(self):
        return "徐徐诱之"

    def getHeadReg(self):
        return "id_XNDI5NDQx"

    def getHtml(self):
        return "https://www.bookbao8.com/book/201505/29/id_XNDI5NDQx.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBao()