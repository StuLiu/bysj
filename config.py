
import os

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))      # 源文件目录

RESOURCES_PATH = os.path.join(PROJECT_ROOT ,"resources")        #资源目录路径

DICT_PATH = os.path.join(RESOURCES_PATH ,"dict")

MYSQLARGS_PATH = os.path.join(PROJECT_ROOT ,"resources","mysqlArgs.xml")

if __name__ == '__main__':
    print(PROJECT_ROOT)
    print(RESOURCES_PATH)
    print(DICT_PATH)