
from database.dbHandler import DbHandler
class AppleAppDbHandler(DbHandler):
    "connect to mysql db and operate table appleapp"
    def __init__(self):
        DbHandler.__init__(self)

    def __del__(self):
        DbHandler.__del__(self)

    # get all app msgs from table appleApp,return ((appId1,appName1),(appId2,appName2)...)
    def queryAll(self):
        sql = "SELECT * FROM appleapp"
        try:
            self._cursor.execute(sql)
        except Exception as e:
            print("query appleapp error!",e)
            return None
        else:
            return self._cursor.fetchall()

if __name__ == "__main__":
    handler = AppleAppDbHandler()
    result = handler.queryAll()
    print(result)
    print(len(result))

