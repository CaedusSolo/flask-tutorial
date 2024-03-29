from sqlalchemy import create_engine, text   #  import necessary libraries and modules
import creds
#  link to connect to database
engine = create_engine(creds.db_connection_string)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))

        result_all = result.all()
        jobs = []
        for row in result_all:
            jobs.append(dict(row._mapping))
    
        return jobs