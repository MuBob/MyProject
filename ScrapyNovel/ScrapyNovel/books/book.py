from ScrapyNovel.books.spider_types import SpiderTypes


class Book:
    def getBookName(self):
        return ""

    def getHtml(self):
        return ""

    def getHtmlLast(self):
        return ".html"

    def getHeadReg(self):
        return ""

    def getScrapyType(self):
        return ""

    def getHtmlRegOrderReverse(self):
        return False


############################################ 来自《书包网》 #############################################################
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
        return ".*" + "id_XMjE4MDQ0" + "_(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "https://www.bookbao8.com/views/201111/20/218044.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBao()


class BookBuJiuTouNiYiBeiZi(Book):
    def getBookName(self):
        return "不就偷你一杯子"

    def getHeadReg(self):
        return ".*" + "id_XMjgwNDQw" + "_(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "https://www.bookbao8.com/book/201207/24/id_XMjgwNDQw.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBao()


class BookZuiDongTingDeShi(Book):
    def getBookName(self):
        return "最动听的事"

    def getHeadReg(self):
        return ".*" + "id_XNDI1MTA1" + "_(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "https://www.bookbao8.com/book/201505/19/id_XNDI1MTA1.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBao()


class BookSanShu(Book):
    def getBookName(self):
        return "三梳"

    def getHeadReg(self):
        return ".*" + "id_XNTM1OTc4" + "_(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "https://www.bookbao8.com/book/201608/18/id_XNTM1OTc4.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBao()


class BookXinSuRuJian(Book):
    def getBookName(self):
        return "心素如简"

    def getHeadReg(self):
        return ".*" + "id_XMjIwNzkx" + "_(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "https://www.bookbao8.com/book/201112/06/id_XMjIwNzkx.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBao()


class BookShuangChengJi(Book):
    def getBookName(self):
        return "双城记"

    def getHeadReg(self):
        return ".*" + "id_XMzg0Njk0" + "_(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "https://www.bookbao8.com/book/201409/18/id_XMzg0Njk0.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBao()


class BookWoCengZaiShiGuangLiTingGuoNi(Book):
    def getBookName(self):
        return "我曾在时光里听过你"

    def getHeadReg(self):
        return ".*" + "id_XNTMyNDAy" + "_(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "https://www.bookbao99.net/book/201607/10/id_XNTMyNDAy.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BookBao()


############################################ 来自《晋江文学城》 #########################################################
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


class BookShenZhiZuoShou(Book):
    def getBookName(self):
        return "神之左手[密室前传]"

    def getHeadReg(self):
        return ".*" + "chapterid" + "=(.*)"

    def getHtml(self):
        return "http://www.jjwxc.net/onebook.php?novelid=1406683"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_JJWXC()


class BookMiShiKunYouYv(Book):
    def getBookName(self):
        return "密室困鱿鱼"

    def getHeadReg(self):
        return ".*" + "chapterid" + "=(.*)"

    def getHtml(self):
        return "http://www.jjwxc.net/onebook.php?novelid=2241909"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_JJWXC()


############################################ 来自《2K小说》 #############################################################

class BookQingJiuXiMeiNan(Book):
    def getBookName(self):
        return "清酒系美男"

    def getHeadReg(self):
        return ".*" + "92979" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://www.2kxs.com/xiaoshuo/92/92979/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_2KXiaoShuo()


class BookTingNanSiYv(Book):
    def getBookName(self):
        return "汀南丝雨"

    def getHeadReg(self):
        return ".*" + "95493" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "https://www.2kxs.com/xiaoshuo/95/95493/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_2KXiaoShuo()


class BookTuLu(Book):
    def getBookName(self):
        return "屠路"

    def getHeadReg(self):
        return ".*" + "86339" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "https://www.2kxs.com/xiaoshuo/86/86339/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_2KXiaoShuo()


class BookTaZhiDaoFengCongNaGeFangXiangLai(Book):
    def getBookName(self):
        return "他知道风从哪个方向来"

    def getHeadReg(self):
        return ".*" + "85248" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "https://www.2kxs.com/xiaoshuo/85/85248/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_2KXiaoShuo()


############################################ 来自《猫扑小说》 ################################################################
class BookWeiQingHunAi(Book):
    def getBookName(self):
        return "危情婚爱，总裁宠妻如命"

    def getHeadReg(self):
        return ".*" + "49339" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://www.mpxiaoshuo.com/book/49339/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_MaoPu()


############################################ 来自《新书啦》 #############################################################
class BookWoDeLaoGongShiMingWang(Book):
    def getBookName(self):
        return "我的老公是冥王"

    def getHeadReg(self):
        return ".*" + "3769" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://www.xinshula.com/3/3769/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_XinShuLa()


############################################ 来自《随便看看吧》（需要代理？） #########################################################
class BookRenJianShiGe(Book):
    def getBookName(self):
        return "人间失格"

    def getHeadReg(self):
        return ".*" + "renjianshige" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://www.sbkk88.com/mingzhu/waiguowenxuemingzhu/renjianshige/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_SDKK88()

    def getHtmlRegOrderReverse(self):
        return True


############################################ 来自《骑士小说网》 ###########################################################
class BookTaWeiAnYeErSheng(Book):
    def getBookName(self):
        return "他为暗夜而声"

    def getHeadReg(self):
        return ".*" + "taweianyeersheng" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "https://www.xs74.com/novel/taweianyeersheng/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_XS74()


############################################ 来自《奇书楼小说网》 ###########################################################
class BookQuanZhiGaoShou(Book):
    def getBookName(self):
        return "全职高手"

    def getHeadReg(self):
        return ".*" + "quanzhi" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "https://www.qishulou.com/dushi/quanzhi/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_QiShuLou()


############################################ 来自《第九中文网》 ###########################################################
class BookZhiShiXiangLiaoNi(Book):
    def getBookName(self):
        return "只是想撩你"

    def getHeadReg(self):
        return ".*" + "14_14328" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://dijiuzww.com/14_14328/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_DiJiuZWW()


############################################ 来自《笔趣馆》 ###########################################################
class BookZhiShiXiangLiaoNi(Book):
    def getBookName(self):
        return "你微笑时很美"

    def getHeadReg(self):
        return ".*" + "bqg151519" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "https://www.biquguan.com/bqg151519/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_BiQuGuan()


############################################ 来自《乐文小说网》（已废弃） ################################################
class BookHenXiangHenXiangNi(Book):
    def getBookName(self):
        return "很想很想你"

    def getHeadReg(self):
        return ".*" + "6092" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://www.lwxs520.com/books/6/6092/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_LWXiaoShuo520()


class BookMiZhiYouYv(Book):
    def getBookName(self):
        return "蜜汁炖鱿鱼"

    def getHeadReg(self):
        return ".*" + "28748" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://www.lwxs520.com/books/28/28748/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_LWXiaoShuo520()


############################################ 来自《乐文小说》 （已废弃）###########################################################
class BookShiZhangFuRen(Book):
    def getBookName(self):
        return "市长夫人"

    def getHeadReg(self):
        return ".*" + "20621" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://www.lwxiaoshuo.com/20/20621/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_LeWenXiaoShuo()


class BookYanHuiXiMeiNan(Book):
    def getBookName(self):
        return "烟灰系美男"

    def getHeadReg(self):
        return ".*" + "44923" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://www.lwxiaoshuo.com/44/44923/index.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_LeWenXiaoShuo()


class BookYiZuoChengZaiDengNi(Book):
    def getBookName(self):
        return "一座城在等你"

    def getHeadReg(self):
        return ".*" + "68965" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://www.lwxiaoshuo.com/68/68965/index.html"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_LeWenXiaoShuo()

############################################ 来自《言情小说网》 ###########################################################
class BookFuQiJiaoHuan(Book):
    def getBookName(self):
        return "夫妻交换小说"

    def getHeadReg(self):
        return ".*" + "4609" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://www.7xxs.net/cbyq/4609/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_7xxs()

class BookTiaoJiaoYinDangXiaoMao(Book):
    def getBookName(self):
        return "淫荡小猫的调教"

    def getHeadReg(self):
        return ".*" + "5002" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://www.7xxs.net/cbyq/5002/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_7xxs()

class BookYinFuChiNv(Book):
    def getBookName(self):
        return "淫父痴女"

    def getHeadReg(self):
        return ".*" + "23968" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://www.7xxs.net/cbyq/23968/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_7xxs()

class BookSaoZiHeJi(Book):
    def getBookName(self):
        return "嫂子合集"

    def getHeadReg(self):
        return ".*" + "171" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://www.7xxs.net/cbyq/171/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_7xxs()

class BookYinLuanXiaoZhen(Book):
    def getBookName(self):
        return "淫乱小镇"

    def getHeadReg(self):
        return ".*" + "4594" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://www.7xxs.net/cbyq/4594/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_7xxs()

class BookZhiFuXiLie(Book):
    def getBookName(self):
        return "制服系列"

    def getHeadReg(self):
        return ".*" + "5151" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://www.7xxs.net/cbyq/5151"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_7xxs()

class BookJiaZuMeiFu(Book):
    def getBookName(self):
        return "家族美妇"

    def getHeadReg(self):
        return ".*" + "8522" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://www.7xxs.net/cbyq/8522"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_7xxs()

class BookJiaTingLuanLun1(Book):
    def getBookName(self):
        return "家庭乱伦1"

    def getHeadReg(self):
        return ".*" + "5182" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://www.7xxs.net/cbyq/5182"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_7xxs()

class BookXianWangLaWenHeJi1(Book):
    def getBookName(self):
        return "鲜网辣文合集1"

    def getHeadReg(self):
        return ".*" + "5141" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://www.7xxs.net/cbyq/5141"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_7xxs()

class BookXianWangLaWenHeJi2(Book):
    def getBookName(self):
        return "鲜网辣文合集2"

    def getHeadReg(self):
        return ".*" + "5484" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://www.7xxs.net/cbyq/5484"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_7xxs()

class BookXianWangLaWenHeJi3(Book):
    def getBookName(self):
        return "鲜网辣文合集3"

    def getHeadReg(self):
        return ".*" + "4588" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://www.7xxs.net/cbyq/4588"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_7xxs()

############################################ 来自《言情小说库》 ###########################################################
class BookHuanQi(Book):
    def getBookName(self):
        return "换妻"

    def getHeadReg(self):
        return ".*" + "huanqi2" + "/(.*)" + self.getHtmlLast() + ".*"

    def getHtml(self):
        return "http://www.yqk.net/yanqing/huanqi2/"

    def getScrapyType(self):
        return SpiderTypes.getTypeName_YanQingKu()
