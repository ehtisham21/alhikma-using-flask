from flask import Blueprint
from .views import *

register = Blueprint('register', __name__)
register.add_url_rule('sign-up/<string:action_type>', view_func=register_view, methods=['GET'])
