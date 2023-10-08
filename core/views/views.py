from flask import jsonify, request, Response
from marshmallow import ValidationError

from core.models import User
from core.schemas.user_schema import UserSchema
from database.db import db


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
                # create_user = User(first_name, last_name, cnic_number, email, phone_number)
                # create_user.create()
                new_user = User(**validated_data)
                new_user.create()
                return Response('You have successfully signed up. Please check your email for confirmation.', status=201)
            else:
                return Response('You already have an account with this CNIC.', status=409)
        except ValidationError as err:
            return jsonify(err.messages), 400

    elif action_type == 'mosque':
        return jsonify(message='Mosque registration')
    else:
        return jsonify(message='Invalid action type')
