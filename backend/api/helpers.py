from sqlalchemy import create_engine

def get_engine():
    params = {
        "host": "test-database.ctyo46w3wzci.us-east-2.rds.amazonaws.com",
        "database": "youtube_sql",
        "user": "postgres",
        "password": "lego_10010"
    }

    from sqlalchemy import create_engine
    engine = create_engine(
        'postgresql://{}:{}@{}/{}'.format(params["user"], params["password"], params["host"], params["database"])
        )

    return engine