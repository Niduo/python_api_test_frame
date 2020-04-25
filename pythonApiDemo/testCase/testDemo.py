# coding=utf-8
"""
by: 老屋
des：测试httpbin接口用例
"""

from common.runRequest import RunRequest
import pytest


class TestDemo:
    @ classmethod
    def setup_class(cls):
        cls.m = RunRequest()
        cls.successCode = 200
        cls.msg_code = '错误, response code is not 200'
        cls.msg_data = '错误, data不一致'
        print('test class start!')

    @classmethod
    def teardown_class(cls):
        print('test class end!')

    def setup(self):
        print('test method start!')

    def teardown(self):
        print('test method end!')

    def test_001(self):
        # 断言json data字段
        print("test001 start!")
        status_code, actual_data, expect_data = self.m.run_back_json(1)
        print('code type:', type(status_code), 'self.successCode type:', type(self.successCode), '\n', 'actual_data type: ', type(actual_data), 'expect_data type:', type(expect_data))
        print('actual_data:', actual_data, '\n', 'expect_data:', '\n', expect_data)
        assert status_code == self.successCode, self.msg_code
        assert actual_data['data'] == expect_data['data'], self.msg_data

    def test_002(self):
        # text包含比较
        status_code, actual_data, expect_data = self.m.run_back_text(2)
        assert status_code == self.successCode, self.msg_code
        assert expect_data in actual_data, self.msg_data

    def test_003(self):
        # text包含比较
        status_code, actual_data, expect_data = self.m.run_back_text(3)
        assert status_code == self.successCode, self.msg_code
        assert expect_data in actual_data, self.msg_data

    def test_004(self):
        status_code, actual_data, expect_data = self.m.run_back_text(4)
        assert status_code == self.successCode, self.msg_code
        assert actual_data == expect_data, self.msg_data

    def test_005(self):
        print("test003 start!")
        c = 1+2
        assert c == 3


if __name__ == '__main__':
    # pytest.main(['-x', './testDemo.py'])
    pytest.main(['-vv', './testDemo.py::TestDemo::test_002'])
    # pytest.main(['-v', './testDemo.py::TestDemo::test_001', './testDemo.py::TestDemo::test_002'])

