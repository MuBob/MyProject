from NovelScrapy.NovelScrapy.books.book import Book
from NovelScrapy.NovelScrapy.spiders.spider_types import SpiderTypes
class BookShiJieWeiChenLi(Book):
    def getBookName(self):
        return "世界微尘里"

    def getHeadReg(self):
        return "id_XMzg2OTY0"

    def getHtml(self):
        return "https://www.bookbao8.com/book/201501/04/id_XMzg2OTY0.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBao()