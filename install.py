#coding:utf-8

import os,sys,time

# python脚本 持续将apk push入系统并安装 运行adb jenkins需要adb绝对的路径
os.system('/Users/phoenixzhang/Downloads/yunos-sdk_v0.2.5_20161222.1220/tools/adb/adb push /Users/phoenixzhang/AndroidStudioProjects/Activity03/app/build/outputs/apk/app-debug.apk /data/local/tmp/com.example.phoenixzhang.activity03')
time.sleep(2)
os.system('/Users/phoenixzhang/Downloads/yunos-sdk_v0.2.5_20161222.1220/tools/adb/adb shell pm install -r "/data/local/tmp/com.example.phoenixzhang.activity03"')
