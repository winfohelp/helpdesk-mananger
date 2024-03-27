import sqlite3

class SQlite:
    def __init__(self, db_path: str):
        self.db_path = db_path
    
        
    def connect(self):
        return sqlite3.connect(self.db_path)
    
    def cursor(self, conn):
        return conn.cursor()
    
    def execute(self, cursor, query):
        return cursor.execute(query)
    
    
QUERY = """
            CREATE TABLE IF NOT EXISTS ordens (
                id TEXT PRIMARY KEY,
                cliente TEXT,
                problema TEXT,
                solucao TEXT,
                valor REAL,
                servico_realizado TEXT
            )
        """

DB_PATH = "inmemory.db"

db = SQlite(DB_PATH)

conn = db.connect()

cursor = db.cursor(conn)

insert = db.execute(cursor,QUERY)
