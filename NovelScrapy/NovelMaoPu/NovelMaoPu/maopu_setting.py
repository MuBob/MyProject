from NovelScrapy.NovelMaoPu.NovelMaoPu.books.book_weiqinghunai import BookWeiQingHunAi


class MaoPuSetting:

    @staticmethod
    def initBook():
        return BookWeiQingHunAi()

    @staticmethod
    def getHtml():
        book = MaoPuSetting.initBook()
        return book.getHtml()

    @staticmethod
    def getHeadHtmlReg():
        book =  MaoPuSetting.initBook()
        return ".*"+book.getHtml()+"(.*).html.*"

    @staticmethod
    def getNovelName():
        book =  MaoPuSetting.initBook()
        return book.getBookName()+".txt"