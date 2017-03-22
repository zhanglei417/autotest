#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输入三个数字 正序倒序分别输出list

l = []
for i in range(3):
    x = int(raw_input('integer:\n'))
    l.append(x)
l.sort()
print l
l.reverse()
print l