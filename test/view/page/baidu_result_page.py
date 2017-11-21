#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: baidu_result_page.py
# @time: 17/11/21 下午2:32

from selenium.webdriver.common.by import By

from test.view.page.baidu_main_page import BaiduMainPage


class BaiduResultPage(BaiduMainPage):
    loc_result_links = (By.XPATH, '//div[contains(@class, result)]/h3/a')

    @property
    def result_links(self):
        return self.find_elements(*self.loc_result_links)

if __name__ == '__main__':
    pass