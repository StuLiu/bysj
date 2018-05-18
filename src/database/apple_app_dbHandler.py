
from database.dbHandler import DbHandler
class AppleAppDbHandler(DbHandler):
    "connect to mysql db and operate table appleapp"
    def __init__(self):
        DbHandler.__init__(self)

    def __del__(self):
        DbHandler.__del__(self)

    # get all app msgs from table appleApp,return ((appId1,appName1),(appId2,appName2)...)
    def queryAll(self):
        sql = "SELECT app_id, app_name, rating_mean FROM appleapp"
        try:
            self._cursor.execute(sql)
        except Exception as e:
            print("query appleapp error!",e)
            return None
        else:
            return self._cursor.fetchall()

    def updateRatingMean(self, appId, ratingMean):
        sql = "UPDATE appleapp set rating_mean={} " \
              "WHERE appleapp.app_id='{}'".format(ratingMean, appId)
        print(appId, ratingMean, sql)
        try:
            self._cursor.execute(sql)
            self._db.commit()
        except Exception as e:
            print("query appleapp error!",e)
            self._db.rollback()

    def getRatingMeanByAppId(self,appId):
        sql = "SELECT appleapp.rating_mean FROM appleapp " \
              "WHERE app_id='{}'".format(appId)
        try:
            self._cursor.execute(sql)
        except Exception as e:
            print("query appleapp error!", e)
            return None
        else:
            return self._cursor.fetchone()[0]

if __name__ == "__main__":
    handler = AppleAppDbHandler()
    # result = handler.queryAll()
    # print(result)
    # print(len(result))
    # handler.updateRatingMean('1010704842', 3.0)
    print(handler.getRatingMeanByAppId('1010704842'))
    print(handler.queryAll())
