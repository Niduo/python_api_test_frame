from common.sendEmail import SendEmail
import pytest
import datetime


report_path = './report/'
test_demo = 'testDemo.html'
test001_002 = 'testDemo1_2.html'
test_demo2 = 'test_Demo1_2.html'
cases = 'all_case.html'
now_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

# 执行test_Demo_module1 case
demo_module_case1_2 = ['-v', './testCase/testDemo.py::TestDemo::test001::tests002', './testCase/testDemo.py::TestDemo::test002', '--html=./report'+'%s' % test001_002]

# 执行test_Demo
testDemo = ['-v', './testCase/testDemo.py', '--html=%s' % report_path+'%s%s' % (now_time, test_demo)]

# 执行test_Demo2
testDemo2 = ['-v', './testCase/testDemo2.py', '--html=%s' % report_path+'%s%s' % (now_time, test_demo2)]

# 执行testDemo&testDemo2
testDemo1_2 = ['-v', './testCase/testDemo.py', './testCase/testDemo2.py', '--html=%s' % report_path+'%s%s' % (now_time, test001_002)]

# 执行所有case
all_case = ['-v', './testCase', '--html=./report/'+'%s' % cases]


if __name__ == '__main__':
    pytest.main(testDemo1_2)

    # send mail
    sm = SendEmail()
    mail_subject = 'interface demo test'
    mail_content = 'Plz check'
    mail_att = './report/'+test_demo
    # sm.send(mail_subject, mail_content, mail_att)






