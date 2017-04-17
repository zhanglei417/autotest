# -*- coding:utf-8 -*-
import unittest
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
import datetime
import random


class MyIOSTests(unittest.TestCase):
    def setUp(self):
        app = os.path.join(os.path.dirname(__file__),
                           '/Users/phoenixzhang/Library/Developer/Xcode/DerivedData/test2-bpldwizfqdeltofwovppwrtgzhyh/Build/Products/Debug-iphonesimulator',
                           'test2.app')
        app = os.path.abspath(app)
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '10.2',
                'deviceName': 'iPhone 6s Plus'
            })