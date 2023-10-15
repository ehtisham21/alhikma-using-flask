from sqlalchemy import String, Column, Integer
from app import db


class Mosques(db.Model):
    __tablename__ = 'mosques'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(28), nullable=False, unique=True)
    mosque_name = Column(String(28), nullable=False)
    mosque_address = Column(String(28), nullable=False)
    password = Column(String(28), nullable=False)

    def __init__(self, email, mosque_name, mosque_address, password):
        self.email = email
        self.mosque_name = mosque_name
        self.mosque_address = mosque_address
        self.password = password

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self