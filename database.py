from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://cyttestproject_continued:a0491153c4c73a17f4972591d7accf9fb75c47a7@x3o.h.filess.io:3307/cyttestproject_continued?charset=utf8mb4"
engine = create_engine(db_connection_string)

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(result.all())