from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

uri = os.environ.get('DATABASE_URL', 'postgres://hxhebarhtwakjb:BqP0tr8Vwy8k3bhYjYW0fJHRMh@ec2-23-23-211-161.compute-1.amazonaws.com:5432/d4e678cmliti44')
engine = create_engine(uri, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
					 autoflush=False,
					 bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
  import Flasktest.models
  Base.metadata.create_all(bind=engine)