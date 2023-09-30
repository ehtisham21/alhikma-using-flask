from flask import jsonify
def register_view(action_type):
    if action_type == 'user':
        return jsonify(message='User registration')
    elif action_type == 'mosque':
        return jsonify(message='Mosque registration')
    else:
        return jsonify(message='Invalid action type')
