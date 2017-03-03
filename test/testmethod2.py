#coding:utf-8
# 函数定义方式：def 函数名（参数列表）：
# 函数返回值使用语句return


def test(a,b):
    return a,b;
# 一个变量接收，结果为元祖
i = test(123,234);
print i,i[0],i[1];
# 多个变量接收，结果为相应的变量,一定要一致否则报错ValueError: need more than 2 values to unpack
a,b = test(123,234);
print a,b;

