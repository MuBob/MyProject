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

    def getHtmlRegOrderReverse(self):
        return False


class BookZhiCiZhongNian(Book):
    def getBookName(self):
        return "至此终年"

    def getHeadReg(self):
        return ".*" + "id_XMjc2MjQx" + "_(.*).html.*"

    def getHtml(self):
        return "https://www.bookbao8.com/book/201206/25/id_XMjc2MjQx.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBao()

class BookNiXiaoBuXiaoDouHenQingCheng_BookBao8(Book):
    def getBookName(self):
        return "你笑不笑都很倾城"

    def getHeadReg(self):
        return ".*" + "id_XMjE4MDQ0" + "_(.*).html.*"

    def getHtml(self):
        return "https://www.bookbao8.com/views/201111/20/218044.html"

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

class BookZuiDongTingDeShi(Book):
    def getBookName(self):
        return "最动听的事"

    def getHeadReg(self):
        return ".*" + "id_XNDI1MTA1" + "_(.*).html.*"

    def getHtml(self):
        return "https://www.bookbao8.com/book/201505/19/id_XNDI1MTA1.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBao()


class BookSanShu(Book):
    def getBookName(self):
        return "三梳"

    def getHeadReg(self):
        return ".*" + "id_XNTM1OTc4" + "_(.*).html.*"

    def getHtml(self):
        return "https://www.bookbao8.com/book/201608/18/id_XNTM1OTc4.html"

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
        return ".*" + "chapterid" + "=(.*)"

    def getHtml(self):
        return "http://www.jjwxc.net/onebook.php?novelid=1017137"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_JJWXC()


class BookWoDeManLinDa(Book):
    def getBookName(self):
        return "我的曼林达"

    def getHeadReg(self):
        return ".*" + "chapterid" + "=(.*)"

    def getHtml(self):
        return "http://www.jjwxc.net/onebook.php?novelid=2589669"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_JJWXC()


class BookPingShengBuWan(Book):
    def getBookName(self):
        return "平生不晚"

    def getHeadReg(self):
        return ".*" + "chapterid" + "=(.*)"

    def getHtml(self):
        return "http://www.jjwxc.net/onebook.php?novelid=2534494"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_JJWXC()


class BookNiXiaoBuXiaoDouQingCheng(Book):
    def getBookName(self):
        return "你笑不笑都很倾城"

    def getHeadReg(self):
        return ".*" + "chapterid" + "=(.*)"

    def getHtml(self):
        return "http://www.jjwxc.net/onebook.php?novelid=739180"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_JJWXC()


class BookMiZhiDunYouYv(Book):
    def getBookName(self):
        return "蜜汁炖鱿鱼"

    def getHeadReg(self):
        return ".*" + "chapterid" + "=(.*)"

    def getHtml(self):
        return "http://www.jjwxc.net/onebook.php?novelid=2307154"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_JJWXC()


class BookBieLaiWuYang(Book):
    def getBookName(self):
        return "别来无恙"

    def getHeadReg(self):
        return ".*" + "chapterid" + "=(.*)"

    def getHtml(self):
        return "http://www.jjwxc.net/onebook.php?novelid=1928902"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_JJWXC()


class BookAiNiShiWoZuoGuoZuiHaoDeShi(Book):
    def getBookName(self):
        return "爱你,是我做过最好的事"

    def getHeadReg(self):
        return ".*" + "chapterid" + "=(.*)"

    def getHtml(self):
        return "http://www.jjwxc.net/onebook.php?novelid=427080"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_JJWXC()


class BookRenJianShiGe(Book):
    def getBookName(self):
        return "人间失格"

    def getHeadReg(self):
        return ".*" + "renjianshige/" + "(.*)" + ".html.*"

    def getHtml(self):
        return "http://www.sbkk88.com/mingzhu/waiguowenxuemingzhu/renjianshige/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_SDKK88()

    def getHtmlRegOrderReverse(self):
        return True

class BookShuangChengJi(Book):
    def getBookName(self):
        return "双城记"

    def getHeadReg(self):
        return ".*" + "id_XMzg0Njk0" + "_(.*)" + ".html.*"

    def getHtml(self):
        return "https://www.bookbao8.com/book/201409/18/id_XMzg0Njk0.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBao()


class BookXieYang(Book):
    def getBookName(self):
        return "斜阳"

    def getHeadReg(self):
        return ".*" + "80_80494/" + "(.*)" + ".html.*"

    def getHtml(self):
        return "http://www.bookben.com/read/80_80494/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBen()

class BookQingJiuXiMeiNan(Book):
    def getBookName(self):
        return "清酒系美男"

    def getHeadReg(self):
        return ".*" + "92979" + "/(.*)" + ".html.*"

    def getHtml(self):
        return "http://www.2kxs.com/xiaoshuo/92/92979/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_2KXiaoShuo()

class BookTingNanSiYv(Book):
    def getBookName(self):
        return "汀南丝雨"

    def getHeadReg(self):
        return ".*" + "95493" + "/(.*)" + ".html.*"

    def getHtml(self):
        return "https://www.2kxs.com/xiaoshuo/95/95493/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_2KXiaoShuo()

class BookTuLu(Book):
    def getBookName(self):
        return "屠路"

    def getHeadReg(self):
        return ".*" + "86339" + "/(.*)" + ".html.*"

    def getHtml(self):
        return "https://www.2kxs.com/xiaoshuo/86/86339/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_2KXiaoShuo()

class BookTaZhiDaoFengCongNaGeFangXiangLai(Book):
    def getBookName(self):
        return "他知道风从哪个方向来"

    def getHeadReg(self):
        return ".*" + "85248" + "/(.*)" + ".html.*"

    def getHtml(self):
        return "https://www.2kxs.com/xiaoshuo/85/85248/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_2KXiaoShuo()

class BookHenXiangHenXiangNi(Book):
    def getBookName(self):
        return "很想很想你"

    def getHeadReg(self):
        return ".*" + "6092" + "/(.*)" + ".html.*"

    def getHtml(self):
        return "http://www.lwxs520.com/books/6/6092/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_LWXiaoShuo520()

class BookMiZhiYouYv(Book):
    def getBookName(self):
        return "蜜汁炖鱿鱼"

    def getHeadReg(self):
        return ".*" + "28748" + "/(.*)" + ".html.*"

    def getHtml(self):
        return "http://www.lwxs520.com/books/28/28748/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_LWXiaoShuo520()

class BookShiZhangFuRen(Book):
    def getBookName(self):
        return "市长夫人"

    def getHeadReg(self):
        return ".*"+"20621"+"/(.*)"+".html"

    def getHtml(self):
        return "http://www.lwxiaoshuo.com/20/20621/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_LeWenXiaoShuo()

class BookWeiQingHunAi(Book):
    def getBookName(self):
        return "危情婚爱，总裁宠妻如命"

    def getHeadReg(self):
        return ""

    def getHtml(self):
        return "http://www.mpxiaoshuo.com/book/49339/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_MaoPu()

class BookYanHuiXiMeiNan(Book):
    def getBookName(self):
        return "烟灰系美男"

    def getHeadReg(self):
        return ".*" + "44923" + "/(.*)" + ".html"

    def getHtml(self):
        return "http://www.lwxiaoshuo.com/44/44923/index.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_LeWenXiaoShuo()


class BookYiZuoChengZaiDengNi(Book):
    def getBookName(self):
        return "一座城在等你"

    def getHeadReg(self):
        return ".*" + "68965" + "/(.*)" + ".html"

    def getHtml(self):
        return "http://www.lwxiaoshuo.com/68/68965/index.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_LeWenXiaoShuo()


class BookWoDeLaoGongShiMingWang(Book):
    def getBookName(self):
        return "我的老公是冥王"

    def getHeadReg(self):
        return ".*" + "3769" + "/(.*).html.*"

    def getHtml(self):
        return "http://www.xinshula.com/3/3769/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_XinShuLa()


