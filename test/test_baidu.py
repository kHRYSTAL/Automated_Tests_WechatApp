#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 使用selenium 模拟请求百度
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: test_baidu.py
# @time: 17/11/20 下午7:12


import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
URL = "http://www.baidu.com"
base_path = os.path.dirname(os.path.abspath(__file__)) + '\..'
# driver_path = os.path.abspath(base_path + '\drivers\chromedriver.exe')

locator_kw = (By.ID, 'kw')
locator_su = (By.ID, 'su')
# xpath匹配 <div class="result"><h3><a>中的内容
locator_result = (By.XPATH, "//div[contains(@class, 'result')]/h3/a")


driver = webdriver.Chrome()
driver.get(URL)
driver.find_element(*locator_kw).send_keys("selenium 灰蓝")
driver.find_element(*locator_su).click()

time.sleep(2)
links = driver.find_elements(*locator_result)
print(links)
for link in links:
    print(link.text)

driver.quit()

# def setUp(self):
#     self.driver = webdriver.Chrome(executable_path=self.driver_path)
#     self.driver.get(self.URL)
