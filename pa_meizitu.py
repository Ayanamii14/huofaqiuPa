import requests
import re

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
pa_url = 'https://www.mzitu.com/all'
pa_html = requests.get(pa_url, headers=headers)

'''
re.I 忽略大小写
re.M,将所有行的尾字母输出
'''
result = re.findall(r'<a href="[a-zA-Z0-9.:/]+" target="_blank">[a-zA-Z0-9\u4e00-\u9fa5！？\-.\s、：の，_!?,+]+</a>', pa_html.text, re.M|re.I)
for c in result:
    url_re = re.search(r'https://[a-zA-Z0-9/.]+', c, re.M|re.I)
    title_re = re.search(r'', c, re.M|re.I)
    print(url_re.group())
