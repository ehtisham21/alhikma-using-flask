from flask import Flask
from configuration import config
from database.db import db, migrate

app = Flask(__name__)

app.config.from_object(config.DatabaseCredentials)

db.init_app(app)
migrate.init_app(app,db)
from app import api
from core import *
app.register_blueprint(core, url_prefix='/')
# with app.app_context():
#     db.create_all()