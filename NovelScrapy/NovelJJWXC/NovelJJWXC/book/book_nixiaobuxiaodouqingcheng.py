
from NovelScrapy.ScrapyBookbao.ScrapyBookbao.book.book import Book
class BookNiXiaoBuXiaoDouQingCheng(Book):
    def getBookName(self):
        return "你笑不笑都很倾城"

    def getHeadReg(self):
        return "chapterid"

    def getHtml(self):
        return "http://www.jjwxc.net/onebook.php?novelid=739180"