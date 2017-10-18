'''
url_manager.py 上面爬虫流程图中的[URL 管理器]
负责管理深度 URL 链接和去重等机制。
'''


class UrlManager:
    def __init__(self):
        self.new_urls = set()
        self.used_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.used_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) <= 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls)

    def get_new_url(self):
        pop_url = self.new_urls.pop()
        self.used_urls.add(pop_url)
        return pop_url

    def get_url_count(self):
        if self.new_urls is None:
            return 0
        return len(self.new_urls)