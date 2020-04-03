# coding=utf-8
"""
by 老屋
des 使用 allure执行用例，但插件无法下载暂不用

"""

from common.runRequest import RunRequest
import pytest
import allure


@allure.feature('Demo测试模块')
class AllureReportDemo:
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

    @allure.story('post的演示成功的测试')
    def test_001(self):
        print("test001 start!")
        status_code, actual_data, expect_data = self.m.run_request(1)
        assert status_code == self.successCode, self.msg_code
        assert actual_data == expect_data, self.msg_data

    @allure.story('get的演示成功的测试')
    def test_002(self):
        print("test002 start")
        status_code, actual_data, expect_data = self.m.run_request(2)
        assert status_code == self.successCode, self.msg_code
        assert actual_data == expect_data, self.msg_data

    def test_003(self):
        print("test003 start!")
        with allure.step("1+2赋值"):
            c = 1+2
        with allure.step('断言'):
            assert c == 4

    def test_004(self):
        status_code, actual_data, expect_data = self.m.run_request(4)
        assert status_code == self.successCode, self.msg_code
        assert actual_data == expect_data, self.msg_code

    def test_005(self):
        status_code, actual_data, expect_data = self.m.run_request(5)
        assert status_code == self.successCode, self.msg_code
        assert actual_data == expect_data, self.msg_code


if __name__ == '__main__':
    # pytest.main("-v ./testDemo2.py")
    pytest.main(['-v', './testDemo.py'])

