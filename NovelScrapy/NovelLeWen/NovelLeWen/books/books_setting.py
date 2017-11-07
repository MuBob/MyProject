from NovelScrapy.NovelLeWen.NovelLeWen.books.book_shizhangfuren import BookShiZhangFuRen
from NovelScrapy.NovelLeWen.NovelLeWen.books.book_mizhiyouyu import BookMiZhiYouYv


class BooksSetting:

    @staticmethod
    def initBook():
        return BookMiZhiYouYv()

    @staticmethod
    def getHtml():
        book = BooksSetting.initBook()
        return book.getHtml()

    @staticmethod
    def getHeadHtmlReg():
        book =  BooksSetting.initBook()
        return ".*"+book.getHeadReg()+"_(.*).html.*"

    @staticmethod
    def getNovelName():
        book =  BooksSetting.initBook()
        return book.getBookName()+".txt"