from NovelScrapy.NovelJJWXC.NovelJJWXC.book.book_mizhidunyouyv import BookMiZhiDunYouYv
from NovelScrapy.NovelJJWXC.NovelJJWXC.book.book_bielaiwuyang import BookBieLaiWuYang


class BooksSetting:

    @staticmethod
    def initBook():
        return BookBieLaiWuYang()

    @staticmethod
    def getHtml():
        book = BooksSetting.initBook()
        return book.getHtml()

    @staticmethod
    def getHeadHtmlReg():
        book =  BooksSetting.initBook()
        return ".*"+book.getHeadReg()+"=(.*).*"

    @staticmethod
    def getNovelName():
        book =  BooksSetting.initBook()
        return book.getBookName()+".txt"