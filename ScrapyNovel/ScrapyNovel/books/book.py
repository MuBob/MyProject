from ScrapyNovel.books.spider_types import SpiderTypes


class Book:
    def getBookName(self):
        return ""

    def getHtml(self):
        return ""

    def getHeadReg(self):
        return ""

    def getScrapyType(self):
        return ""

class BookZhiCiZhongNian(Book):
    def getBookName(self):
        return "至此终年"

    def getHeadReg(self):
        return ".*" + "id_XMjc2MjQx" + "_(.*).html.*"

    def getHtml(self):
        return "https://www.bookbao8.com/book/201206/25/id_XMjc2MjQx.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBao()

class BookBuJiuTouNiYiBeiZi(Book):
    def getBookName(self):
        return "不就偷你一杯子"

    def getHeadReg(self):
        return ".*" + "id_XMjgwNDQw" + "_(.*).html.*"

    def getHtml(self):
        return "https://www.bookbao8.com/book/201207/24/id_XMjgwNDQw.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBao()


class BookXinSuRuJian(Book):
    def getBookName(self):
        return "心素如简"

    def getHeadReg(self):
        return ".*" + "id_XMjIwNzkx" + "_(.*).html.*"

    def getHtml(self):
        return "https://www.bookbao8.com/book/201112/06/id_XMjIwNzkx.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBao()

class BookManManDeDouShiWoDuiNiDeAi(Book):
    def getBookName(self):
        return "满满的都是我对你的爱"

    def getHeadReg(self):
        return    ".*" + "chapterid" + "=(.*)"

    def getHtml(self):
        return "http://www.jjwxc.net/onebook.php?novelid=1017137"
    def getScrapyType(self):
        return SpiderTypes.getTypeName_JJWXC()

class BookWoDeManLinDa(Book):
    def getBookName(self):
        return "我的曼林达"

    def getHeadReg(self):
        return    ".*" + "chapterid" + "=(.*)"

    def getHtml(self):
        return "http://www.jjwxc.net/onebook.php?novelid=2589669"
    def getScrapyType(self):
        return SpiderTypes.getTypeName_JJWXC()

class BookPingShengBuWan(Book):
    def getBookName(self):
        return "平生不晚"

    def getHeadReg(self):
        return    ".*" + "chapterid" + "=(.*)"

    def getHtml(self):
        return "http://www.jjwxc.net/onebook.php?novelid=2534494"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_JJWXC()

class BookNiXiaoBuXiaoDouQingCheng(Book):
    def getBookName(self):
        return "你笑不笑都很倾城"

    def getHeadReg(self):
        return    ".*" + "chapterid" + "=(.*)"

    def getHtml(self):
        return "http://www.jjwxc.net/onebook.php?novelid=739180"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_JJWXC()

class BookMiZhiDunYouYv(Book):
    def getBookName(self):
        return "蜜汁炖鱿鱼"

    def getHeadReg(self):
        return    ".*" + "chapterid" + "=(.*)"

    def getHtml(self):
        return "http://www.jjwxc.net/onebook.php?novelid=2307154"
    def getScrapyType(self):
        return SpiderTypes.getTypeName_JJWXC()

class BookBieLaiWuYang(Book):
    def getBookName(self):
        return "别来无恙"

    def getHeadReg(self):
        return    ".*" + "chapterid" + "=(.*)"

    def getHtml(self):
        return "http://www.jjwxc.net/onebook.php?novelid=1928902"
    def getScrapyType(self):
        return SpiderTypes.getTypeName_JJWXC()

class BookAiNiShiWoZuoGuoZuiHaoDeShi(Book):
    def getBookName(self):
        return "爱你,是我做过最好的事"

    def getHeadReg(self):
        return    ".*" + "chapterid" + "=(.*)"

    def getHtml(self):
        return "http://www.jjwxc.net/onebook.php?novelid=427080"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_JJWXC()