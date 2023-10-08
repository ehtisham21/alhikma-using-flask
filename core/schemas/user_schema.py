import re
from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
ma = Marshmallow()

class UserSchema(ma.Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    cnic_number = fields.Number(required= True)
    email = fields.Email(required=True)
    phone_number = fields.Number(required=True)


    @validates("first_name")
    def validate_first_name(self, value):
        if "first name" in value:
            raise ValidationError("Name cannot contain the word 'First Name'.")
        if not re.match("^[A-Z].*", value):
            raise ValidationError("The first letter of the first name must be uppercase.")
        if not re.match("^[a-zA-Z0-9_]+$", value):
            raise ValidationError("First Name can only contain letters, numbers, and underscores.")
        if len(value) < 3:
            raise ValidationError("Minimum length of first name must be 3.")

    @validates("last_name")
    def validate_last_name(self, value):
        if "last name" in value:
            raise ValidationError("Name cannot contain the word 'Last Name'.")
        if not re.match("^[A-Z].*", value):
            raise ValidationError("The first letter of the last name must be uppercase.")
        if not re.match("^[a-zA-Z0-9_]+$", value):
            raise ValidationError("Last Name can only contain letters, numbers, and underscores.")
        if len(value) < 3:
            raise ValidationError("Minimum length of last name must be 3.")
    @validates("email")
    def validate_email(self, value):
        if not re.match(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+.[A-Z|a-z]{2,}", value):
            raise ValidationError("Please recheck your email.")

    @validates("cnic_number")
    def validate_cnic_number(self, value):
        if len(str(value)) < 13:
            raise ValidationError("Cnic  number  must be at least 13 numbers long.")
        # if not all(p.isdigit() for p in value):
        #     raise ValidationError("All CNIC numbers must be numbers.")
        # cnic_pattern = re.compile(r'^\d{5}-\d{7}-\d{1}$')
        # if not cnic_pattern.match(str(value)):
        #     raise ValidationError("Please enter a valid CNIC number in the format '12345-9456875-1'.")

    # @validates("phone_number")
    # def validate_phone_number(self, value):
    #     if not re.match("^\d{11}$", str(value)):
    #         raise ValidationError("Please enter a valid 11-digit phone number with only numeric characters.")