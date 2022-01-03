import urllib.request
from bs4 import BeautifulSoup
class Dom:
    def __init__(self,url):
        self.url = url
    def extractHTML(self):
        response = urllib.request.urlopen(self.url)
        html = response.read()
        encoding = response.headers.get_content_charset('utf-8')
        html_content = html.decode(encoding)
        html_text = BeautifulSoup(html_content,"html.parser")
        return html_text
