#coding:utf-8

import subprocess

"""
过滤出占用8080端口的进程，并杀掉
"""

#获取占用8080端口的进程的pid
pid_port_8080=subprocess.getstatusoutput("lsof -i:5037 |awk '{print $2}'|grep -oE '[0-9]*$'|sort -r|head -n 1")
#杀
subprocess.getstatusoutput('kill '+ pid_port_8080[1])