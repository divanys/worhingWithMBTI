import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('./db/MBTI.db', isolation_level=None)
        self.cursor = self.conn.cursor()

    def create_table_user(self):
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS user
                                (id_user INTEGER PRIMARY KEY NOT NULL,
                                result TEXT NOT NULL,
                                brightness INTEGER NOT NULL,
                                surname TEXT NOT NULL,
                                name TEXT NOT NULL,
                                email TEXT NOT NULL);
                            ''')
    def insert_user(self, id_user, result, brightness, surname, name, email):
        self.cursor.execute('''
                            INSERT INTO user 
                                (id_user,
                                result,
                                brightness,
                                surname,
                                name,
                                email)
                            VALUES (?, ?, ?, ?, ?, ?);
                            ''', (id_user, result, brightness, surname, name, email))
    
    def create_table_results(self):
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS results
                                (id_results INTEGER PRIMARY KEY AUTOINCREMENT,
                                abbreviation TEXT NOT NULL,
                                personality_type TEXT NOT NULL,
                                e_i TEXT NOT NULL,
                                s_n TEXT NOT NULL,
                                t_f TEXT NOT NULL,
                                j_p TEXT NOT NULL,
                                total TEXT NOT NULL);
                            ''')
        
    def insert_user(self, id_results, abbreviation, personality_type, e_i, s_n, t_f, j_p, total):
        self.cursor.execute('''
                            INSERT INTO user 
                                (id_results,
                                abbreviation,
                                personality_type,
                                e_i,
                                s_n,
                                t_f,
                                j_p,
                                total);
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
                            ''', (id_results, abbreviation, personality_type, e_i, s_n, t_f, j_p, total))