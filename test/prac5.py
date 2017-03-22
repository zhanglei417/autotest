#!/usr/bin/python
# -*- coding: UTF-8 -*-

for i in range(1, 10):
    print
    for j in range(1, i+1):
        # i j i*j 赋值给d%
        print "%d*%d=%d" % (i, j, i*j),