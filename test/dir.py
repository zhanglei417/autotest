#coding:utf-8
# sys模块

import sys

# dir为查看模块功能列表。
print dir(sys)

# dir也可查看某一个对象属性的功能列表不包含数据
a = []
b = [1,2]
c = (1,2)
d = "a"
e = 1
print dir(a)
print dir(b)
print dir(c)
print dir(d)
print dir(e)