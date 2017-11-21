#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 邮件类。用来给指定用户发送邮件。可指定多个收件人，可带附件。
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: mail.py
# @time: 17/11/21 下午1:00

import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror, error
from utils.log import logger


class Email:
    def __init__(self, server, sender, password, receiver, title, message=None, path=None):
        """
        :param server: smtp服务器
        :param sender: 发件人
        :param password: 发件人密码
        :param receiver: 收件人 多人用;隔开
        :param title: 邮件标题
        :param message: 邮件正文
        :param path: 福建路径 可传入list(多附件) 或 str(单个附件)
        """
        self.title = title
        self.message = message
        self.files = path
        self.msg = MIMEMultipart("related")
        self.server = server
        self.sender = sender
        self.receiver = receiver
        self.password = password

    def _attach_file(self, att_file):
        """ 将单个文件添加到附件列表中 """
        att = MIMEText(open('%s' % att_file, 'rb').read(), 'plain', 'utf-8')
        att['Content-Type'] = "application/octet-stream"
        file_name = re.split(r'[\\|/]]', att_file)
        att['Content-Disposition'] = 'attachment; filename="%s"' % file_name[-1]
        self.msg.attach(att)
        logger.info('attach file {}'.format(att_file))

    def send(self):
        self.msg['Subject'] = self.title
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver

        # 邮件正文
        if self.message:
            self.msg.attach(MIMEText(self.message))

        # 添加附件 支持多个附件 或者 单个附件
        if self.files:
            if isinstance(self.files, list):
                for f in self.files:
                    self._attach_file(f)
            elif isinstance(self.files, str):
                self._attach_file(self.files)

        # 连接服务器并发送
        try:
            smtp_server = smtplib.SMTP(self.server)  # 连接server
        except (gaierror and error) as e:
            logger.exception('发送邮件失败, 无法连接到SMTP服务器,检查网络以及SMTP服务器. %s', e)
        else:
            # 没有异常时执行
            try:
                smtp_server.login(self.sender, self.password)  # 登录服务器
            except smtplib.SMTPAuthenticationError as e:
                logger.exception("用户名密码验证失败! %s", e)
            else:
                smtp_server.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string())

            finally:
                smtp_server.quit()  # 断开连接
                logger.info('发送邮件"{0}"成功! 收件人：{1}。如果没有收到邮件，请检查垃圾箱，'
                            '同时检查收件人地址是否正确'.format(self.title, self.receiver))


if __name__ == '__main__':
    pass
