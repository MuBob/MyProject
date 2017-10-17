import re

from bs4 import BeautifulSoup as bs

from net.patch_douban.src.Refresh import Refresh


class Parses:
    def parseSoupByHtmlData(self, html_data):
        soup = bs(html_data, 'html.parser')
        return soup
    def findDivListById(self, soup, id):
        div = soup.find_all(name='div', id=id)
        return div

    def findDivListByClass(self, soup, class_):
        div = soup.find_all(name='div', class_=class_)
        return div

    def findListByClass(self, list, class_):
        length = len(list)
        if(length>0):
            nowplaying_movie_list = list[0].find_all('li', class_=class_)
            return nowplaying_movie_list
        else:
            return None

    def findListInP(self, list):
        eachList = [];
        for item in list:
            p_ = item.find_all('p')[0].string
            if p_ is not None:
                eachList.append(p_)
        return eachList

    def findMovieListByData(self, data):
        soup = self.parseSoupByHtmlData(data)
        nowplaying_movie = self.findDivListById(soup, 'nowplaying')
        movieList = self.findListByClass(nowplaying_movie, 'list-item')
        return movieList

    def findCommonListByData(self, data):
        soup=self.parseSoupByHtmlData(data)
        commentList = self.findDivListByClass(soup, 'comment')
        return commentList

    def getMainList(self, movieList):
        list=[]
        for item in movieList:
            list_dic={}
            list_dic['id']=item['data-subject']
            for tag_image_item in item.findAll('img'):
                list_dic['name']=tag_image_item['alt']
                list.append(list_dic)
        return list

    def getCommonStr(self, data_common):
        if data_common == None:
            print('当前电影%s的url请求失败：%s' % (item['name'], url))
        else:
            list_by_data = self.findCommonListByData(data_common)
            # print('listByData=', list_by_data)
            list_by_class = self.findListInP(list_by_data)
            # print('listByClas=', list_by_class)
            # outFile_Common = FileOut(projectDir + "out_file/common_data_%s.txt" % (item['name']))
            # outFile_Common.out(list_by_class.__str__())
            str_from_list = Refresh().getStrFromList(list_by_class)
            pattern = re.compile(r'[\u4e00-\u9fa5]+')
            filterdata = re.findall(pattern, str_from_list)
            cleaned_comments = ''.join(filterdata)
            return cleaned_comments
