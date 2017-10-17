from urllib import request
class Patches:
    __url=""
    def setUrl(self, url):
        self.__url=url
        return self
    def run(self):
        try:
            resp = request.urlopen(self.__url)
            html_data = resp.read().decode('utf-8')
            return html_data
        except:
            print('发生异常请求')
            return None