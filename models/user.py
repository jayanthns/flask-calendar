from extensions import db
from database.db import BaseModelMixin
from passlib.hash import pbkdf2_sha256 as sha256
# from sqlalchemy.orm import relationship, backref


class User(BaseModelMixin):
    """User model to store user details"""

    __tablename__ = 'users'

    username = db.Column(db.String(100), default="")
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), default="")
    is_superuser = db.Column(db.Boolean(), default=False)

    profile = db.relationship(
        'Profile', backref="user", uselist=False, lazy=True
    )
    authenticated = db.Column(db.Boolean(), default=False)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = sha256.hash(password)

    def check_password(self, password):
        return sha256.verify(password, self.password_hash)

    @property
    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    @property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    @property
    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def __repr__(self):
        return "<User '{}'>".format(self.email)


class Profile(BaseModelMixin):
    """User Profile to store user extra details"""
    __tablename__ = 'user_profiles'
    address1 = db.Column(db.String(100), default="")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return "<Profile '{}'>".format(self.user.email)
