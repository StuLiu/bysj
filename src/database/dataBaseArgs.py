
import xml.dom.minidom as xmlDom

import config


class DataBaseArgs(object):
    __DOMTree = xmlDom.parse(config.MYSQLARGS_PATH)
    __mysql = __DOMTree.documentElement.getElementsByTagName("mysql")[0]
    __url = __mysql.getElementsByTagName('url')[0].childNodes[0].data
    __userName = __mysql.getElementsByTagName('userName')[0].childNodes[0].data
    __password = __mysql.getElementsByTagName('password')[0].childNodes[0].data
    __database = __mysql.getElementsByTagName('database')[0].childNodes[0].data

    @classmethod
    def getUserName(cls):
        return cls.__userName

    @classmethod
    def getPassWord(cls):
        return cls.__password

    @classmethod
    def getDataBase(cls):
        return cls.__database

    @classmethod
    def getUrl(cls):
        return cls.__url

if __name__ == '__main__':
    print(DataBaseArgs.getUserName())
    print(DataBaseArgs.getPassWord())
    print(DataBaseArgs.getDataBase())
    print(DataBaseArgs.getUrl())