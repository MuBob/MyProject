import jieba
import os
import matplotlib as matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from xpinyin import Pinyin

matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
import matplotlib

from wordcloud import WordCloud  # 词云包

class JieUtil:
    def jieDf(self, str):
        segment = jieba.lcut(str)
        words_df = pd.DataFrame({'sequence_list': segment})
        return words_df

    def loadStopWord(self, words_df):
        abspath =os.path.abspath('..')
        stopwords = pd.read_csv(abspath+"\\word_util\\stop_words_zh_UTF-8.txt",
                                index_col=False,
                                quoting=3,
                                sep="\t",
                                names=['stopword'],
                                encoding='utf-8')  # quoting=3全不引用
        words = words_df[~words_df.sequence_list.isin(stopwords.stopword)]
        return words

    def canculate(self, words):
        words_stat = words.groupby(by=['segment'])['segment'].agg({"计数": numpy.size})
        words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)
        return words_stat

    def showWordCloud(self, title=None, dir_frequences=None):
        if dir_frequences==None:
            print('JieUtil.showWordCloud.dir_frequences==None!!!!!!!!!!!!!!!!!!')
        abspath = os.path.abspath('..')
        wordcloud = WordCloud(font_path=abspath+"\\word_util\\simhei.ttf",
                              background_color="white",
                              max_font_size=80)  # 指定字体类型、字体大小和字体颜色
        wordcloud.fit_words(dir_frequences)
        plt.imshow(wordcloud)
        plt.axis("off")
        pinyin = Pinyin()
        if title!=None:
            get_pinyin = pinyin.get_pinyin(chars=title, show_tone_marks=True)
            plt.title(get_pinyin)
        plt.show()