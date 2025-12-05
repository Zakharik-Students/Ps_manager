import psycopg2

conn = psycopg2.connect(database = 'weather',
                        user = 'zakhar',
                        host = 'localhost',
                        port = 5432)
cur = conn.cursor()


def insert():
    cur.execute("""INSERT INTO weather VALUES ('Kireevsk', 2, 35)""")
    conn.commit()
    cur.close()
    conn.close()

insert()
