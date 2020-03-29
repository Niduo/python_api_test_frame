from common.configRead import ConfigRead
import pymysql

readConfig = ConfigRead()


class MyDB:
    global host, username, password, port, database, config
    host = readConfig.get_db("host")
    username = readConfig.get_db("username")
    password = readConfig.get_db("password")
    port = readConfig.get_db("port")
    database = readConfig.get_db("database")
    config = {
        'host': str(host),
        'user': username,
        'passwd': password,
        'port': int(port),
        'db': database
    }

    def __init__(self):
        self.db = None
        self.cursor = None

    def connectDB(self):
        try:
            # connect to DB
            self.db = pymysql.connect(**config)
            # create cursor
            self.cursor = self.db.cursor()
            print("Connect DB successfully!")
        except ConnectionError as ex:
            print(str(ex))

    def executeSQL(self, sql, params):
        self.connectDB()
        # executing sql
        self.cursor.execute(sql, params)
        # executing by committing to DB
        self.db.commit()
        return self.cursor

    def get_all(self, cursor):
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        value = cursor.fetchone()
        return value

    def closeDB(self):
        self.db.close()
        print("Database closed!")