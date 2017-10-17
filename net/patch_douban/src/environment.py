import os
import re


from net.patch_douban.src.FileOut import FileOut
from net.patch_douban.src.JieUtil import JieUtil
from net.patch_douban.src.Parses import Parses
from net.patch_douban.src.Patches import Patches
from net.patch_douban.src.Refresh import Refresh

@staticmethod
def getProjectDir():
    projectDir="E:/Users/Administrator/PycharmProjects/MyProject/net/patch_douban/"
    return projectDir
url_movies='https://movie.douban.com/nowplaying/hangzhou/'
common_url='https://movie.douban.com/subject/%s/comments?start=%d&limit=20'
pathes=Patches()
parses=Parses()
jieUtil=JieUtil()
projectDir =os.path.abspath('..')
print("projectDir=",projectDir)
outFile1=FileOut(projectDir+"\\out_file\\html_data.txt")
outFile2=FileOut(projectDir+"\\out_file\\soup.txt")
data = pathes.setUrl(url_movies).run()
if data==None:
    print('网络请求失败')
else:
    outFile1.out(data)
    movieList=parses.findMovieListByData(data)
    nowList=parses.getMainList(movieList)
    # 循环调用
    for index in range(nowList.__len__()):
        item = nowList.__getitem__(index)
        for i in range(10):
            num = i + 1
            url = common_url % (item['id'], num-1)
            print('title=%s, url=%s'%(item['name'], url))
            data_common = pathes.setUrl(url).run()
            cleaned_comments=parses.getCommonStr(data_common)
            jieDf = jieUtil.jieDf(cleaned_comments)
            words = jieUtil.loadStopWord(jieDf)
            # word_frequence_list = {'a':1,'b':10,'c':100,'d':1000}
            word_frequence_list = {}
            key_list = words.head(1000).sequence_list
            for key in key_list.keys():
                word_frequence_list.setdefault(key_list[key], key)
            jieUtil.showWordCloud(title=item['name'], dir_frequences=word_frequence_list)
            break
    pass
pass
