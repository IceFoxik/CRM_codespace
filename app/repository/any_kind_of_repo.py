import psycopg2
from psycopg2 import sql

# Настройки подключения к базе данных
DB_CONFIG = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': 5432
}

def connect_to_db():
    """Подключение к базе данных."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None

def insert_server(server_name, cost):
    """Добавление новой записи в таблицу servers."""
    conn = connect_to_db()
    if conn is None:
        return
    try:
        with conn.cursor() as cur:
            query = "INSERT INTO servers (server, cost) VALUES (%s, %s);"
            cur.execute(query, (server_name, cost))
            conn.commit()
            print(f"Запись '{server_name}' успешно добавлена.")
    except Exception as e:
        print(f"Ошибка при добавлении записи: {e}")
    finally:
        conn.close()

def read_servers():
    """Чтение всех записей из таблицы servers."""
    conn = connect_to_db()
    if conn is None:
        return
    try:
        with conn.cursor() as cur:
            query = "SELECT * FROM servers;"
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                print(f"ID: {row[0]}, Server: {row[1]}, Cost: {row[2]}")
    except Exception as e:
        print(f"Ошибка при чтении записей: {e}")
    finally:
        conn.close()

def read_server_by_name(server_name):
    """Чтение записи по имени сервера."""
    conn = connect_to_db()
    if conn is None:
        return
    try:
        with conn.cursor() as cur:
            query = "SELECT * FROM servers WHERE server = %s;"
            cur.execute(query, (server_name,))
            row = cur.fetchone()
            if row:
                print(f"ID: {row[0]}, Server: {row[1]}, Cost: {row[2]}")
            else:
                print(f"Сервер с именем '{server_name}' не найден.")
    except Exception as e:
        print(f"Ошибка при чтении записи: {e}")
    finally:
        conn.close()

def delete_server(server_id):
    """Удаление записи из таблицы servers по ID."""
    conn = connect_to_db()
    if conn is None:
        return
    try:
        with conn.cursor() as cur:
            query = "DELETE FROM servers WHERE id = %s;"
            cur.execute(query, (server_id,))
            conn.commit()
            if cur.rowcount > 0:
                print(f"Запись с ID {server_id} успешно удалена.")
            else:
                print(f"Запись с ID {server_id} не найдена.")
    except Exception as e:
        print(f"Ошибка при удалении записи: {e}")
    finally:
        conn.close()

def reset_table():
    """Сброс таблицы и последовательности для id."""
    conn = connect_to_db()
    if conn is None:
        return
    try:
        with conn.cursor() as cur:
            query = "TRUNCATE TABLE servers RESTART IDENTITY;"
            cur.execute(query)
            conn.commit()
            print("Таблица очищена, и последовательность для id сброшена.")
    except Exception as e:
        print(f"Ошибка при сбросе таблицы: {e}")
    finally:
        conn.close()

# Основной блок выполнения
if __name__ == "__main__":
    # Добавление записей
    insert_server("server1", 100)
    insert_server("server2", 200)
    insert_server("server3", 300)

    # Чтение всех записей
    print("\nВсе записи в таблице:")
    read_servers()

    # Чтение записи по имени
    print("\nЧтение записи по имени:")
    read_server_by_name("server1")

    # Удаление записи
    print("\nУдаление записи:")
    delete_server(1)
    
    # Повторное чтение всех записей после удаления
    print("\nПовторное чтение всех записей:")
    read_servers()

    # Сброс таблицы
    # reset_table()
