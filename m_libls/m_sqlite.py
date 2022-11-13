import os
import sqlite3


class sqlile_db:
    def __init__(self, path ):
        self.db_path = path
        # self.db_connection = None
        # self.db_cursor = None
        if os.path.exists(self.db_path) == False: 
            self.initial()
        else:
            self.db_connection = sqlite3.connect(self.db_path)
            self.db_cursor = self.db_connection.cursor()
        
    def initial (self):
        print (f"initial module")
        self.db_connection = sqlite3.connect(self.db_path)
        self.db_cursor = self.db_connection.cursor()
        sqlite_select_query = "select sqlite_version();"
        self.db_cursor.execute(sqlite_select_query)
        record = self.db_cursor.fetchall()
        print("SQLite Database has been created: ", record)
        with open(f'{os.getcwd()}/scr/create_db_initial.sql', 'r') as sqlite_file:
            sql_script = sqlite_file.read() 
        self.db_cursor.executescript(sql_script)

        # self.db_cursor.execute(sqlite_create_table_query)
        # self.db_connection.commit()
        # self.db_cursor.close()
    
    def get_all_prases (self):
        pass
    
    def add_phase (self, value_eng, value_ru):
        pass
    
    def remove_prase (self, rm_value):
        pass

    def close_connetion (self):
        self.db_cursor.close()
        self.db_connection.close()
