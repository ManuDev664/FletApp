import psycopg2

def connect():
    # CONECTAR CON POSTGRES
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1234",
        host="192.168.181.132",
        port="5433"
    )
    return conn