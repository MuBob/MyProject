from NovelScrapy.NovelLeWen.NovelLeWen.books.book_shizhangfuren import BookShiZhangFuRen
from NovelScrapy.NovelLeWen.NovelLeWen.books.book_mizhiyouyu import BookMiZhiYouYv
from NovelScrapy.NovelLeWen.NovelLeWen.books.book_henxianghenxiangni import BookHenXiangHenXiangNi


class BooksSetting:

    @staticmethod
    def initBook():
        return BookHenXiangHenXiangNi()

    @staticmethod
    def getHtml():
        book = BooksSetting.initBook()
        return book.getHtml()

    @staticmethod
    def getHeadHtmlReg():
        book =  BooksSetting.initBook()
        return ".*"+book.getHeadReg()+"/(.*).html.*"

    @staticmethod
    def getNovelName():
        book =  BooksSetting.initBook()
        return book.getBookName()