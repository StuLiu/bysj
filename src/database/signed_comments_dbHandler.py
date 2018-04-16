
from database.dbHandler import DbHandler
class SignedCommentsDbHandler(DbHandler):
    "connect to mysql db and operate table signedcomments"
    def __init__(self):
        DbHandler.__init__(self)

    def __del__(self):
        DbHandler.__del__(self)

    def insertSignedComment(self,sequence):
        sql = "INSERT INTO signedcomments VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # sql statement arguments
        if len(sequence) != 11:
            print("insertSignedComment parameter error!")
            return
        param = tuple(sequence)
        # print(param)
        try:
            self._cursor.execute(sql, param)
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            print("insertVectorizedComment error!",e)

    def queryAll(self):
        sql = "SELECT * FROM signedcomments"
        try:
            self._cursor.execute(sql)
        except Exception as e:
            print("qurey error!",e)
            return None
        else:
            return self._cursor.fetchall()

    def querySpam(self):
        sql = "SELECT * FROM signedcomments WHERE isSpam=1"
        try:
            self._cursor.execute(sql)
        except Exception as e:
            print("qurey error!",e)
            return None
        else:
            return self._cursor.fetchall()

    def queryNotSpam(self):
        sql = "SELECT * FROM signedcomments WHERE isSpam=0"
        try:
            self._cursor.execute(sql)
        except Exception as e:
            print("qurey error!",e)
            return None
        else:
            return self._cursor.fetchall()

    def queryCommentsByAppId(self,appId):
        sql = "SELECT * FROM signedcomments NATURAL JOIN appleapp WHERE app_id="+appId
        try:
            self._cursor.execute(sql)
        except Exception as e:
            print("query appcomments error!", e)
            return None
        else:
            return self._cursor.fetchall()

if __name__ == "__main__":
    handler = SignedCommentsDbHandler()

    # handler.insertSignedComment([
    #     "time","112546","asad","只要一部手机📱，躺在家里也能zuan0🌸💰➕为❤615912134",0,0,5,"v1","myname","1010704842","1"
    # ])
    print(len(handler.queryAll()))
