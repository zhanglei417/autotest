#coding:utf-8
import os,sys,time
os.system('adb -host shell mkdir test')
os.system('adb -host push /Users/phoenixzhang/Downloads/plover/runtime/test/testMain.js /test')
os.system('adb -host push /Users/phoenixzhang/Downloads/plover/runtime/test/configtest.json /test')
time.sleep(1)
f=open("/Users/phoenixzhang/Downloads/autotest.txt",'w')

print '===============================开始测试==============================='
start = time.time()
os.system('adb -host shell testrbc -f /test/configtest.json -r >>~/Downloads/autotest.txt')

# for i in range(300):
#     os.system('adb -host shell procrank -p |grep \'SettingsHome\' >>~/Downloads/autotest.txt')
#     print '==================================第' + str(i+1) + '次=================================='
#     time.sleep(1)
c = time.time() - start

print('测试运行耗时:%0.2f'%(c) + '秒')

print '===============================测试完毕==============================='
os.system('adb -host pull /var/log/test ~/Downloads/testreport')
time.sleep(1)
os.system('adb -host shell rm -rf /var/log/test/*')
time.sleep(1)
os.system('sh ~/Downloads/apacheshell/test.sh')
time.sleep(1)
# os.system('cp -R ~/Downloads/testreport/*/* ~/Downloads/test')
# time.sleep(1)
os.system('rm -rf ~/Downloads/testreport/*')
time.sleep(1)
fr=open("/Users/phoenixzhang/Downloads/autotest.txt",'r')
lines = fr.readlines()
for line in lines:
    print line
