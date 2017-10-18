from SpiderLearn.UrlManager import UrlManager
from SpiderLearn.FileOutput import FileOutput
from SpiderLearn.HtmlDownload import HtmlDownload
from SpiderLearn.HtmlParser import HtmlParser


class SpiderMain:
    def __init__(self):
        self.url_manager = UrlManager()
        self.download = HtmlDownload()
        self.htmp_parser = HtmlParser()
        self.output = FileOutput()

    def craw(self, url):
        if url is None or len(url) <= 0:
            return
        count = 1
        self.url_manager.add_new_url(url)
        while self.url_manager.has_new_url():
            try:
                new_url = self.url_manager.get_new_url()
                headers = {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36"
                }
                html_content = self.download.down(new_url, retry_count=2, headers=headers)
                print('craw=%d, url=%s, content=%s' % (count, new_url, html_content))
                new_urls, new_data = self.htmp_parser.parser(new_url, html_content, key="Android")
                print('newUrls.size=%d, data.size=%s' % (len(new_urls), len(new_data)))
                self.url_manager.add_new_urls(new_urls)
                print('urlManager=',self.url_manager.get_url_count())
                self.output.collect_data(new_data)
                if count >= 30:
                    break
                count += 1
            except Exception as e:
                print("craw failed! e=" + str(e))
            self.output.output_file()


if __name__ == '__main__':
    rootUrl = "http://baike.baidu.com/item/Android"
    SpiderMain().craw(rootUrl)
