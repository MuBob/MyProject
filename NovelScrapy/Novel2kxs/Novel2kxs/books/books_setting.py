from NovelScrapy.Novel2kxs.Novel2kxs.books.book_qingjiuximeinan import BookQingJiuXiMeiNan
from NovelScrapy.Novel2kxs.Novel2kxs.books.book_yanyanggaogaozhao import BookYanYangGaoGaoZhao
from NovelScrapy.Novel2kxs.Novel2kxs.books.book_qingjiuximeinan import BookQingJiuXiMeiNan


class BooksSetting:
    @staticmethod
    def initBook():
        # return BookYanYangGaoGaoZhao()
        return BookQingJiuXiMeiNan()

    @staticmethod
    def getHtml():
        book = BooksSetting.initBook()
        return book.getHtml()

    @staticmethod
    def getHeadHtmlReg():
        book = BooksSetting.initBook()

        return ".*" + book.getHeadReg() + "(.*).html.*"

    @staticmethod
    def getNovelName():
        book = BooksSetting.initBook()
        return book.getBookName() + ".txt"