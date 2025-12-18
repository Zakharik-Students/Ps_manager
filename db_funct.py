import psycopg2
from psycopg2 import Binary

# connection with data base
def connect_db():
    conn = psycopg2.connect(database = 'Ps_manager',
                           user = 'zakhar',
                            host = 'localhost',
                            port = 5432)
    cur = conn.cursor()
    return(conn, cur)

#def close db
def disconnect_db(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

