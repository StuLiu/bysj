
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
        sql = "SELECT * FROM signedcomments NATURAL JOIN appleapp " \
              "WHERE signedcomments.app_id='{}'".format((appId))
        # print(sql)
        try:
            self._cursor.execute(sql)
        except Exception as e:
            print("query appcomments error!", e)
            return None
        else:
            return self._cursor.fetchall()

    def queryCommentsByUserName(self,userName):
        sql = "SELECT * FROM signedcomments " \
              "WHERE user_name='{}'".format(userName)
        try:
            self._cursor.execute(sql)
        except Exception as e:
            print("query appcomments error!", e)
            return None
        else:
            return self._cursor.fetchall()

    def countByUserName(self,userName):
        sql = "SELECT COUNT(*) FROM signedcomments " \
              "WHERE signedcomments.user_name='{}'".format(userName)
        try:
            self._cursor.execute(sql)
        except Exception as e:
            print("query appcomments error!", e)
            return None
        else:
            return self._cursor.fetchone()[0]

    def contentIsUnique(self,content):
        sql = "SELECT COUNT(*) FROM signedcomments " \
              "WHERE signedcomments.content='{}'".format(content)
        try:
            self._cursor.execute(sql)
        except Exception as e:
            print("query appcomments error!", e)
            return None
        else:
            if self._cursor.fetchone()[0] > 1:
                return 0
            else:
                return 1


if __name__ == "__main__":
    handler = SignedCommentsDbHandler()

    # handler.insertSignedComment([
    #     "time","112546","asad","只要一部手机📱，躺在家里也能zuan0🌸💰➕为❤615912134",0,0,5,"v1","myname","1010704842","1"
    # ])
    print(handler.countByUserName(u"许飞的亟待解决的报道"))
    print(handler.countByUserName(u"绿的可能"))
    print(handler.contentIsUnique(u"快递快递咖啡咖啡咖啡咖啡咖啡咖啡咖啡看"))
    print(handler.contentIsUnique(u"Air 2的双屏功能能支持就能很好用了"))

    print(handler.queryCommentsByUserName("许飞的亟待解决的报道"))
    print(handler.queryCommentsByAppId('1118621880'))