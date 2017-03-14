#coding:utf-8
# 函数定义方式：def 函数名（参数列表）：


def test(a):
    # global定义全局变量，若不注释则i为局部变量
    global i;
    i = 7;
    print (a)
    print i
test(123)

# 判断如果name是main则为直接调用，可以执行下面print方法。否则不执行。可以使import1引入时不执行下面print方法。
if __name__ == "__main__":
    print i + 1

