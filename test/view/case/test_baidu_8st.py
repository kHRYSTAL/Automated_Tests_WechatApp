#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: test_baidu_8st.py
# @time: 17/11/21 下午2:35


import time
import unittest

from test.view.page.baidu_result_page import BaiduResultPage, BaiduMainPage
from utils.HTMLTestRunner import HTMLTestRunner
from utils.config import Config, DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
from utils.log import logger


class TestBaidu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baiduTest.xlsx'

    def sub_setUp(self):
        self.page = BaiduMainPage().get(self.URL, maximize_window=False)

    def sub_tearDown(self):
        self.page.quit()

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.search(d['search'])
                time.sleep(2)
                self.page = BaiduResultPage(self.page)  # 页面跳转到result page
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()

if __name__ == '__main__':
    report = REPORT_PATH + '/report.html'
    print("开始生成报告")
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 灰蓝', description='修改html报告')
        runner.run(TestBaidu('test_search'))
        print("生成报告成功")

    # e = Email(title='百度搜索测试报告',
    #           message='这是今天的测试报告',
    #           receiver='...',
    #           server='...',
    #           sender='...',
    #           password='...',
    #           path=report
    #           )
    #
    # e.send()
