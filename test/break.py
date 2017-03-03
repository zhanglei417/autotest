#coding:utf-8
# break语句强制停止循环执行

for i in range(1,8):
    if i == 5:
        break
    print i
a = 1
while a:
    a += 1
    if a == 5:
        break
    print a

