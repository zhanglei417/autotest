# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
# str为字符串 str.isalnum() 所有字符都是数字或者字母 str.isalpha() 所有字符都是字母 str.isdigit()
# 所有字符都是数字 str.islower() 所有字符都是小写 str.isupper() 所有字符都是大写
# str.istitle() 所有单词都是首字母大写，像标题 str.isspace() 所有字符都是空白字符、\t、\n、\r


s = raw_input('输入分数:')


def score_level(s):
    if 100 >= int(s) >= 90:
        grade = 'A'
    elif 60 <= int(s) <= 90:
        grade = 'B'
    elif 0 <= int(s) <= 59:
        grade = 'C'
    else:
        grade = 'not valid'
    print '%s belongs to %s' % (s, grade)

if s.isdigit():
    score_level(s)
else:
    print "not a number"

