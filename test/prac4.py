import copy
# 五种复制python中列表方法
a = [1, 2, 3, ['a', 'b']]
b = a
c = a[:]
d = copy.copy(a)
e = copy.deepcopy(a)
print "a         ", a
print "=         ", b
print "[:]       ", c
print "copy      ", d
print "deepcopy  ", e
print
