import os

import sqlmodel
from sqlmodel import SQLModel, Session

DATABASE_URL=os.environ.get("DATABASE_URL") or "postgresql+psycopg://db_user:db_password@db_service:5432/db_name"

if DATABASE_URL == '':
    raise NotImplementedError("`DATABASE_URL` needs to be set.")
# this allows us to connect to the database using the DATABASE_URL environment variable, which is set in the .env file. The format of the DATABASE_URL is: postgresql+psycopg://user:password@host:port/dbname
engine = sqlmodel.create_engine(DATABASE_URL) 

# database models
def init_db():
    print('Creating database tables...')
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
