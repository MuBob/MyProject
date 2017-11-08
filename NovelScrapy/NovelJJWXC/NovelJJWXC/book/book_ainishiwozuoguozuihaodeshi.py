
from NovelScrapy.ScrapyBookbao.ScrapyBookbao.book.book import Book
class BookAiNiShiWoZuoGuoZuiHaoDeShi(Book):
    def getBookName(self):
        return "爱你,是我做过最好的事"

    def getHeadReg(self):
        return "chapterid"

    def getHtml(self):
        return "http://www.jjwxc.net/onebook.php?novelid=427080"