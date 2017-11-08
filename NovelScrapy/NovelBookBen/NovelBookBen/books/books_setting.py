from NovelScrapy.NovelBookBen.NovelBookBen.books.book_ruanchenenjing import BookRuanChenEnJing


class BooksSetting:

    @staticmethod
    def initBook():
        return BookRuanChenEnJing()

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