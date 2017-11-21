#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 测试百度api
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: test_baidu_http.py
# @time: 17/11/21 下午3:11

import unittest
from utils.config import Config, REPORT_PATH
from utils.client import HttpClient
from utils.log import logger
from utils.HTMLTestRunner import HTMLTestRunner


class TestBaiduHttp(unittest.TestCase):
    URL = Config().get('URL')

    def setUp(self):
        self.client = HttpClient(url=self.URL, method='GET')

    def test_baidu_http(self):
        res = self.client.send()
        logger.debug(res.text)
        self.assertIn('关于百度', res.text)

if __name__ == '__main__':
    report = REPORT_PATH + '/report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='测试接口', description='接口html报告')
        runner.run(TestBaiduHttp('test_baidu_http'))
