#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 生成测试报告
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: test_baidu_6st.py
# @time: 17/11/21 下午12:29

import time
import unittest
from utils.log import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config, DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
from utils.HTMLTestRunner import HTMLTestRunner


class TestBaidu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baiduTest.xlsx'
    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def sub_setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)

    def sub_tearDown(self):
        self.driver.quit()

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            """
            subTest是PY3 unittest里带的功能，PY2中没有，PY2中要想使用，需要用unittest2库。subTest是没有setUp和tearDown的，所以需要自己手动添加并执行。
            """
            with self.subTest(data=d):
                self.sub_setUp()
                self.driver.find_element(*self.locator_kw).send_keys(d['search'])
                self.driver.find_element(*self.locator_su).click()
                time.sleep(2)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()


if __name__ == '__main__':
    report = REPORT_PATH + '/report.html'
    print(report)
    print("开始执行测试并生成报告")
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 灰蓝', description='修改html报告')
        runner.run(TestBaidu('test_search'))
        print("输出report.html成功")
