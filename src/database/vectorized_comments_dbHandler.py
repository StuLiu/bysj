
from database.dbHandler import DbHandler
class VectorizedCommentsDbHandler(DbHandler):
    "connect to mysql db and operate table vectorizedcomments"
    # connect to database named dbName，init db and cursor
    def __init__(self):
        DbHandler.__init__(self)

    def __del__(self):
        DbHandler.__del__(self)

    def insertVectorizedComment(self,sequence):
        sql = "INSERT INTO vectorizedcomments VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
              "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
              "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # sql statement arguments
        if len(sequence) != 53:
            print("insertVectorizedComment parameter error!")
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
        sql = "SELECT vectorizedcomments.*, " \
              "signedcomments.isSpam " \
              "FROM vectorizedcomments NATURAL JOIN signedcomments"
        try:
            self._cursor.execute(sql)
        except Exception as e:
            print("query VecterizedComment error!", e)
            return None
        else:
            return self._cursor.fetchall()

    # def query(self,limit):
    #     sql = "SELECT vectorizedcomments.comment_id, " \
    #           "vectorizedcomments.title_len, " \
    #           "vectorizedcomments.content_len, " \
    #           "vectorizedcomments.content_pl_rate, " \
    #           "vectorizedcomments.content_eng_rate, " \
    #           "vectorizedcomments.content_n_rate, " \
    #           "vectorizedcomments.content_v_rate, " \
    #           "vectorizedcomments.content_a_rate, " \
    #           "vectorizedcomments.content_x_rate, " \
    #           "vectorizedcomments.content_w_rate, " \
    #           "vectorizedcomments.content_y_rate, " \
    #           "vectorizedcomments.content_m_rate, " \
    #           "vectorizedcomments.comment_rating, " \
    #           "signedcomments.isSpam " \
    #           "FROM vectorizedcomments NATURAL JOIN signedcomments " \
    #           "limit "+str(limit)
    #     try:
    #         self._cursor.execute(sql)
    #     except Exception as e:
    #         print("query VecterizedComment error!", e)
    #         return None
    #     else:
    #         return self._cursor.fetchall()

    def querySpam(self):
        sql = "SELECT vectorizedcomments.*, " \
              "signedcomments.isSpam " \
              "FROM vectorizedcomments NATURAL JOIN signedcomments " \
              "WHERE signedcomments.isSpam='1'"
        try:
            self._cursor.execute(sql)
        except Exception as e:
            print("query VecterizedComment error!", e)
            return None
        else:
            return self._cursor.fetchall()

    def queryNotSpam(self):
        sql = "SELECT vectorizedcomments.*, " \
              "signedcomments.isSpam " \
              "FROM vectorizedcomments NATURAL JOIN signedcomments " \
              "WHERE signedcomments.isSpam='0' "
        try:
            self._cursor.execute(sql)
        except Exception as e:
            print("query VecterizedComment error!", e)
            return None
        else:
            return self._cursor.fetchall()

if __name__ == "__main__":
    handler = VectorizedCommentsDbHandler()
    print(type(handler.querySpam()[0][-1]))
    # handler.insertVectorizedComment(['22222',1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0
    #                                     , 1.0, 1.0, 1.0, 1.0, 1.0,1.0,1.0,1.0,1.0,1.0
    #                                     , 1.0, 1.0, 1.0, 1.0, 1.0,1.0,1.0,1.0,1.0,1.0
    #                                     , 1.0, 1.0, 1.0, 1.0, 1.0,1.0,1.0,1.0,1.0,1.0
    #                                     , 1.0, 1.0, 1.0, 1.0, 1.0,1.0,1.0,1.0,1.0,1.0
    #                                  ,1.0,1.0])
    # print(handler.queryNotSpam(10))
    # print(handler.query(5))
    # print(handler.queryAll())
    # handler.insertVectorizedComment([
    #     "1404494927",1,2,3.,4.,5.,6.,7.,8.,9.,10.,11.,12
    # ])
