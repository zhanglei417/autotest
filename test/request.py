#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
import json

def zp(r):
    try:
        print(json.dumps(json.loads(r.text), indent=4,ensure_ascii=False, encoding="utf-8"))
    except Exception, e:
        print r.text

def login():
    data = {'userName': '15827241843', 'password': '123456'}
    r = requests.post("http://localhost:5000/Login", data=data)
    zp(r)


def logout():
    r = requests.get("http://www.sina.com")
    zp(r)


def RouteStation():
    url = "http://localhost:5000/RouteStation?"
    url += "fromAdress=1"
    url += "&toAddress=2"
    url += "&date=2015-08-20"
    r = requests.get(url)
    zp(r)

logout()
