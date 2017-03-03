#coding:utf-8
# 文档字符串是，编写使用三引号


def test(a):
    '''
    Param a: 输入参数a。
    return: 无返回值。
    '''
    print a;

def testb(b):
    '''
    Param b: 输入参数b。
    return: 无返回值。
    '''
    print a;
# 输出文档字符串
print test.__doc__
# help方法输出帮助信息
help(test)
help(testb)
