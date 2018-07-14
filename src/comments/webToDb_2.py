"""
==============================
         多线程爬虫脚本
  从指定网址爬取评论并存入数据库
==============================
"""
print(__doc__)

import re
import time
from comments.mySpider import MySpider
from database.app_comments_dbHandler import AppCommentsDbHandler
from database.apple_app_dbHandler import AppleAppDbHandler


import threading
class ThreadOfWebToDb(threading.Thread):

    def __init__(self, appids):
        threading.Thread.__init__(self)
        self.__appids = appids    # a list
        self.__headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/57.0'}
        self.__pattern = re.compile('<entry>.*?<updated>(.*?)</updated>.*?<id>(.*?)</id>.*?'
            '<title>(.*?)</title>.*?<content.*?>(.*?)</content>.*?<im:voteSum>(.*?)</im:voteSum>.*?'
            '<im:voteCount>(.*?)</im:voteCount>.*?<im:rating>(.*?)</im:rating>.*?'
            '<im:version>(.*?)</im:version>.*?<name>(.*?)</name>', re.M | re.S)
        self.__appCommentsHandler = AppCommentsDbHandler()
        self.__count = 0

    def countOfNewComments(self):
        return self.__count

    def run(self):
        # get comments from websits and save them to database
        for appid in self.__appids:
            count_befor = self.__appCommentsHandler.countByAppId(appid)
            for currPage in range(1, 11):
                url = "https://itunes.apple.com/rss/customerreviews/page=" + str(currPage) + \
                      "/id=" + str(appid) + "/sortby=mostrecent/xml?l=en&&cc=cn"
                spider = MySpider(url, self.__headers, self.__pattern)
                comments = spider.getMsgs()
                try:
                    # insert comment entries from current website page one by one
                    for comment in comments:
                        commentItemList = list(comment)
                        commentItemList.append(appid)       # app_id
                        commentItemList.append(str(''))     # isSpam
                        try:
                            self.__appCommentsHandler.insertAppComment(commentItemList)
                        except UserWarning:
                            raise UserWarning('{} Outdated comments!'.format(appid))
                        except Exception as errStr:
                            print(errStr)
                except (Exception,UserWarning) as errStr:
                    # print(errStr)
                    break
            count_after = self.__appCommentsHandler.countByAppId(appid)
            print('{} get {} comments.Update next app\'s comment!'
                  .format(appid, count_after-count_befor))
            self.__count += count_after-count_befor

class WebToDb_2(object):

    def __init__(self):
        self.__appleAppHandler = AppleAppDbHandler()
        self.__appCommentsHandler = AppCommentsDbHandler()

    def executeAll(self):
        appleApps = self.__appleAppHandler.queryAll()
        sizeOfAppleApps = len(appleApps)
        print("sizeOfAppleApps",sizeOfAppleApps)
        sizeOfAppids = int(sizeOfAppleApps / 10 + 1)
        listOfAppids = []       # [[appid1,appid2,...], ...]
        countTemp = 0
        appidsTemp = []
        for index in range(0,sizeOfAppleApps):
            countTemp += 1
            appidsTemp.append(appleApps[index][0])
            if countTemp >= sizeOfAppids or index >= sizeOfAppleApps-1:
                listOfAppids.append(appidsTemp)
                appidsTemp = []
                countTemp = 0
        # for li in listOfAppids:
        #     for appid in li:
        #         print(appid,',')
        #     print('\n')
        listOfThreads = []
        for appids in listOfAppids:
            myThread = ThreadOfWebToDb(appids)
            listOfThreads.append(myThread)
        print("number of threads:{}".format(len(listOfThreads)))
        for thread in listOfThreads:
            thread.start()

        countOfNewComments = 0
        for thread in listOfThreads:
            thread.join()
            countOfNewComments += thread.countOfNewComments()
        return countOfNewComments


if __name__ == '__main__':
    try:
        fr = time.time()
        print("本次更新总共新增{}条评论".format(WebToDb_2().executeAll()))
        to = time.time()
        print('运行时间:{}秒'.format(to-fr))
    except Exception as e:
        print(e)
