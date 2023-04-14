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
    
    def check_user_exists(self, id_user):
        self.cursor.execute("SELECT * FROM user WHERE id_user=?", (id_user,))
        result = self.cursor.fetchone()
        if result:
            return True
        else:
            return False
        
    def update_user(self, id_user, result, brightness, surname, name, email):
        self.cursor.execute("""
                            UPDATE user SET result=?,
                                            brightness=?,
                                            surname=?,
                                            name=?,
                                            email=?
                                            WHERE id_user=?""", (result, brightness, surname, name, email, id_user))

    def create_table_results(self):
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS results
                                (id_results INTEGER PRIMARY KEY AUTOINCREMENT,
                                abbreviation TEXT NOT NULL,
                                personality_type TEXT NOT NULL,
                                e_i INTEGER NOT NULL,
                                s_n INTEGER NOT NULL,
                                t_f INTEGER NOT NULL,
                                j_p INTEGER NOT NULL,
                                total INTEGER NOT NULL,
                                id_user INTEGER,
                                FOREIGN KEY (id_user) REFERENCES user(id_user));
                            ''')
        
    def insert_results(self, abbreviation, personality_type, e_i, s_n, t_f, j_p, total, id_user):
        self.cursor.execute('''
                            INSERT INTO results 
                                (abbreviation,
                                personality_type,
                                e_i,
                                s_n,
                                t_f,
                                j_p,
                                total,
                                id_user)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
                            ''', (abbreviation, personality_type, e_i, s_n, t_f, j_p, total, id_user))
        
    # def update_result(self, id_results, abbreviation, personality_type, e_i, s_n, t_f, j_p, total, id_user):
    #     self.cursor.execute("""
    #                         UPDATE results SET abbreviation=?,
    #                                         personality_type=?,
    #                                         e_i=?,
    #                                         s_n=?,
    #                                         t_f=?,
    #                                         j_p=?,
    #                                         total=?
    #                                         WHERE id_user=?""", (id_results, abbreviation, personality_type, e_i, s_n, t_f, j_p, total, id_user))