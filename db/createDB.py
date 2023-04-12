import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('./db/MBTI.db', isolation_level=None)
        self.cursor = self.conn.cursor()

    def create_table_user(self):
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS user
                                (id_user INT PRIMARY KEY NOT NULL,
                                name TEXT NOT NULL,
                                surname TEXT NOT NULL,
                                email TEXT NOT NULL,
                                result TEXT NOT NULL);
                            ''')
    def insert_user(self, id_user, name, surname, email, result):
        self.cursor.execute('''
                            INSERT INTO user 
                                (id_user,
                                name,
                                surname,
                                email,
                                result)
                            VALUES (?, ?, ?, ?, ?);
                            ''', (id_user, name, surname, email, result))
    
    def create_table_results(self):
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS results
                                (id_results INTEGER PRIMARY KEY AUTOINCREMENT,
                                 TEXT NOT NULL,
                                two TEXT NOT NULL,
                                 TEXT NOT NULL,
                                result TEXT NOT NULL);
                            ''')