import pytest
from common.sendEmail import SendEmail

test_report = 'report.html'

# 执行test_Demo_module1 case
test001_002 = 'demo_module_case1_2'
demo_module_case1_2 = ['-v', './testCase/testDemo.py::TestDemo::test001::tests002', './testCase/testDemo.py::TestDemo::test002', '--html=./report'+'%s' % test001_002]

# 执行test_Demo
test_demo = 'testDemo.html'
testDemo = ['-v', './testCase/testDemo.py', '--html=./report/'+'%s' % test_demo]

# 执行test_Demo2
test_demo2 = 'testDemo2.html'
testDemo2 = ['-v', './testCase/testDemo2.py', '--html=./report/'+'%s' % test_demo2]

# 执行testDemo&testDemo2
test_demo_demo2 = 'test_Demo1_2.html'
testDemo1_2 = ['-v', './testCase/testDemo.py', './testCase/testDemo2.py', '--html=./report/'+'%s' % test_demo_demo2]

# 执行所有case
cases = 'all_case'
all_case = ['-v', './testCase', '--html=./report/'+'%s' % cases]

if __name__ == '__main__':
    # pytest.main(demo_module_case1_2)
    pytest.main(testDemo)
    # pytest.main(testDemo2)
    # pytest.main(testDemo1_2)
    # send mail

    sm = SendEmail()
    mail_subject = 'interface demo test'
    mail_content = 'Plz check'
    mail_att = './report/'+test_demo
    sm.send(mail_subject, mail_content, mail_att)






