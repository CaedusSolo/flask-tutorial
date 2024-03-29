from sqlalchemy import create_engine, text   #  import necessary libraries and modules
import os 
from dotenv import load_dotenv

def configure():
    load_dotenv()

configure()

#  link to connect to database
engine = create_engine(os.getenv('db_connection_string'))

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))

        result_all = result.all()
        jobs = []
        for row in result_all:
            jobs.append(dict(row._mapping))
    
        return jobs
    
def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("select * from jobs where id = :val"),
            {'val' : id})
        
        row = result.fetchone()
        if row:
            return row._asdict()
        else:
            return None