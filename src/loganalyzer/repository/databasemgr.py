import sqlite3
from typing import Optional
from pathlib import Path
import logging

log = logging.getLogger(__name__)

DATABASE_NAME = 'logdb.db'

default_dbpath = Path(__file__).parent.parent.parent.parent / 'data' / DATABASE_NAME

class DatabaseManager():

    def __init__(self, db_path_param=default_dbpath) -> None:
        self.db_path: str = str(db_path_param)
        self.conn: Optional[sqlite3.Connection] = None

    
    def connect(self):
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_path)
        return self.conn
    

    def init_database(self):
        """
        Not it's not thread safe yet.
        """
        log.warning('This method is not thread safe')
        log.info('Initializing database')
        connection = self.connect()
        connection.execute('''
        CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT NOT NULL,
        http_method TEXT,
        http_api_path TEXT,
        http_response_code TEXT
        )
        ''')
        connection.commit()
    

    def execute_sql(self, query: str):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as ex:
            log.error(f"unexpected error happened while running {query}")
            return None
    

    def close_connection(self):
        try:
            self.conn.close
            self.conn = None
        except Exception as ex:
            log.error('an unexpected error happned while closing connection')


if __name__ == '__main__':
    db_obj = DatabaseManager()
    db_obj.init_database()
    
    #let's add some data to it
    db_obj.execute_sql("INSERT INTO logs (ip, http_method, http_api_path, http_response_code) VALUES ('127.0.0.1', 'GET', '/api/users', '200')")

    rs = db_obj.execute_sql("select * from logs")
    log.info(f"-----------------the feched ip is {rs[1]}")
