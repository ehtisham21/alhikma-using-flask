from sqlalchemy import String, Column, Integer
from app import db
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(28), nullable=False, unique=True)
    username = Column(String(28), nullable=False, unique=True)
    password = Column(String(28), nullable=False)

    def __int__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self