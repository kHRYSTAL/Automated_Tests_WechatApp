#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 添加用于接口测试的client，对于HTTP接口添加HTTPClient，发送http请求。还可以封装TCPClient，用来进行tcp链接，测试socket接口等等。
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: client.py
# @time: 17/11/21 下午3:00


import requests
from utils.log import logger

METHODS = ['GET', 'POST', 'HEAD', 'TRACE', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']


class UnSupportMethodException(Exception):
    """当传入method的参数不是支持的类型时抛出异常"""
    pass


class HttpClient(object):
    """
    http请求的client 初始化时传入url method 等可以添加headers和cookies 但没有auth, proxy
    >>> HttpClient('http://www.baidu.com').send()
    <Response [200]>
    """

    def __init__(self, url, method="GET", headers=None, cookies=None):
        """headers: dict e.g. headers={'Content-Type:'text/html'}, cookies 也是字典"""
        self.url = url
        self.session = requests.session()
        self.method = method.upper()
        if self.method not in METHODS:
            raise UnSupportMethodException('不支持的method:{0}，请检查传入参数！'.format(self.method))

        self.set_headers(headers)
        self.set_cookies(cookies)

    def set_headers(self, headers):
        if headers:
            self.session.headers.update(headers)

    def set_cookies(self, cookies):
        if cookies:
            self.session.cookies.update(cookies)

    def send(self, params=None, data=None, **kwargs):
        response = self.session.request(method=self.method, url=self.url,
                                        params=params, data=data, **kwargs)

        response.encoding = 'utf-8'
        logger.debug('{0}{1}'.format(self.method, self.url))
        logger.debug('请求成功: {0}\n{1}'.format(response, response.text))
        return response
