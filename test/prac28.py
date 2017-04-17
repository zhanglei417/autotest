#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 排序

N = 4
l = [4,3,2,1]
for i in range(N - 1):
    n = i
    for j in range(i + 1, N):
        if l[n] > l[j]:
            m = j
            l[i],l[m] = l[m],l[i]
            print l
print 'after sorted'
for i in range(N):
    print l[i]
