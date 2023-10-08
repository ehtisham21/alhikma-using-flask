from sqlalchemy import String, Column, Integer
from app import db
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(28), nullable=False, unique=True)
    first_name = Column(String(28), nullable=False, unique=True)
    last_name = Column(String(28), nullable=False, unique=True)
    cnic_number = Column(String(28), nullable=False)
    phone_number = Column(String(28), nullable=False)

    def __int__(self, email, first_name, last_name, cnic_number, phone_number):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.cnic_number = cnic_number
        self.phone_number = phone_number

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self