'''
html_parser.py 上面爬虫流程图中的[解析器]
负责对下载器下载下来的网页内容进行解析，解析规则就是我们自己定义的感兴趣的内容，这里我们只分析网页后解析出 url、title、content，其他的不关心，解析好的数据通过字典返回。
'''
from urllib.parse import urljoin

import re
from bs4 import BeautifulSoup
from numpy.core.defchararray import strip


class HtmlParser:
    def parser(self, url, content, encoding='utf-8', key=None):
        if url is None or len(url) <= 0:
            return
        soup = BeautifulSoup(content, "html.parser", from_encoding=encoding)
        urls = self._get_new_urls(url, soup)
        data = self._get_new_data(url, soup, key)
        if data==None:
            return None, None
        else:
            return urls, data

    def _get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/item/\w+"))
        for link in links:
            url_path = link["href"]
            new_url = urljoin(url, url_path)
            new_urls.add(new_url)
        return new_urls

    def _get_new_data(self, url, soup, key):
        data = {'url': url}
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title_node.get_text().strip()
        summary_node = soup.find('div', class_='lemma-summary')
        data['summary'] = summary_node.get_text().strip()
        print("summary=%s, key=%s"%(data['summary'], key))
        if data['title'].find(key)==0|data['summary'].find(key)==0:
            print("has=", data['summary'].find(key))
            return data
        else:
            return None
