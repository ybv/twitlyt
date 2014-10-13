from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("/etc/psycopg.conf")
URI = Config.get("DB", "db-URI")

uri = os.environ.get('DATABASE_URL', URI)
engine = create_engine(uri, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
					 autoflush=False,
					 bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
  import Flasktest.models
  Base.metadata.create_all(bind=engine)
