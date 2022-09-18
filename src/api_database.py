import sqlite3 as sql


conn = sql.connect('api_handler.db', check_same_thread=False)
cursor = conn.cursor()

def create_table():
    with open("create_table.sql", "r") as sqlQuery:
        query = sqlQuery.read()

    cursor.execute(query)

def consulting_db():
    with open("consulting.sql", 'r') as sqlQuery:
        query = sqlQuery.read()
    cursor.execute(query)

def insert_db(inputs, begin_time, end_time, processing_timer):
    with open("insert.sql", 'r') as sqlQuery:
        query = sqlQuery.read()
    cursor.execute(query, (inputs, begin_time, end_time, processing_timer))
    conn.commit()


def close_connection():
    cursor.close()
    conn.close()
