#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
# 将一个数组逆序输出。

l = [1,5,8,15,21]
j =[]
s = 19

l.append(s)
for i in range(len(l)-2,-1,-1):
    temp = s
    if l[i] > s:
        l[i + 1] = l[i]
    else:
        l[i + 1] = s
        break
print l

for i in range(len(l)-1,-1,-1):
    j.append(l[i])
print j
# 以下方法也可逆序输出
print l[::-1]