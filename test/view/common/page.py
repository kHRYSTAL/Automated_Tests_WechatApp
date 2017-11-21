#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: page.py
# @time: 17/11/21 下午2:24

from test.view.common.browser import Browser

class Page(Browser):
    def __init__(self, page=None):
        if page:
            self.driver = page.driver
        else:
            super(Page, self).__init__()

    def get_driver(self):
        return self.driver

    def find_element(self, *args):
        return self.driver.find_element(*args)

    def find_elements(self, *args):
        return self.driver.find_elements(*args)

if __name__ == '__main__':
    pass