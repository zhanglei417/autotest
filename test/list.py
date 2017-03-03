#coding:utf-8
# 列表定义

students = ["a", "b", "c", "d"]
print students
# 替换
students[1] = "f"
print students

# 元祖无法修改

students = ("a", "b", "c", "d")
print students

# set集合

a = set("ababababasdsdsdfasdasd")
b = set("abt")
# 求交集
x=a&b
print x

# 并集
x=a|b
print x

# 差集
x=a-b
print x

# 去除重复元素
print set(a)

# 字典
zidian = {'name':'zhanglei', 'age':16, 'address':'taoranting'}
print zidian
print zidian['name']
# 添加与修改
zidian['age']=15
zidian['aihao']='football'
print zidian['age']
print zidian