import psycopg2
import psycopg2.extras

import configure as cf


class Db:
    def __init__(self):
        self.connection = psycopg2.connect(user=cf.USER,
                                           password=cf.PASSWORD,
                                           host=cf.HOST,
                                           port=cf.PORT,
                                           database=cf.DB_NAME)
        self.connection.autocommit = True
        self.cur = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        
   
    '''
    таблица для пользователя
    '''
    def create_users_table(self):
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS users (
                    id_user SERIAL PRIMARY KEY,
                    name VARCHAR(32),
                    email VARCHAR(255),
                    result VARCHAR(255)
                );"""
        )
    # Здесь мы передаём информацию о пользователе/админах/сообщениях от пользователя
    def insert_user(self, id_user, name, email, result):
        self.cur.execute(
            """INSERT INTO users (id_user, name, email, result) VALUES (%s, %s, %s, %s);""",
            (id_user, name, email, result,)
        )
        return True
    
    '''
    таблица для готовых данных
    '''


db = Db()
db.create_users_table()