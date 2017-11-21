#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: file_reader.py
# @time: 17/11/21 上午10:23
import yaml
import os
from xlrd import open_workbook


class YamlReader:
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError("配置文件不存在!")
        self._data = None

    @property
    def data(self):
        """将函数变为属性 @property为get函数"""
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))  # load后是个generator，用list组织成列表
        return self._data


class SheetTypeError(Exception):
    pass


class ExcelReader:
    """
    读取excel文件中的内容。返回list。

    如：
    excel中内容为：
    | A  | B  | C  |
    | A1 | B1 | C1 |
    | A2 | B2 | C2 |

    如果 print(ExcelReader(excel, title_line=True).data)，输出结果：
    [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]

    如果 print(ExcelReader(excel, title_line=False).data)，输出结果：
    [[A,B,C], [A1,B1,C1], [A2,B2,C2]]

    可以指定sheet，通过index或者name：
    ExcelReader(excel, sheet=2)
    ExcelReader(excel, sheet='BaiDuTest')
    """

    def __init__(self, excel, sheet=0, title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError("Excel文件不存在")
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()  # 指定data 为空列表 []

    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excel)
            if type(self.sheet) not in [int, str]:
                raise SheetTypeError("Please pass in <type int> or <type str>, not {0}".format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            if self.title_line:
                # 如果title_line为True 则组成excel对象为字典 首行为列名 Key
                title = s.row_values(0) # 首行为title
                for row in range(1, s.nrows):
                    # 遍历其余行 与首行组成dict
                    """
                    zip结果为
                    [(title, row1), (title, row2), (title, row3)...]
                    dict化
                    [{title: row1}, {title: row2}, {title, row3}]
                    """
                    self._data.append(dict(zip(title, s.row_values(row))))

            else:
                for row in range(0, s.nrows):
                    # 遍历所有行 拼接组成数组
                    self._data.append(s.row_values(row))

        return self._data

if __name__ == "__main__":
    from utils.config import BASE_PATH
    y = os.path.join(BASE_PATH, 'config', 'config.yml')
    reader = YamlReader(y)
    # print(reader.data)

    e = os.path.join(BASE_PATH, 'data', 'baiduTest.xlsx')
    reader = ExcelReader(e, title_line=True)
    print(reader.data)

