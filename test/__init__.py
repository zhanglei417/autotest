#coding:utf-8
# 函数定义方式：def 函数名（参数列表）：


def test(a):
    # global定义全局变量
    global i;
    i = 7;
    print (a)
    print i
test(123)
print i;
