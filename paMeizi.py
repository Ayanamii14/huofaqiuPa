from hfqPaNet import hfqRequest
from bs4 import BeautifulSoup
import os


class mzitu():

    def all_url(self, url):
        html = hfqRequest.get(url, 3)
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='all').find_all('a')
        for a in all_a:
            title = a.get_text()
            print(u'开始保存：', title)
            path = str(title).replace("?", '_')
            self.mkdir("/Users/liuyuhao/meizitu", path)
            os.chdir("D:/Users/liuyuhao/meizitu/" + path)
            href = a['href']
            self.html(href)

    def html(self, href):
        html = hfqRequest.get(href, 3)
        max_span = BeautifulSoup(html.text, 'lxml').find_all('span')[10].get_text()
        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            self.img(page_url)

    def img(self, page_url):
        img_html = hfqRequest.get(page_url, 3)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.save(img_url)

    def save(self, img_url):
        name = img_url[-9:-4]
        print(u'开始保存：', img_url)
        img = hfqRequest.get(img_url, 3)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    def mkdir(self, dirpath, filename):
        filename = filename.strip()
        nowpath = os.filename.join(dirpath, filename)
        isExists = os.filename.exists(nowpath)
        if not isExists:
            print(u'在', nowpath, '建了一个名字叫做', filename, u'的文件夹！')
            os.makedirs(nowpath)
            return True
        else:
            print(u'名字叫做', filename, u'的文件夹已经存在了！')
            return False


Mzitu = mzitu()  ##实例化
Mzitu.all_url('http://www.mzitu.com/all')  ##给函数all_url传入参数  你可以当作启动爬虫（就是入口）