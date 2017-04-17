#!/usr/bin/python
# -*- coding: UTF-8 -*-


l = []
l1 = []
l2 = []
m = "the sky is blue "
print "输入字符串为：" + m
n = list(m)
for i in range(len(n)):
    l.append(n[i])
    if n[i] == " ":
        l1.append("".join(l))
        l = []
print "临时列表为："
print l1
for i in range(len(l1)-1,-1,-1):
    l2.append(l1[i])
print "输出字符串为：" + "".join(l2)
