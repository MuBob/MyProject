'''
html_downloader.py 上面爬虫流程图中的[下载器]
负责对指定的 URL 网页内容进行下载获取，这里只是简单处理了 HTTP CODE 200，实质应该依据 400、500 等分情况进行重试等机制处理。
'''
from http import cookiejar
from urllib import request, parse, error


class HtmlDownload:
    def down1(self, url, retry_count=3, headers=None, proxy=None, data=None):
        if url is None:
            return
        try:
            req = request.Request(url, headers=headers, data=data)
            cookie_jar = cookiejar.CookieJar()
            cookie_processor = request.HTTPCookieProcessor(cookie_jar)
            opener = request.build_opener()

            if proxy:
                proxies = {parse.urlparse(url).scheme(): proxy}
                opener.add_handler(request.ProxyHandler(proxies))
            content = opener.open(req).read()
        except error.URLError as e:
            print("HtmlDownLoader download error:",e.reason)
            content=None
            if retry_count>0:
                if hasattr(e,'code') and 500<= e.code< 600:
                    return self.down(url, retry_count-1, headers, proxy. data)

        return content

    def down2(self, url, retry_count=3, headers=None, proxy=None, data=None):
        if url is None:
            return
        try:
            req = request.Request(url, headers=headers, data=data)
            cookie_jar = cookiejar.CookieJar()
            cookie_processor = request.HTTPCookieProcessor(cookie_jar)
            opener = request.build_opener()

            if proxy:
                proxies = {parse.urlparse(url).scheme(): proxy}
                opener.add_handler(request.ProxyHandler(proxies))
            content = request.urlopen(req).read()

        except error.URLError as e:
            print("HtmlDownLoader download error:", e.reason)
            content = None
            if retry_count > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:
                    return self.down(url, retry_count - 1, headers, proxy.data)

        return content

    def down(self, url, retry_count=3, headers=None, proxy=None, data=None):
        return self.down2(url, retry_count, headers, proxy, data)
