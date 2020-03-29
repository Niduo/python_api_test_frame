# coding=utf-8
from testModule.module import Module


class TestDemo2:
    @classmethod
    def setup_class(cls):
        cls.m = Module()
        cls.successCode = 200
        cls.msg_code = '错误, response code is not 200'
        cls.msg_data = '错误, data不一致'
        print('test 第二个类 start!')

    @classmethod
    def teardown_class(cls):
        print('test class end!')

    def setup(self):
        print('test method start!')

    def teardown(self):
        print('test method end!')

    def test_2001(self):
        # 断言json data字段
        status_code, actual_data, expect_data = self.m.run_back_json(1)
        print('code type:', type(status_code), 'self.successCode type:', type(self.successCode), '\n', 'actual_data type: ', type(actual_data), 'expect_data type:', type(expect_data))
        print('actual_data:', actual_data, '\n', 'expect_data:', '\n', expect_data)
        assert status_code == self.successCode, self.msg_code
        assert actual_data['data'] == expect_data['data'], self.msg_data

    def test_2002(self):
        # text包含比较
        status_code, actual_data, expect_data = self.m.run_back_text(2)
        assert status_code == self.successCode, self.msg_code
        assert expect_data in actual_data, self.msg_data

    def test_2003(self):
        # text包含比较
        status_code, actual_data, expect_data = self.m.run_back_text(3)
        assert status_code == self.successCode, self.msg_code
        assert expect_data in actual_data, self.msg_data

    def test_2004(self):
        status_code, actual_data, expect_data = self.m.run_back_text(4)
        assert status_code == self.successCode, self.msg_code
        assert actual_data == expect_data, self.msg_data

    def test_2005(self):
        print("test003 start!")
        c = 1+2
        assert c == 3







