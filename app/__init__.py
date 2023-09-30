# import flask module
from flask import Flask
from configuration import config
from database.db import db
app = Flask(__name__)

app.config.from_object(config.DatabaseCredentials)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:localhost@db/alhikmaflaskapplication'

db.init_app(app)


from app import api
from models import user

with app.app_context():
    db.create_all()