# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。


def reverse(m,n):
    if n == 0:
        return
    print (m[n-1])
    reverse (m,n-1)

s = raw_input('Input a string:')
l = len(s)
reverse(s,l)
