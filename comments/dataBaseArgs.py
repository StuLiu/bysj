
import xml.dom.minidom as xmlDom
class DataBaseArgs(object):
    DOMTree = xmlDom.parse("mysqlArgs.xml")
    mysql = DOMTree.documentElement.getElementsByTagName("mysql")[0]
    userName = mysql.getElementsByTagName('userName')[0].childNodes[0].data
    password = mysql.getElementsByTagName('password')[0].childNodes[0].data
    database = mysql.getElementsByTagName('database')[0].childNodes[0].data

    @classmethod
    def getUserName(self):
        return self.userName

    @classmethod
    def getPassWord(self):
        return self.password

    @classmethod
    def getDataBase(self):
        return self.database

if __name__ == '__main__':
    print(DataBaseArgs.getUserName())