#coding:utf-8

import os,sys,time
f=open("/Users/phoenixzhang/Downloads/test.txt",'w')

print '===============================开始内存测试==============================='
start = time.time()
os.system('adb -host shell procrank -p |grep -E \'Pss\' >>~/Downloads/test.txt')

for i in range(3):
    os.system('adb -host shell procrank -p |grep \'SettingsHome\' >>~/Downloads/test.txt')
    print '==================================第' + str(i+1) + '次=================================='
    time.sleep(1)
c = time.time() - start

print('测试运行耗时:%0.2f'%(c) + '秒')

print '===============================内存测试完毕==============================='

fr=open("/Users/phoenixzhang/Downloads/test.txt",'r')
lines = fr.readlines()
for line in lines:
    print line
