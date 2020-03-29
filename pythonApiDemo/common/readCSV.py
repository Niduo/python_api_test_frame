# -*- coding : utf-8 -*-
# coding:unicode_escape
from common.configRead import ConfigRead
import pandas as pd

"""
读csv
id||module||subPath||method||title||params||expect_result
case号需大于0
"""


class ReadCSV:
    def __init__(self):
        self.csvData = pd.read_csv(ConfigRead().testFilePath, encoding='gbk')

    def show_fields(self):
        """
        获取字段
        :return: 返回第一行的字段
        """
        print(self.csvData.head(0))
        return self.csvData.head(0)

    def get_module(self, case_number):
        """
        根据传入的case号获取module值

        :param case_number: case号int类型
        :return: 返回case对应的module值
        """
        value = self.get_value_by_row_column(case_number, 2)
        return value

    def get_sub_path(self, case_number):
        """
        根据传入的case号获取subPath值

        :param case_number: case号int类型
        :return: 返回case对应的module值
        """
        value = self.get_value_by_row_column(case_number, 3)
        return value

    def get_method(self, case_number):
        """
        根据传入的case号获取method值

        :param case_number: case号int类型
        :return: 返回case对应的module值
        """
        value = self.get_value_by_row_column(case_number, 4)
        return value

    def get_title(self, case_number):
        """
        根据传入的case号获取title值

        :param case_number: case号int类型
        :return: 返回case对应的module值
        """
        value = self.get_value_by_row_column(case_number, 5)
        return value

    def get_params(self, case_number):
        """
        根据传入的case号获取params值

        :param case_number: case号int类型
        :return: 返回case对应的module值
        """
        value = self.get_value_by_row_column(case_number, 6)
        return value

    def get_expect_result(self, case_number):
        """
        根据传入的case号获取params值

        :param case_number: case号int类型
        :return: 返回case对应的module值
        """
        value = self.get_value_by_row_column(case_number, 7)
        return value


    def get_value_by_field_name(self, columnName:str, case_number:int):
        """
        根据列的字段名和行号获取字段值
        :param columnName: 字段名
        :param case_number: case行号
        :return: 返回字段值
        """

        if case_number < 1:
            print("输入case行号不能小于1")
            return -1
        else:
            num = case_number-1
            value = self.csvData[columnName][num]
            return value

    def get_full_demo_host(self, case_number:int):
        """
        根据传入的subpath拼接成全地址
        :param case_number: case号
        :return:
        """
        # 获取所有列字段
        # columnList = list(self.csvData.columns.values)
        if case_number < 1:
            print("输入case行号不能小于1")
        else:
            value = ConfigRead().get_full_path(self.get_sub_path(case_number))
            # print(value)
            return value

    def get_value_by_row_column(self, case_number:int, column:int):
        """
        根据行号和列号获取指定值
        :param case_number: 行号
        :param column: 列号
        :return: 指定的值
        """
        if case_number < 1:
            print("输入case行号不能小于1")
            return -1
        elif column < 1:
            print("输入列号不能小于1")
            return -1
        else:
            orderRow = case_number-1
            orderColumn = column-1
            value = self.csvData.iloc[orderRow][orderColumn]
            # print(value)
            return value


if __name__ == '__main__':
    d = ReadCSV()
    c = d.get_value_by_row_column(1, 3)
    print(c)
    # e = d.get_sub_path(1)
    # f = d.get_module(1)
    # c.get_value_by_row_column(1,1)
    # d.csvData.loc[[1], [1]]
    # print(d.csvData.iloc[2][3])
