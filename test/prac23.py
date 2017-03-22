# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 按相反的顺序输出列表的值。

s = list(raw_input('输入列表:'))
l = len(s)

for i in s[::-1]:
    print i

for i in range(l,0,-1):
    print s[i-1]