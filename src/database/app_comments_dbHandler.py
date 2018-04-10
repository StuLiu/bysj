import pymysql
from database.dbHandler import DbHandler
class AppCommentsDbHandler(DbHandler):
    "connect to mysql db and operate table appleapp"
    def __init__(self):
        DbHandler.__init__(self)

    def __del__(self):
        DbHandler.__del__(self)

    # insert a comment entry into table named appComments
    # if the comment exist,raise a UserWaring
    # if insert failed for other reason,raise a Exception
    def insertAppComment(self,sequence):
        # time,comment_id,title,content,voteSum,voteCount,rating,version,user_name,app_id,isSpam
        sql = "INSERT INTO appcomments VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # sql statement arguments
        param = tuple(sequence)
        # print(param)
        try:
            self._cursor.execute(sql,param)
            self._db.commit()
        except pymysql.IntegrityError:
            self._db.rollback()
            raise UserWarning('The comment is existing!')
        except:
            self._db.rollback()
            raise Exception('Insert error! Fail to insert the comment.')

    def queryAll(self):
        sql = "SELECT * FROM appcomments NATURAL JOIN appleapp"
        try:
            self._cursor.execute(sql)
        except Exception as e:
            print("query appcomments error!",e)
            return None
        else:
            return self._cursor.fetchall()

    def queryCommentsByAppId(self,appId):
        sql = "SELECT * FROM appcomments NATURAL JOIN appleapp WHERE app_id="+appId
        try:
            self._cursor.execute(sql)
        except Exception as e:
            print("query appcomments error!", e)
            return None
        else:
            return self._cursor.fetchall()

    def count(self):
        sql = "SELECT COUNT(*) FROM appcomments"
        try:
            self._cursor.execute(sql)
        except Exception as e:
            print("count appcomments error!", e)
            return None
        else:
            return self._cursor.fetchone()[0]

if __name__ == "__main__":
    handler = AppCommentsDbHandler()
    # handler.insertAppComment([
    #     "time","cid","title","content",1,1,5,'version','username','1010704842','0'
    # ])

    result = handler.queryAll()
    print(result)
    print(len(result))

    print(handler.count())

