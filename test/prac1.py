#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 输出1到5组成的每一位都不重复的三位数
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != k) and (i != j) and (j != k):
                print i, j, k