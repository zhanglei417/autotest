#coding:utf-8
# 可以直接import本地的文件

import testmethod1
# 可以import包下面的模块儿，包为文件夹，文件夹下必须有init.py
import test.testmethod1 as c
# 可以as一个其他名字
import testmethod1 as t

# 可以从模块中导入一个方法
from testmethod1 import *

import test

c.test(234)
testmethod1.test(123)
t.test(123)
test(123)
# 由于包中国的init文件中将方法导入成a，所以可以直接import包后按包名调用，推荐此方法。
test.a.test(456);