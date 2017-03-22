# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

x = int(raw_input("请输入一个数:\n"))

a = x / 10000
b = x / 1000 % 10
c = x / 100 % 10
d = x / 10 % 10
e = x % 10

if a == e and b == d:
    print "这是一个回文数"
else:
    print "这不是一个回文数"