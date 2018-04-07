
import time
class MyLogFile(object):
    def __init__(self,fileName):
        try:
            self.fileObj = open(fileName+'.txt', 'a+')
        except Exception as errStr:
            print('Can\'t open {}txt,',errStr)

    def __del__(self):
        self.fileObj.close()

    def addMsg(self,strs):
        tempstr = '--------'
        self.fileObj.write('\n\n' + tempstr + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n')
        for s in strs:
            self.fileObj.write(tempstr + s + '\n')


if __name__ == '__main__':
    a = MyLogFile('logTest')
    a.addMsg('p************\n  aasd\n***************\n')
    a = MyLogFile('logTest')
    a.addMsg('p************\n  aasd\n***************\n')