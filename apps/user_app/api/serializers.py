from marshmallow import ValidationError, validate

from extensions import ma

from models.user import User, Profile


def validate_email(email):
    if User.query.filter_by(email=email).first():
        raise ValidationError("Email id is already exists.")


# def validate_username(username):
#     if User.query.filter_by(username=username).first():
#         raise ValidationError("Username is already exists.")


class ProfileSchema(ma.ModelSchema):
    class Meta:
        model = Profile
        fields = ('address1',)


class UserSchema(ma.ModelSchema):
    email = ma.Email(required=True, validate=validate_email)
    password = ma.String(max_length=8, validate=validate.Length(
        min=6, max=10), required=True)
    profile = ma.Nested(ProfileSchema, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'modified_on', 'profile')
        load_only = ('password',)
        dump_only = ('id', 'modified_on')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UserLoginSchema(ma.Schema):
    email = ma.Email(required=True)
    password = ma.String(
        required=True, validate=validate.Length(min=8, max=24))

    class Meta:
        # Fields to expose
        fields = ('email', 'password')
        load_only = ('password',)  # write-only fields


user_login_schema = UserLoginSchema()
