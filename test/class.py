#coding:utf-8

class people:
# '所有人的基类'
    empCount = 0

#  以下相当于构造函数，构造对象为对象名(参数列表)
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        people.empCount += 1

    def displaycount(self):
        print "Total people %d" % people.empCount

    def displayemployee(self):
        print "Name : ", self.name, ", sex: ", self.sex

zhanglei = people("zhang","man")
print zhanglei
# 查看实例有哪些属性
print zhanglei.__dict__
# 为实例添加属性
zhanglei.hobby = "football"
# 查看实例所属类的属性列表
print zhanglei.__class__.__dict__
print zhanglei.__dict__
print zhanglei.name
print zhanglei.sex
zhanglei.displaycount()
zhanglei.displayemployee()