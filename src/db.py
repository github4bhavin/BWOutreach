import sqlite3
import logging
import os

from config import SQLITE_DB_FILE

class OutreachDB(object):
    
    def __init__(self) -> None:
        self.con = sqlite3.connect(SQLITE_DB_FILE)
        
    def execute_sql_from_file(self, sql_file:str) -> None:
        if not os.path.exists(sql_file):
            logging.error(f"{sql_file} does not exist!")
            return None
    
        cur = self.con.cursor()
        sql_txt = open(sql_file).read()
        cur.execute(sql_txt)
        self.con.commit()
        return True