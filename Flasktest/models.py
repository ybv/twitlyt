from sqlalchemy import Column, Integer, String
from Flasktest.database import Base

class User(Base):
  __tablename__ = 'users'
  id = Column('user_id',Integer, primary_key=True)
  name = Column(String(20), unique=True)
  oauth_token = Column(String(20), unique=False)
  oauth_secret = Column(String(200), unique=False)

  def __init__(self, name):
	self.name = name
  def __repr__(self):
	'<User %r>' % (self.name)
