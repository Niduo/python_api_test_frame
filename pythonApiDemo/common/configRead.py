import os
import configparser

# 获取当前绝对路径
# proDir = os.path.split(os.path.realpath(__file__))[0]
# curDir = os.path.abspath('..') 当前目录
# 父目录
# proDir = os.path.abspath('..')
# configPath = os.path.join(proDir, "config\config.txt",)


class ConfigRead:
    def __init__(self):
        # print(proDir, configPath)
        # fd = open(configPath, 'r', encoding='utf-8')
        # data = fd.read()
        # 判断utf-8文件前三个字节是否为BOM_UTF8。如果是，则剔除\xef\xbb\xbf字节remove BOM
        # if data[:3] == codecs.BOM_UTF8:
        #     print(data[:3])
        #     data = data[3:]
        #     file = codecs.open(configPath, "w")
        #     file.write(data)
        #     file.close()
        # fd.close()
        # self.cf = configparser.ConfigParser()
        # self.cf.read(configPath)
        # proDir = os.path.split(os.path.realpath(__file__))[0]
        # father = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
        current_path = __file__
        self.proDir = os.path.abspath(os.path.join(current_path, os.pardir, os.pardir))
        # proDir = os.path.dirname(os.path.realpath()) #与上面一行代码作用一样
        self.configPath = os.path.join(self.proDir, "config\\config.txt")
        self.testFilePath = os.path.join(self.proDir, "testFiles\\testData.csv")
        self.cf = configparser.ConfigParser()
        self.cf.read(self.configPath)

    # 获取demo网站httpbin的地址
    def get_demoHost(self):
        value = self.cf.get("HTTP", "demourl")
        return value

    # 获取demo网站httpbin的地址
    def get_testHost(self):
        value = self.cf.get("HTTP", "testhost")
        return value

    # 获取email的值
    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    # 获取http的值
    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    # 获取超时
    def get_timeout(self, timeout):
        value = self.cf.get('HTTP', 'timeout')
        return value

    # 获取db的值
    def get_db(self, itemName):
        value = self.cf.get("DATABASE", itemName)
        return value

    # 获取配置文件所有的section
    def get_section(self):
        value = self.cf.sections()
        return value

    # 获取指定section下所有option
    def get_option(self, option):
        value = self.cf.options(option)
        return value

    # 获取指定section下所有的键值对
    def get_key_value(self, item):
        value = self.cf.sections(item)
        return value

    # 获取testfile路径
    # def get_testFile_path(self):
    #     value = proDir+self.cf.get("TESTFILE", "path")
    #     print(value, type(value))
    #     return value

    # 拼接请求全地址
    def get_full_path(self, path):
        value = self.get_demoHost()+path
        return value


if __name__ == '__main__':
    C = ConfigRead()
#     # print(configPath, '\n')
    C.get_testFile_path()
#     print(C.get_demoHost())