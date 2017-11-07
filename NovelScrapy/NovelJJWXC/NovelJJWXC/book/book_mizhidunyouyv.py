
from NovelScrapy.ScrapyBookbao.ScrapyBookbao.book.book import Book
class BookMiZhiDunYouYv(Book):
    def getBookName(self):
        return "蜜汁炖鱿鱼"

    def getHeadReg(self):
        return "chapterid"

    def getHtml(self):
        return "http://www.jjwxc.net/onebook.php?novelid=2307154"