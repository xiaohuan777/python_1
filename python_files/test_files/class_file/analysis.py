
from urllib import request
import re

class Spider():
    url = 'http://www.sohu.com/'
    root_pattern = '<div class="news">([\s\S]*?)</div>'
    p_pattern = '<p>([\s\S]*?)</p>'
    name_pattern = 'title=\'([\s\S]*?)\\\'>'
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        
        
        for html in root_html:
            p_html = re.findall(Spider.p_pattern, html)
            # print(p_html)

        for html in p_html:
            a_html = re.findall(Spider.name_pattern, html)
            print(a_html)
        
        # print(p_html)

   
    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)

s1 = Spider()
s1.go()
