from extensions import db
from database.db import BaseModelMixin


class CalendarYear(BaseModelMixin):
    """Calendaryear model to store year"""

    __tablename__ = "calendar_years"

    year = db.Column(db.Integer, unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=False, nullable=False)
    calendar_holidays = db.relationship(
        'CalendarHoliday', backref="calendar_year", uselist=True, lazy=True
    )

    def __repr__(self):
        return "<CalendarYear '{}'>".format(self.year)


class CalendarHoliday(BaseModelMixin):
    """Calendar Holiday List Data"""

    __tablename__ = "calendar_holidays"

    name = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    no_of_days = db.Column(db.Integer, nullable=False)
    year_id = db.Column(db.Integer, db.ForeignKey('calendar_years.id'), nullable=False)

    def __repr__(self):
        return "<CalendarHoliday '{0} - {1}'>".format(self.name, self.start_date)
