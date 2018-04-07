
import pymysql

class CommentDbHandler(object):
    "connect to mysql db and operate it"
    # connect to database named dbName，init db and cursor
    def __init__(self,url,userName,pwd,dbName):
        try:
            self.db = pymysql.connect(url,userName,pwd,dbName,charset='utf8mb4')
        except:
            print('Connect comments database failed!');exit(1)
        else:
            print('Connect comments database successfully')
        self.cursor = self.db.cursor()

    def __del__(self):
        self.closeConnect()

    # insert a comment entry into table named appComments
    # if the comment exist,raise a UserWaring
    # if insert failed for other reason,raise a Exception
    def insertComment(self,comment):
        # time,comment_id,title,content,voteSum,voteCount,rating,version,user_name,app_id,isSpam
        sql = "Insert INTO APPCOMMENTS VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # sql statement arguments
        param = (comment[0], comment[1], comment[2],
                 comment[3], comment[4], comment[5],
                 comment[6], comment[7], comment[8],
                 comment[9], comment[10])
        # print(param)
        try:
            self.cursor.execute(sql,param)
            self.db.commit()
        except pymysql.IntegrityError:
            self.db.rollback()
            raise UserWarning('The comment is existing!')
        except:
            self.db.rollback()
            raise Exception('Insert error! Fail to insert the comment.')

    def insertSignedComments(self, comment):
        # time,comment_id,title,content,voteSum,voteCount,rating,version,user_name,app_id,isSpam
        sql = "Insert INTO SIGNEDCOMMENTS VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # sql statement arguments
        param = (comment[0], comment[1], comment[2],
                 comment[3], comment[4], comment[5],
                 comment[6], comment[7], comment[8],
                 comment[9], comment[10])
        # print(param)
        try:
            self.cursor.execute(sql, param)
            self.db.commit()
        except pymysql.IntegrityError:
            self.db.rollback()
            print('The comment is existing!')
        except:
            self.db.rollback()
            print('Insert error! Fail to insert the comment.')

    # get all app msgs from table appleApp,return ((appId1,appName1),(appId2,appName2)...)
    def getApps(self):
        sql = "SELECT * FROM APPLEAPP"
        try:
            self.cursor.execute(sql)
        except Exception:
            return None
        else:
            return self.cursor.fetchall()

    def queryComments(self):
        sql = "SELECT * FROM APPCOMMENTS NATURAL JOIN APPLEAPP"
        try:
            self.cursor.execute(sql)
        except Exception:
            return None
        else:
            return self.cursor.fetchall()

    def queryCommentsByAppId(self,appId):
        sql = "SELECT * FROM APPCOMMENTS NATURAL JOIN APPLEAPP WHERE APP_ID="+appId
        try:
            self.cursor.execute(sql)
        except Exception:
            return None
        else:
            return self.cursor.fetchall()

    def querySpamComments(self):
        sql = "SELECT * FROM SIGNEDCOMMENTS NATURAL JOIN APPLEAPP WHERE ISSPAM=1"
        try:
            self.cursor.execute(sql)
        except Exception:
            return None
        else:
            return self.cursor.fetchall()

    def insertApps(self,app):
        sql = "Insert INTO APPLEAPP VALUES (%s,%s)"
        param = tuple(app)
        # print(param)
        try:
            self.cursor.execute(sql, param)
            self.db.commit()
        except pymysql.IntegrityError:
            self.db.rollback()
            print("this app exist!")
        except:
            self.db.rollback()
            raise Exception('Insert error! Fail to insert the app.')

    # close comment database connection
    def closeConnect(self):
        self.db.close()
        print('\nClose database successfully!')

if __name__ == '__main__':
    print(CommentDbHandler('127.0.0.1','root','123456','appleAppComments').getApps())