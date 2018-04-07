####
#单线程爬虫
####

import re
import time
from mySpider import MySpider
from commentDbHandler import CommentDbHandler
from dataBaseArgs import DataBaseArgs
from myLogFile import MyLogFile

class WebToDb(object):

    def __init__(self, headers, pattern):
        self.headers = headers
        self.pattern = pattern

    # version 1.0 getting comments from websites
    def execute(self):
        # count the number of comments inserted successfully
        counter = 0
        # get comment db handler
        dbHandler = CommentDbHandler('127.0.0.1', DataBaseArgs.getUserName(),
                                     DataBaseArgs.getPassWord(), DataBaseArgs.getDataBase())
        # get app tuples
        apps = dbHandler.getApps()
        # update comments of each app select from table appleApp
        for app in apps:
            print('\n' + 'Update comment of appleApp-{},id-{} now.'.format(app[1], app[0]))
            # get comment entries from page 1 to 10
            for currPage in range(1, 11):
                url = "https://itunes.apple.com/rss/customerreviews/page=" + str(currPage) + \
                      "/id=" + str(app[0]) + "/sortby=mostrecent/xml?l=en&&cc=cn"
                spider = MySpider(url, self.headers, self.pattern)
                comments = spider.getMsgs()
                try:
                    # insert comment entries from current website page one by one
                    for comment in comments:
                        commentItemList = list(comment)
                        commentItemList.append(app[0])
                        commentItemList.append(str(''))
                        try:
                            dbHandler.insertComment(commentItemList)
                        except UserWarning:
                            raise UserWarning('Outdated comments!')
                        except Exception as errStr:
                            print(errStr)
                            continue
                        else:
                            # print("Add a comment  successfully!")
                            counter += 1
                except (Exception,UserWarning) as errStr:
                    print(errStr,'Update next app\'s comment!')
                    break
        logTexts.append('update database finished.(single thread)')
        logTexts.append('Update ' + str(counter) + ' comments totally!')

    def executeByAppId(self,appId):
        # count the number of comments inserted successfully
        counter = 0
        # get comment db handler
        dbHandler = CommentDbHandler('127.0.0.1', DataBaseArgs.getUserName(),
                                     DataBaseArgs.getPassWord(), DataBaseArgs.getDataBase())

        print('\n' + 'Update comment of appid-{} now.'.format(appId))
        # get comment entries from page 1 to 10
        for currPage in range(1, 11):
            url = "https://itunes.apple.com/rss/customerreviews/page=" + str(currPage) + \
                  "/id=" + str(appId) + "/sortby=mostrecent/xml?l=en&&cc=cn"
            spider = MySpider(url, self.headers, self.pattern)
            comments = spider.getMsgs()
            try:
                # insert comment entries from current website page one by one
                for comment in comments:
                    commentItemList = list(comment)
                    commentItemList.append(appId)
                    commentItemList.append(str(''))
                    try:
                        dbHandler.insertComment(commentItemList)
                    except UserWarning:
                        raise UserWarning('Outdated comments!')
                    except Exception as errStr:
                        print(errStr,'ss')
                        continue
                    else:
                        print("Add a comment  successfully!")
                        counter += 1
            except (Exception,UserWarning) as errStr:
                print(errStr,'Update next app\'s comment!')
                break
        logTexts.append('update database by appid-%s finished.(single thread)'%(appId))
        logTexts.append('Update ' + str(counter) + ' comments totally!')


if __name__ == '__main__':
    # define request headers
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/57.0'}
    # compile regular expression to grab comment entries
    pattern = re.compile('<entry>.*?<updated>(.*?)</updated>.*?<id>(.*?)</id>.*?<title>(.*?)</title>.*?'
                         '<content.*?>(.*?)</content>.*?<im:voteSum>(.*?)</im:voteSum>.*?'
                         '<im:voteCount>(.*?)</im:voteCount>.*?<im:rating>(.*?)</im:rating>.*?'
                         '<im:version>(.*?)</im:version>.*?<name>(.*?)</name>', re.M | re.S)
    logTexts = []
    try:
        fr = time.time()
        WebToDb(headers, pattern).execute()
        # WebToDb(headers, pattern).executeByAppId('1338720864')
        to = time.time()
        logTexts.append('runtime:' + str(to - fr) + 's')
        for logText in logTexts:
            print(logText)
        MyLogFile('Log').addMsg(logTexts)
    except Exception as e:
        print(e)
    finally:
        print('******Finish******\n')
