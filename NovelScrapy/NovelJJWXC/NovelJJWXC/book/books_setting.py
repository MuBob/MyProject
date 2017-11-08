from NovelScrapy.NovelJJWXC.NovelJJWXC.book.book_mizhidunyouyv import BookMiZhiDunYouYv
from NovelScrapy.NovelJJWXC.NovelJJWXC.book.book_bielaiwuyang import BookBieLaiWuYang
from NovelScrapy.NovelJJWXC.NovelJJWXC.book.book_nixiaobuxiaodouqingcheng import BookNiXiaoBuXiaoDouQingCheng
from NovelScrapy.NovelJJWXC.NovelJJWXC.book.book_ainishiwozuoguozuihaodeshi import BookAiNiShiWoZuoGuoZuiHaoDeShi


class BooksSetting:

    @staticmethod
    def initBook():
        return BookAiNiShiWoZuoGuoZuiHaoDeShi()

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