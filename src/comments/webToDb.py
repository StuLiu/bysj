"""
==============================
         单线程爬虫脚本
  从指定网址爬取评论并存入数据库
==============================
"""
print(__doc__)

import re
import time
from comments.mySpider import MySpider
from database.app_comments_dbHandler import AppCommentsDbHandler
from database.apple_app_dbHandler import AppleAppDbHandler

class WebToDb(object):

    def __init__(self):
        self.__headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/57.0'}
        self.__pattern = re.compile('<entry>.*?<updated>(.*?)</updated>.*?<id>(.*?)</id>.*?'
            '<title>(.*?)</title>.*?<content.*?>(.*?)</content>.*?<im:voteSum>(.*?)</im:voteSum>.*?'
            '<im:voteCount>(.*?)</im:voteCount>.*?<im:rating>(.*?)</im:rating>.*?'
            '<im:version>(.*?)</im:version>.*?<name>(.*?)</name>', re.M | re.S)
        self.__appCommentsHandler = AppCommentsDbHandler()
        self.__appleAppHandler = AppleAppDbHandler()

    def executeAll(self):
        counter = 0
        appleApps = self.__appleAppHandler.queryAll()
        for appleApp in appleApps:
            print('\n正在获取苹果应用: %s-%s 的最新评论······' % (appleApp[0],appleApp[1]))
            added = self.executeByAppId(appleApp[0])
            print('新增%d条评论' % added)
            counter += added
        return counter

    def executeByAppId(self,appId):
        count_before = self.__appCommentsHandler.count()
        # get comment entries from page 1 to 10
        for currPage in range(1, 11):
            url = "https://itunes.apple.com/rss/customerreviews/page=" + str(currPage) + \
                  "/id=" + str(appId) + "/sortby=mostrecent/xml?l=en&&cc=cn"
            spider = MySpider(url, self.__headers, self.__pattern)
            comments = spider.getMsgs()
            try:
                # insert comment entries from current website page one by one
                for comment in comments:
                    commentItemList = list(comment)
                    commentItemList.append(appId)       # app_id
                    commentItemList.append(str(''))     # isSpam
                    try:
                        self.__appCommentsHandler.insertAppComment(commentItemList)
                    except UserWarning:
                        raise UserWarning('Outdated comments!')
                    except Exception as errStr:
                        print(errStr)
            except (Exception,UserWarning) as errStr:
                print(errStr,'Update next app\'s comment!')
                break
        count_after = self.__appCommentsHandler.count()
        return count_after - count_before

if __name__ == '__main__':
    try:
        fr = time.time()
        # print("更新%d条评论" % WebToDb().executeByAppId('1010704842'))
        print("本次更新总共新增%d条评论" % WebToDb().executeAll())
        to = time.time()
        print('运行时间:' + str(to - fr) + '秒')
    except Exception as e:
        print(e)
