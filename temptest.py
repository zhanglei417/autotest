import os,sys,time
os.system('/Users/phoenixzhang/Downloads/yunos-sdk_v0.2.5_20161222.1220/tools/adb/adb -host shell mount -o remount, rw /')
os.system('/Users/phoenixzhang/Downloads/yunos-sdk_v0.2.5_20161222.1220/tools/adb/adb -host shell mkdir test')
os.system('/Users/phoenixzhang/Downloads/yunos-sdk_v0.2.5_20161222.1220/tools/adb/adb -host push /Users/phoenixzhang/Downloads/plover/runtime/test/testMain.js /test')
os.system('/Users/phoenixzhang/Downloads/yunos-sdk_v0.2.5_20161222.1220/tools/adb/adb -host push /Users/phoenixzhang/Downloads/plover/runtime/test/configtest.json /test')
time.sleep(1)
f=open("/Users/phoenixzhang/Downloads/autotest.txt",'w')

os.system('/Users/phoenixzhang/Downloads/yunos-sdk_v0.2.5_20161222.1220/tools/adb/adb -host shell testrbc -f /test/configtest.json -r >>~/Downloads/autotest.txt')

os.system('/Users/phoenixzhang/Downloads/yunos-sdk_v0.2.5_20161222.1220/tools/adb/adb -host pull /var/log/test ~/Downloads/testreport')
time.sleep(1)
os.system('/Users/phoenixzhang/Downloads/yunos-sdk_v0.2.5_20161222.1220/tools/adb/adb -host shell rm -rf /var/log/test/*')
time.sleep(1)
os.system('sh ~/Downloads/apacheshell/test.sh')
time.sleep(1)
# os.system('sh ~/Downloads/apacheshell/testscr.sh')
# time.sleep(1)
os.system('rm -rf ~/Downloads/testreport/*/screenshot')
time.sleep(1)
os.system('rm -rf ~/Downloads/testreport/*')
time.sleep(1)
fr=open("/Users/phoenixzhang/Downloads/autotest.txt",'r')
lines = fr.readlines()
for line in lines:
    print line
