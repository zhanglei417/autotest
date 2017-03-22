#coding:utf-8
s = list(raw_input('输入小写英文字符串:'))
# s=list("aabbbbccdddddaaaccc")
result_list=[]

for i in range(ord('a'), ord('z')):
    count = 0
    for j in range(0,len(s)):
        if s[j] == chr(i):
            count += 1
    if count != 0:
        result_list.append(chr(i))
        result_list.append(str(count))

print "统计结果是：" + ''.join(result_list)