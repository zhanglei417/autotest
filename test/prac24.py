#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 逗号分隔列表

L = [1,2,3,4,5]
for n in L:
    print str(n)
# join用法，前面的插入到后面的序列中
s1 = ','.join(str(n) for n in L)
print s1