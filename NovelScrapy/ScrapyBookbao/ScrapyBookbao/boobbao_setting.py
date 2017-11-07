from NovelScrapy.ScrapyBookbao.ScrapyBookbao.book.book_jiaowonvshen import BookJiaoWoNvShen

from NovelScrapy.ScrapyBookbao.ScrapyBookbao.book.book_yiwuxiangyiwu import BookYiWuXiangYiWu
from NovelScrapy.ScrapyBookbao.ScrapyBookbao.book.book_nishiwoxueshengyouzenyang import BookNiShiWoXueShengYouZenYang
from NovelScrapy.ScrapyBookbao.ScrapyBookbao.book.book_xuxuyouzhi import BookXuXuYouZhi
from NovelScrapy.ScrapyBookbao.ScrapyBookbao.book.book_qianqingrenbuzhii import BookQianQingRenBuZhi


class BookbaoSetting:

    @staticmethod
    def initBook():
        return BookQianQingRenBuZhi()

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