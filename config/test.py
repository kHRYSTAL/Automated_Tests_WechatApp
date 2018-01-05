#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: test.py
# @time: 18/1/5 下午6:46

import random

a = [str(x) for x in range(10)]
b = [chr(x) for x in range(65, 91)]
c = [chr(x) for x in range(97, 123)]


def gen_random_password():
    num_len = random.randint(1, 6)
    print(num_len)
    low_case_len = random.randint(1, 7 - num_len)
    up_case_len = 8 - num_len - low_case_len
    l = random.sample(a, num_len) + random.sample(b, low_case_len) + random.sample(c, up_case_len)
    random.shuffle(l)
    return ''.join(l)


print(gen_random_password())
