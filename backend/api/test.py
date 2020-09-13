from sqlalchemy import text, create_engine

def get_sql_connection():
    params = {
        "host": "test-database.ctyo46w3wzci.us-east-2.rds.amazonaws.com",
        "database": "youtube_sql",
        "user": "postgres",
        "password": "lego_10010"
    }
    engine = create_engine(
        'postgresql://{}:{}@{}/{}'.format(params["user"], params["password"], params["host"], params["database"])
        )
    conn = engine.connect()
    return conn

if __name__ == '__main__':
    conn = get_sql_connection()

    stmt = text("SELECT * FROM videos WHERE id=:p1;")
    stmt = stmt.bindparams(p1=2)
    x = conn.execute(stmt).fetchone()
    print(x.items())

    conn.close()