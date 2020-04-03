# python_test_api_frame
接口测试demo

###################################################

框架结构说明：
数据驱动模式，将程序和数据分离，便于代码的维护，用例维护采用cvs文件维护，入参和期望结果也在此文件内维护
python+pytest+requests+csv

package dir：
common 为工具包为其他py提供便捷的封装方法
config 全局配置常用的系统级参数
report 存放测试报告
testcase 测试用例
testdata 局部数据存放
testfile 每一条用例用cvs维护， 请求时读取该文件，便于维护case

###################################################
