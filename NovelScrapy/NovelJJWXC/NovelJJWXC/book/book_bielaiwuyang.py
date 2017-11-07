
from NovelScrapy.ScrapyBookbao.ScrapyBookbao.book.book import Book
class BookBieLaiWuYang(Book):
    def getBookName(self):
        return "别来无恙"

    def getHeadReg(self):
        return "chapterid"

    def getHtml(self):
        return "http://www.jjwxc.net/onebook.php?novelid=1928902"