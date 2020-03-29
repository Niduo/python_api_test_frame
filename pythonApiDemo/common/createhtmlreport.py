# -*- conding:utf-8 -*-
import HTMLTestRunner
import csv
import json


class createhtmlreport(object):
    def htmlreport(self, filename, revtitle, revdesc, revsuite):
        filehtml = '../testReport/'+filename
        # wb：以二进制的方式写入图片，w：写入，b：代表图片，以二进制方式
        with open(filehtml, 'w', encoding='utf-8')as htmla:
            # verbosity生成报告条数：1或2
            # 1生成一条报告
            # 2生成详细信息
            HTMLTestRunner.HTMLTestRunner(
                # 文本流向哪里，定义内存空间
                stream=htmla,
                # 测试报告条数
                verbosity=2,
                # 标题，公用模块不能写死
                title=revtitle,
                # 描述，用变量代替
                description=revdesc
            ).run(revsuite)# 执行测试用例