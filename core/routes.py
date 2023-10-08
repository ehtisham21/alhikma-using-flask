from flask import Blueprint
from .views import *

core = Blueprint('core', __name__)
core.add_url_rule('sign-up/<string:action_type>', view_func=register_view, methods=['POST'])
