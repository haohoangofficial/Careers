import urllib.request
from bs4 import BeautifulSoup
class POST:
    def __init__(self):
        print('Hello')

class Get:
    def __init__(self,url,agent):
        self.url = url
        self.agent = agent

    def extractHTML(self):
        response = urllib.request.urlopen(self.url)
        html = response.read()
        encoding = response.headers.get_content_charset('utf-8')
        html_content = html.decode(encoding)
        html_text = BeautifulSoup(html_content, "html.parser")
        return html_text
    def userAgent(self):
        file = open('useragents.txt','r')
        body = file.readlines()
