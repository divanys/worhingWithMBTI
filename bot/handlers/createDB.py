import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('./db/MBTI.db', isolation_level=None)
        self.cursor = self.conn.cursor()

    

    def create_table_user(self):
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS user
                                (id_user INTEGER PRIMARY KEY NOT NULL,
                                result TEXT ,
                                brightness INTEGER ,
                                surname TEXT ,
                                name TEXT ,
                                email TEXT );
                            ''')
    def insert_user_id(self, id_user):
        self.cursor.execute('''
                            INSERT INTO user 
                                (id_user)
                            VALUES (?);
                            ''', (id_user,))
    
    def insert_user_result(self, id_user, result):
        self.cursor.execute('''
                            INSERT INTO user 
                                (result)
                            VALUES (?)
                            WHERE id_user=?;
                            ''', (result, id_user,))
        
    def insert_user_brightness(self, id_user, brightness):
        self.cursor.execute('''
                            INSERT INTO user 
                                (brightness)
                            VALUES (?)
                            WHERE id_user=?;
                            ''', (brightness, id_user,))
    
    def insert_user_surname(self, id_user, surname):
        self.cursor.execute('''
                            INSERT INTO user 
                                (surname)
                            VALUES (?)
                            WHERE id_user=?;
                            ''', (surname, id_user,))
        
    def insert_user_name(self, id_user, name):
        self.cursor.execute('''
                            INSERT INTO user 
                                (name)
                            VALUES (?)
                            WHERE id_user=?;
                            ''', (name, id_user,))
        
    def insert_user_email(self, id_user, email):
        self.cursor.execute('''
                            INSERT INTO user 
                                (email)
                            VALUES (?)
                            WHERE id_user=?;
                            ''', (email, id_user,))
    

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
                                            WHERE id_user=?""", (result, brightness, surname, name, email, id_user,))

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
      


    def select_results(self, id_user):
        self.cursor.execute("SELECT abbreviation, personality_type, e_i, s_n, t_f, j_p, total FROM results WHERE id_user=?", (id_user,))
        rows = self.cursor.fetchall()
        return list(rows)
    

    def create_table_answers(self):
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS answers 
                            (id_answers INTEGER PRIMARY KEY AUTOINCREMENT,
                            id_user INTEGER,
                            num_question INTEGER NOT NULL,
                            question TEXT NOT NULL,
                            answer TEXT NOT NULL,
                            o_or_z INTEGER, 
                            FOREIGN KEY (id_user) REFERENCES user(id_user));
                            ''')
        
    def insert_answers(self, id_user, num_question, question, answer):
        self.cursor.execute('''
                            INSERT INTO answers 
                                (id_user,
                                num_question,
                                question,
                                answer)
                            VALUES (?, ?, ?, ?);
                            ''', (id_user, num_question, question, answer))
        
    def insert_answers_o_or_z(self, id_user, num_question, o_or_z):
        self.cursor.execute('''
                            UPDATE answers 
                            SET o_or_z=?
                            WHERE id_user=? AND num_question=?;
                            ''', (o_or_z, id_user, num_question,))
        
    def select_answers_answer(self, id_user, num_question):
        self.cursor.execute('''
                            SELECT answer
                            FROM answers
                            WHERE id_user=? AND num_question=?; 
                            ''', (id_user, num_question,))
        row = self.cursor.fetchall()
        return row

    def select_answers(self, id_user):
        self.cursor.execute("SELECT * FROM answers WHERE id_user=?", (id_user,))
        rows = self.cursor.fetchall()
        return rows
    
    # def select_