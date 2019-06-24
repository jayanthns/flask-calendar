from extensions import db
from database.db import BaseModelMixin


class Article(BaseModelMixin):
    """Article model to store article details"""

    __tablename__ = 'articles'

    name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return "<Article '{}'>".format(self.name)
