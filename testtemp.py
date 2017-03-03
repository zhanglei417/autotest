#coding:utf-8
import os,sys,time
os.system('/Users/phoenixzhang/Downloads/yunos-sdk_v0.2.5_20161222.1220/tools/adb/adb -host shell mkdir test')
os.system('/Users/phoenixzhang/Downloads/yunos-sdk_v0.2.5_20161222.1220/tools/adb/adb -host push /Users/phoenixzhang/Downloads/plover/runtime/test/testMain.js /test')
os.system('/Users/phoenixzhang/Downloads/yunos-sdk_v0.2.5_20161222.1220/tools/adb/adb -host push /Users/phoenixzhang/Downloads/plover/runtime/test/configtest.json /test')
time.sleep(1)


print '===============================开始测试==============================='
start = time.time()
os.system('/Users/phoenixzhang/Downloads/yunos-sdk_v0.2.5_20161222.1220/tools/adb/adb -host shell testrbc -f /test/configtest.json -r')

print '===============================测试完毕==============================='
os.system('/Users/phoenixzhang/Downloads/yunos-sdk_v0.2.5_20161222.1220/tools/adb/adb -host pull /var/log/test ../Users/phoenixzhang/Downloads/testreport')
time.sleep(1)
# os.system('/Users/phoenixzhang/Downloads/yunos-sdk_v0.2.5_20161222.1220/tools/adb/adb -host shell rm -rf /var/log/test/*')
# time.sleep(1)
os.system('/bin/sh ../Users/phoenixzhang/Downloads/apacheshell/test.sh')
time.sleep(1)
os.system('rm -rf ../Users/phoenixzhang/Downloads/testreport/*')
time.sleep(1)

