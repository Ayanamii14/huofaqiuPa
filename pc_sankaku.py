import requests
from bs4 import BeautifulSoup
import os
import re
import threading
from hfqPaNet import hfqRequest


begin_index = 650000
max_index = 715418
thread_num = 5;
loop_time_index = 0;
loop1_index = begin_index + 0
loop2_index = begin_index + 1
loop3_index = begin_index + 2
loop4_index = begin_index + 3
loop5_index = begin_index + 4


class SankakuUrl():

    def __init__(self):
        # 浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

    #pa
    def paurlrequest(self, url):
        content = hfqRequest.get(url, 3)
        return content

    def paAll(self, urlhref, index):
        pageUrl = urlhref + str(index)
        img_html = self.paurlrequest(pageUrl)
        if img_html.status_code == 200:
            # 图片url
            img_url = BeautifulSoup(img_html.text, "lxml").find("a", id="highres")["href"]
            self.pa_save(img_url, index)
        else:
            print("error:", index)

    def pa_mkdir(self):
        file_path = "M:\sankakuComplex_tu"
        isExists = os.path.exists(file_path)
        if not isExists :
            print(u"创建完成", "->", file_path)
            os.makedirs(file_path)
            # 切换目录
            os.chdir(file_path)
            return True
        else :
            print(u"已经存在")
            return False

    def pa_save(self, img_url, index):
        # 正则匹配
        searchObj = re.search(r'(?:jpg|gif|mp4|png)', img_url)
        if searchObj:
            imgtype = searchObj.group()
            img = self.paurlrequest("https:" + img_url)
            f = open(str(index) + "." + imgtype, "wb")
            f.write(img.content)
            f.close()

# 执行
pachong = SankakuUrl()
pachong.pa_mkdir()

# 爬50张就休息一下
def loop(loop_index):
    while loop_index < max_index:
        pachong.paAll("https://idol.sankakucomplex.com/post/show/", loop_index)
        loop_index = loop_index + thread_num


def loop1():
    loop(loop1_index)

def loop2():
    loop(loop2_index)


def loop3():
    loop(loop3_index)

def loop4():
    loop(loop4_index)

def loop5():
    loop(loop5_index)

t1 = threading.Thread(target=loop1, name='LoopThread1')
t2 = threading.Thread(target=loop2, name='LoopThread2')
t3 = threading.Thread(target=loop3, name='LoopThread3')
t4 = threading.Thread(target=loop4, name='LoopThread4')
t5 = threading.Thread(target=loop5, name='LoopThread5')
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()