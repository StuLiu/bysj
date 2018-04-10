import pymysql
from database.dataBaseArgs import DataBaseArgs

class DbHandler(object):
    "connect to mysql db "
    # connect to database，init db and cursor
    def __init__(self):
        try:
            self._db = pymysql.connect(DataBaseArgs.getUrl(), DataBaseArgs.getUserName(),
                DataBaseArgs.getPassWord(),DataBaseArgs.getDataBase(),charset='utf8mb4')
        except:
            print('Connect comments database failed!\n');exit(1)
        else:
            print('Connect comments database successfully\n')
        self._cursor = self._db.cursor()

    def __del__(self):
        self._db.close()
        print('\nClose database successfully!')
