import bcrypt
from flask import jsonify, request, Response
from marshmallow import ValidationError

from core.models import User, Mosques
from core.schemas.user_schema import UserSchema
from werkzeug.security import check_password_hash
def register_view(action_type):
    if action_type == 'user':
        # data = request.get_json()
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        cnic_number= request.form.get('cnic_number')
        email= request.form.get('email')
        phone_number= request.form.get('phone_number')

        user_schema = UserSchema()
        try:
            validated_data = user_schema.load({'first_name': first_name, 'last_name': last_name, 'cnic_number':cnic_number,
                                              'email':email,'phone_number':phone_number})
            user_existed = User.query.filter_by(cnic_number=validated_data['cnic_number']).first()
            if not user_existed:
                new_user = User(**validated_data)
                new_user.create()
                return Response('You have successfully signed up. Please check your email for confirmation.', status=201)
            else:
                return Response('You already have an account with this CNIC.', status=409)
        except ValidationError as err:
            return jsonify(err.messages), 400

    elif action_type == 'mosque':
        email = request.form.get('email')
        mosque_name = request.form.get('mosque_name')
        mosque_address = request.form.get('mosque_address')
        password = request.form.get('password')
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        mosque_existed = Mosques.query.filter_by(email=email).first()
        if not mosque_existed:
            create_mosque = Mosques(email, mosque_name, mosque_address, hashed_password)
            create_mosque.create()  # Here calling create functing to store the data in table.
            return Response('You have successfully signed up. Please check your email for confirmation.', status=201)
        else:
            return Response('You already have an account with this email.', status=409)
    else:
        return jsonify(message='Invalid action type')
