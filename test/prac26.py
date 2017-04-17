#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 文本颜色设置。

#!/usr/bin/python
# -*- coding: UTF-8 -*-

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC
print bcolors.OKBLUE + "蓝色字体?" + bcolors.ENDC
print bcolors.OKBLUE + bcolors.BOLD + "蓝色加粗字体?" + bcolors.ENDC
print bcolors.OKGREEN + bcolors.UNDERLINE + "蓝色加粗字体?" + bcolors.ENDC



# ===============================================ANSI控制码的说明
# \33[0m 关闭所有属性
# \33[1m 设置高亮度
# \33[4m 下划线
# \33[5m 闪烁
# \33[7m 反显
# \33[8m 消隐
# \33[30m -- \33[37m 设置前景色
# \33[40m -- \33[47m 设置背景色
# \33[nA 光标上移n行
# \33[nB 光标下移n行
# \33[nC 光标右移n行
# \33[nD 光标左移n行
# \33[y;xH设置光标位置
# \33[2J 清屏
# \33[K 清除从光标到行尾的内容
# \33[s 保存光标位置
# \33[u 恢复光标位置
# \33[?25l 隐藏光标
# \33[?25h 显示光标
