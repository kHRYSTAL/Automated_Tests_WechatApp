#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: log.py
# @time: 17/11/21 上午10:48
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from utils.config import LOG_PATH, Config


class Logger(object):
    def __init__(self, logger_name='wechatApp'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        c = Config().get('log')
        self.log_file_name = c.get('file_name') if c and c.get('file_name') else 'test.log'  # 日志文件
        self.backup_count = c.get('backup') if c and c.get('backup') else 5  # 保留的日志数量
        # 日志输出级别
        self.console_output_level = c.get('console_level') if c and c.get('console_level') else 'WARNING'
        self.file_output_level = c.get('file_level') if c and c.get('file_level') else 'DEBUG'
        # 日志输出格式
        pattern = c.get('pattern') if c and c.get('pattern') else '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        self.formatter = logging.Formatter(pattern)

    def get_logger(self):
        """在logger中添加日志句柄并返回 如果logger已经有句柄, 则直接返回"""
        if not self.logger.handlers:  # 避免日志重复
            # region console处理
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)
            # endregion

            # region 文件处理
            # 每天重新创建一个日志文件, 最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH, self.log_file_name),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8')
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
            # endregion

        return self.logger

logger = Logger().get_logger()
