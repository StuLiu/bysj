
import os

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))      # 顶层目录bysj/

RESOURCES_PATH = os.path.join(PROJECT_ROOT ,"resources")        # 资源目录

DICT_PATH = os.path.join(RESOURCES_PATH ,"dict")

MYSQLARGS_PATH = os.path.join(PROJECT_ROOT ,"resources","mysqlArgs.xml")

if __name__ == '__main__':
    print(PROJECT_ROOT)
    print(RESOURCES_PATH)
    print(DICT_PATH)