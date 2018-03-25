import os
class HtmlSetting:
    @staticmethod
    def getPageCount():
        return 3
    @staticmethod
    def getRequestUrlFormat():
        return "http://bj.58.com/chuzu/pn%d/?utm_source=sem-sales-baidu-pc&spm=56414705409.14884475011&utm_campaign=sell&utm_medium=cpc&PGTID=0d3090a7-0000-1ceb-cd82-748557d6488a&ClickID=2"

    @staticmethod
    def getSaveFileName():
        abspath = os.path.abspath('..')
        return abspath+'/out/58house.xls'
