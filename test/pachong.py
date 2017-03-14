#coding:utf-8

import urllib
import re

# 功能为获取html


def get_html(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

# 利用正则获取图片地址


def getImg(html):
    reg = r'(?<=<img src=)"([^"]+\.jpg)"'
    # reg = r'"([^"]+\.jpg)"'   也可以
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html);
    x = 0
    for imgurl in imglist:
# %s意思是字符串参数，就是将变量的值传入到字符串里面，字符串后的'%'后就是写要传入的参数。
        urllib.urlretrieve(imgurl, './img/%s.jpg' % x)
        x += 1
    return imglist
html = get_html("http://www.xiazaizhijia.com/zt/91612.html")
# print html
print getImg(html)



