import sqlite3
import os

class sqlile_db:
    def __init__(self, path ):
        self.db_path = path
        self.db_connection = None
        self.db_cursor = None
        self.initial() if os.path.exists(self.db_path) == False else None
        
    def initial (self):
        print ("initial module")
        self.db_connection = sqlite3.connect(self.db_path)
        self.db_cursor = self.db_connection.cursor()
        sqlite_select_query = "select sqlite_version();"
        self.db_cursor.execute(sqlite_select_query)
        record = self.db_cursor.fetchall()
        print("Версия базы данных SQLite: ", record)
        self.db_cursor.close()
        
        print(os.path.exists(self.db_path))
        pass

