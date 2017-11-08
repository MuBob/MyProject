from NovelScrapy.NovelScrapy.books.book import Book
from NovelScrapy.NovelScrapy.spiders.spider_types import SpiderTypes

class BookJiaoWoNvShen(Book):
    def getBookName(self):
        return "叫我女神"

    def getHeadReg(self):
        return "id_XMjkyNzA4"

    def getHtml(self):
        return "https://www.bookbao8.com/book/201209/22/id_XMjkyNzA4.html"
    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBao()