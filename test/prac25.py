#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 函数调用

def hello_world():
    print 'hello world'

def three_hellos():
    for i in range(3):
        hello_world()
if __name__ == '__main__':
    three_hellos()
else:
    hello_world()