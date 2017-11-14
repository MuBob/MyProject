from ScrapyNovel.books.book import BookRenJianShiGe


class BooksSetting:

    @staticmethod
    def initBook():
        return BookRenJianShiGe()

    @staticmethod
    def getHtml():
        book = BooksSetting.initBook()
        return book.getHtml()

    @staticmethod
    def getHeadHtmlReg():
        book =  BooksSetting.initBook()
        return book.getHeadReg()

    @staticmethod
    def getNovelName():
        book =  BooksSetting.initBook()
        return book.getBookName()

    @staticmethod
    def getScrapyType():
        book= BooksSetting.initBook()
        return book.getScrapyType()

    @staticmethod
    def getHtmlRegOrderReverse():
        book=BooksSetting.initBook()
        return book.getHtmlRegOrderReverse()