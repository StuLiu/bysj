
from database.dbHandler import DbHandler
class VectorizedContentsDbHandler(DbHandler):
    "connect to mysql db and operate table vectorizedcomments"
    # connect to database named dbName，init db and cursor
    def __init__(self):
        DbHandler.__init__(self)

    def __del__(self):
        DbHandler.__del__(self)

    def insertVectorizedContent(self,sequence):
        sql = "INSERT INTO vectorizedcontents VALUES (%s,%s)"
        # sql statement arguments
        if len(sequence) != 2:
            print("insertVectorizedContent parameter error!")
            return
        param = tuple(sequence)
        # print(param)
        try:
            self._cursor.execute(sql, param)
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            print("insertVectorizedContent error!",e)

    def queryAll(self):
        sql = "SELECT vectorizedcontents.comment_id, " \
              "vectorizedcontents.vectorString, " \
              "signedcomments.isSpam FROM " \
              "vectorizedcontents NATURAL JOIN signedcomments"
        try:
            self._cursor.execute(sql)
        except Exception as e:
            print("query VectorizedContent error!", e)
            return None
        else:
            return self._cursor.fetchall()

    def querySpam(self, limit):
        sql = "SELECT vectorizedcontents.comment_id, " \
              "vectorizedcontents.vectorString, " \
              "signedcomments.isSpam FROM " \
              "vectorizedcontents NATURAL JOIN signedcomments " \
              "WHERE signedcomments.isSpam='1' " \
              "limit "+str(limit)
        try:
            self._cursor.execute(sql)
        except Exception as e:
            print("query VectorizedContent error!", e)
            return None
        else:
            return self._cursor.fetchall()

    def queryNotSpam(self, limit):
        sql = "SELECT vectorizedcontents.comment_id, " \
              "vectorizedcontents.vectorString, " \
              "signedcomments.isSpam FROM " \
              "vectorizedcontents NATURAL JOIN signedcomments " \
              "WHERE signedcomments.isSpam='0' " \
              "limit "+str(limit)
        try:
            self._cursor.execute(sql)
        except Exception as e:
            print("query VectorizedContent error!", e)
            return None
        else:
            return self._cursor.fetchall()
if __name__ == "__main__":
    handler = VectorizedContentsDbHandler()
    # handler.insertVectorizedContent(['1358689594','158 55'])
    print(len(handler.querySpam(111111)))
    print(len(handler.queryNotSpam(11111111)))
    # print(handler.query(5))
    # print(handler.queryAll())
    # handler.insertVectorizedComment([
    #     "1404494927",1,2,3.,4.,5.,6.,7.,8.,9.,10.,11.,12
    # ])
