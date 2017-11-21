#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: run_all_case.py
# @time: 17/11/21 下午3:51
from utils import config
import unittest
import os

# 测试用例路径
from utils.HTMLTestRunner import HTMLTestRunner
from utils.config import REPORT_PATH

case_path = os.path.join(config.BASE_PATH, 'test')
print(case_path)

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern='test*.py',
                                                   top_level_dir=None)
    return discover


if __name__ == '__main__':
    report = REPORT_PATH + '/report.html'
    print("开始生成报告")
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 灰蓝', description='修改html报告')
        runner.run(all_case())
        print("生成报告成功")
