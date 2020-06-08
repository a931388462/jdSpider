import urllib.request

class HtmlDownloader(object):
    def download(self, url):
        #伪装成浏览器发起请求
        headers = ('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36')
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        # 开始请求url
        response = opener.open(url)
        if url is None:
            return None
        if response.getcode() != 200:
            return  None
        return  response.read()
