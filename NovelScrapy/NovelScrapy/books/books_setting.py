from NovelScrapy.ScrapyBookbao.ScrapyBookbao.book.book_jiaowonvshen import BookJiaoWoNvShen

from NovelScrapy.ScrapyBookbao.ScrapyBookbao.book.book_yiwuxiangyiwu import BookYiWuXiangYiWu
from NovelScrapy.ScrapyBookbao.ScrapyBookbao.book.book_nishiwoxueshengyouzenyang import BookNiShiWoXueShengYouZenYang
from NovelScrapy.ScrapyBookbao.ScrapyBookbao.book.book_xuxuyouzhi import BookXuXuYouZhi
from NovelScrapy.ScrapyBookbao.ScrapyBookbao.book.book_qianqingrenbuzhii import BookQianQingRenBuZhi
from NovelScrapy.ScrapyBookbao.ScrapyBookbao.book.book_shijieweichenli import BookShiJieWeiChenLi


class BooksSetting:

    @staticmethod
    def initBook():
        return BookShiJieWeiChenLi()

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

    @staticmethod
    def getScrapyType():
        book= BooksSetting.initBook()
        return book.getScrapyType()