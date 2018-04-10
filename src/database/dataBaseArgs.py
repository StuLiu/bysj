
import xml.dom.minidom as xmlDom

import config


class DataBaseArgs(object):
    DOMTree = xmlDom.parse(config.MYSQLARGS_PATH)
    mysql = DOMTree.documentElement.getElementsByTagName("mysql")[0]
    url = mysql.getElementsByTagName('url')[0].childNodes[0].data
    userName = mysql.getElementsByTagName('userName')[0].childNodes[0].data
    password = mysql.getElementsByTagName('password')[0].childNodes[0].data
    database = mysql.getElementsByTagName('database')[0].childNodes[0].data

    @classmethod
    def getUserName(cls):
        return cls.userName

    @classmethod
    def getPassWord(cls):
        return cls.password

    @classmethod
    def getDataBase(cls):
        return cls.database

    @classmethod
    def getUrl(cls):
        return cls.url

if __name__ == '__main__':
    print(DataBaseArgs.getUserName())