# coding=utf-8
from common.requestMethod import RequestMethod
from common.readCSV import ReadCSV as rc
import json
# import ast


class RunRequest:
    @staticmethod
    def run_back_json(case_number):
        """
        自动判断post or get去做请求转化为json数据返回
        :param case_number:  case号
        :return: code_status， actual， expect结果
        """

        if case_number > 0:
            full_path = rc().get_full_demo_host(case_number)
            method = rc().get_method(case_number)
            param = rc().get_params(case_number)
            expect = rc().get_expect_result(case_number)
            j_expect = json.loads(expect)
            # 判断不为空时去请求
            if full_path and method:
                res = RequestMethod().main_json_to_str(method=method, url=full_path, data=param)
                # print(res, type(res))
                j_status = res.status_code
                j_actual = res.json()
                # print("j_status tpye:", type(j_status), 'j_status:\n', j_status)
                # print('j_actual tpye: \n', type(j_actual), 'j_actual', j_actual, '\n')
                # print('expectType: ', type(j_expect), '\n', 'j_expect:\n ', j_expect)
                return j_status, j_actual, j_expect
            else:
                print("路径和方法读取报错: full_path: %s, method: %s" % (full_path, method))
                return -1
        else:
            print("case number不能小于0")
            return -1

    @staticmethod
    def run_back_text(case_number):
        """
        请求转化text的数据返回
        :param case_number:
        :return:
        """
        full_path = rc().get_full_demo_host(case_number)
        param = rc().get_params(case_number)
        method = rc().get_method(case_number)
        t_expect = rc().get_expect_result(case_number)
        if case_number > 0:
            if full_path and method:
                res = RequestMethod().main_json_to_str(method, full_path, param)
                print("res:\n", res, "\n", type(res))
                t_status_code = res.status_code
                # 转字符串做比较
                t_actual = res.text
                print('code:\n', t_status_code, "actualTyep \n", type(t_actual), "\n","actual: \n", t_actual, 'expType:', type(t_expect), 'expect:\n ', t_expect)
                return t_status_code, t_actual, t_expect
            else:
                print("路径和方法读取报错: full_path: %s, method: %s" % (full_path, method))
                return -1
        else:
            print("case number不能小于0")

