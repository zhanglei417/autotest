# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。


Tn = 0
Sn = []
n = int(raw_input('n = :\n'))
a = int(raw_input('a = :\n'))
for count in range(n):
    Tn += a
    a *= 10
    Sn.append(Tn)
    print Tn
#  lambda表达式快速定义函数表示定义x，y为参数的函数，返回x+y，
#  reduce为循环操作list中的前两个元素，返回值再和第三个元素迭代，
#  操作函数为之前给的lambda或者其他function
Sn = reduce(lambda x, y: x+y,Sn)
print Sn

