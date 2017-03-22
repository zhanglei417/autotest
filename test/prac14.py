# !/usr/bin/python

# -*- coding: UTF-8 -*-


# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

# !/usr/bin/python
# -*- coding: UTF-8 -*-

tour = []
height = []
hei = 100.0  # 起始高度
tim = 10  # 次数

for i in range(1, tim + 1):
    tour.append(hei)
    hei /= 2
    height.append(hei)
# format为按前面格式化输出后面format的结果 http://www.jb51.net/article/63672.htm
print '{0}'.format('test', 2, 3)
print('总高度：tour = {0}'.format(sum(tour)))
print('第10次反弹高度：height = {0}'.format(height[-1]))