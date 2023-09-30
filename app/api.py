
from flask import Response, jsonify,request

from app import *
from models import User


@app.route('/hello', methods=['GET'])
def hello():
    return Response('Hello', status=200)
@app.route('/register', methods=['POST'])
def register():

    if request.method == 'POST':
        data = request.get_json()  # Get JSON data from the request
        # Check if required fields are in the JSON data
        if 'username' not in data or 'email' not in data or 'password' not in data:
            return jsonify({'message': 'Missing fields'}), 400

        username = data['username']
        email = data['email']
        password = data['password']
        print(username,password,email)
        user_existed = db.session.query(User).filter_by(email=email).first()
        if not user_existed:
            create_user = User(username=username, email=email, password=password)
            create_user.create()
            return Response('You have successfully signed up. Please check your email for confirmation.', status=201)
        else:
            return Response('You already have an account with this email.', status=400)

