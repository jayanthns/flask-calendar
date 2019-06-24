import datetime

from sqlalchemy.ext.declarative import declared_attr

from extensions import db


class BaseModelMixin(db.Model):
    """Base Model Class

    Arguments:
        db {sqlalchemy instance} -- [db.Model is the sqlalchemy's Model class]
    """
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    modified_on = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow(),
        onupdate=datetime.datetime.utcnow())

    def as_dict(self):
        return {row.name: getattr(self, row.name) for row in self.__table__.columns}

    def __repr__(self):
        return str(self.as_dict)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
