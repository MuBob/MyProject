from NovelScrapy.ScrapyBookbao.ScrapyBookbao.book.book_jiaowonvshen import BookJiaoWoNvShen

from NovelScrapy.ScrapyBookbao.ScrapyBookbao.book.book_yiwuxiangyiwu import BookYiWuXiangYiWu
from NovelScrapy.ScrapyBookbao.ScrapyBookbao.book.book_nishiwoxueshengyouzenyang import BookNiShiWoXueShengYouZenYang


class BookbaoSetting:

    @staticmethod
    def initBook():
        return BookNiShiWoXueShengYouZenYang()

    @staticmethod
    def getHtml():
        book = BookbaoSetting.initBook()
        return book.getHtml()

    @staticmethod
    def getHeadHtmlReg():
        book =  BookbaoSetting.initBook()
        return ".*"+book.getHeadReg()+"_(.*).html.*"

    @staticmethod
    def getNovelName():
        book =  BookbaoSetting.initBook()
        return book.getBookName()+".txt"