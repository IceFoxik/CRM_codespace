# repositories/abstract.py
import psycopg2
from abc import ABC, abstractmethod


class StudentRepositoryABC(ABC):
    @abstractmethod
    def add_teacher(self, tg_id):
        pass

    @abstractmethod
    def get_teacher(self, tg_id):
        pass


class TeacherRepository(StudentRepositoryABC):
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="wg_forge_db",
            host="localhost",
            user="wg_forge",
            password="42a",
            port="5432"
        )
        self.cursor = self.conn.cursor()

    def add_teacher(self, tg_id) -> bool:
        try:
            self.cursor.execute("INSERT INTO teachers (telegram_id) VALUES (%s)", (tg_id,))
            self.conn.commit()
            return True
        except psycopg2.Error as e:
            print(f"Ошибка добавления учителя: {e}")
            self.conn.rollback()
            return False
    def get_teacher(self, tg_id):
        try:
            self.cursor.execute("SELECT * FROM teachers WHERE telegram_id=%s", (tg_id,))
            return True if self.cursor.fetchone() else False
        except psycopg2.Error as e:
            print(f"Ошибка получения студента: {e}")
            return None
    def close(self):
        self.cursor.close()
        self.conn.close()

conn = psycopg2.connect(
    dbname="postgres",
    host="localhost",
    user="postgres",
    password="password",
    port="5432"
)
cur = conn.cursor()
cur.execute("INSERT INTO servers (server, cost) VALUES (%s, %s);", ("server1", 100))
conn.commit()
cur.execute("INSERT INTO servers (server, cost) VALUES (%s, %s);", ("server2", 200))
conn.commit()
cur.execute("INSERT INTO servers (server, cost) VALUES (%s, %s);", ("server3", 300))
conn.commit()
cur.execute("SELECT * FROM servers WHERE server=%s", ('server1',))
cur.fetchone()
print(cur.fetchone())

conn = psycopg2.connect(
    dbname="postgres",
    host="localhost",
    user="postgres",
    password="password",
    port="5432"
)
cur = conn.cursor()
request_to_read_serv = "SELECT * FROM servers"

cur.execute(request_to_read_serv)

data = cur.fetchall()

