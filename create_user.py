"""Create a new admin user able to view the /reports endpoint."""
from getpass import getpass
import sys

from flask import current_app
from manage import app
from extensions import bcrypt, db

from models.user import User


def main():
    """Main entry point for script."""
    with app.app_context():
        db.metadata.create_all(db.engine)
        if User.query.all():
            print('A user already exists! Create another? (y/n):'),
            create = input()
            if create == 'n':
                return
        print('Enter email address: '),
        email = input()
        password = getpass()
        assert password == getpass('Password (again):')

        user = User(email=email)
        user.password = password
        user.is_superuser = True
        user.save()
        print('User added.')


if __name__ == '__main__':
    sys.exit(main())
