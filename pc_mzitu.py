import requests
from bs4 import BeautifulSoup
import os
import re

class pameizi():

    def __init__(self):
        # 浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

    def all_url(self, url):
        start_html = self.pa_request(url)
        result = re.findall(
            r'<a href=[a-zA-Z0-9\u4e00-\u9fa5."<> =:/]+ target="_blank">[a-zA-Z0-9\u4e00-\u9fa5！？\-. 、：の，_!?,+]+</a>',
            start_html.text, re.M | re.I)
        for c in result:
            url_re = re.search(r'https://[a-zA-Z0-9/.]+', c, re.M | re.I)

        all_a = BeautifulSoup(start_html.text, "lxml").find("div", class_ = "all").find_all("a")
        for a in range(len(all_a)) :
            if a == 0:
                continue
            title = all_a[a].get_text()
            print(u"开始保存: ", title)
            ismkdir = self.pa_mkdir(self.pa_removeIllgalChar(str(title), "_"))
            if not ismkdir :
                continue
            href = all_a[a]["href"]
            self.pa_html(href)

    def pa_html(self, href):
        html = self.pa_request(href)
        self.headers["referer"] = href
        max_span = BeautifulSoup(html.text, "lxml").find("div", class_="pagenavi").find_all("span")[-2].get_text()
        for page in range(1, int(max_span) + 1):
            page_url = href + "/" + str(page)
            self.pa_img(page_url)

    def pa_img(self, page_url):
        img_html = self.pa_request(page_url)
        img_url = BeautifulSoup(img_html.text, "lxml").find("div", class_ = "main-image").find("img")["src"]
        self.pa_save(img_url)

    def pa_save(self, img_url):
        img_name = img_url[-9: -4]
        img = self.pa_request(img_url)
        f = open(img_name + ".jpg", "ab")
        f.write(img.content)
        f.close()

    def pa_mkdir(self, path):
        # 去掉两端的空格
        path = path.strip()
        file_path = "M:\pameizi_tu"
        isExists = os.path.exists(os.path.join(file_path, path))
        if not isExists :
            print(u"创建完成", "->", file_path, path)
            os.makedirs(os.path.join(file_path, path))
            # 切换目录
            os.chdir(os.path.join(file_path, path))
            return True
        else :
            print(u"已经存在", "->", path)
            return False

    def pa_request(self, url):
        content = requests.get(url, headers = self.headers)
        return content

    def pa_removeIllgalChar(self, string, toString):
        # 替换不合法字符(windows)
        path = str(string).replace("\\", toString)
        path = path.replace("/", toString)
        path = path.replace(":", toString)
        path = path.replace("*", toString)
        path = path.replace("?", toString)
        path = path.replace("\"", toString)
        path = path.replace("<", toString)
        path = path.replace(">", toString)
        path = path.replace("|", toString)
        return path

#执行
pmz = pameizi()
pmz.all_url("http://www.mzitu.com/all")