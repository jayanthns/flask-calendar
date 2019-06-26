import logging
import datetime
import calendar as f_calendar
import json

from flask import (
    Blueprint, render_template, request, Response
)
from flask_login import login_required

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

WEEK_DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTH_NAMES = (
    'January', 'February', 'March', 'April', 'May', 'June', 'July',
    'August', 'September', 'October', 'November', 'December'
)

calendar_blueprint = Blueprint(
    'calendar', __name__,
    template_folder='templates',
    # static_folder='static',
    # static_url_path='/static'
)


def get_days_dict(year, month):
    today = datetime.datetime.now()
    num_days = f_calendar.monthrange(year, month)[1]
    days = [datetime.date(year, month, day) for day in range(1, num_days + 1)]
    days_dict = [
        {
            day.day: f_calendar.day_name[day.weekday()],
            'disable': day.day < today.day or month < today.month
        }
        for day in days
    ]
    dict = {
        'days': days_dict,
        'year': year,
        'month': month,
        'today': today.day
    }
    return dict


def is_muted_month(c_year, c_month, p_year, p_month, c_day, p_day):
    if p_year < c_year:
        return True
    elif p_year == c_year:
        if p_month < c_month:
            return True
        elif p_month == c_month:
            if p_day < c_day:
                return True
            else:
                return False
    else:
        return False


def modified_get_days_dict(year, month):
    today = datetime.datetime.now()
    num_days = f_calendar.monthrange(year, month)[1]
    days = [datetime.date(year, month, day) for day in range(1, num_days + 1)]
    p_month = month - 1
    p_year = year
    if p_month == 0:
        p_month = 12
        p_year -= 1

    p_num_days = f_calendar.monthrange(p_year, p_month)[1]
    p_days = [datetime.date(p_year, p_month, p_day) for p_day in range(1, p_num_days + 1)]

    n_month = month + 1
    n_year = year
    if n_month > 12:
        n_month = 1
        n_year += 1

    n_num_days = f_calendar.monthrange(n_year, n_month)[1]
    n_days = [datetime.date(n_year, n_month, n_day) for n_day in range(1, n_num_days + 1)]

    days_dict = [
        {
            'styles': 'tdClass ' +
            ('today ' if (
                day.day == today.day and
                day.month == today.month and
                day.year == today.year
            ) else '') +
            ('oldMonth ' if is_muted_month(
                today.year, today.month, year, month, today.day, day.day
            ) else 'currentMonthDays '),

            'day': day.day,
            'week_day': f_calendar.day_name[day.weekday()],
            'extra': ''
            # 'current_month': day.month == today.month and day.year == today.year,
            # 'active': day.day == today.day and day.month == today.month and day.year == today.year,
        }
        for day in days
    ]
    first_day = days_dict[0]['week_day']
    starts_at = WEEK_DAYS.index(first_day)
    if starts_at > 0:
        p_days = p_days[-starts_at:]
    else:
        p_days = []
    p_days_dict = [
        {
            'styles': 'tdClass muted',
            'day': day.day,
            'week_day': f_calendar.day_name[day.weekday()],
            'extra': 'e',
            # 'current_month': False,
            # 'active': False,
        }
        for day in p_days
    ]
    days_dict = p_days_dict + days_dict

    remains = 0

    if not days_dict.__len__() % 7 == 0:
        remains = 7 - (days_dict.__len__() % 7)

    if remains > 0:
        n_days = n_days[:remains]
    else:
        n_days = []

    n_days_dict = [
        {
            'styles': 'tdClass muted',
            'day': day.day,
            'week_day': f_calendar.day_name[day.weekday()],
            'extra': 'e',
            # 'current_month': False,
            # 'active': False,
        }
        for day in n_days
    ]
    days_dict += n_days_dict

    dict = {
        'days': days_dict,
        'year': year,
        'month': month,
        'month_name': MONTH_NAMES[month - 1],
        'today': str(today.day) + '/' + str(today.month) + '/' + str(today.year)
    }
    return dict


@calendar_blueprint.route('/', strict_slashes=False)
@login_required
def calendar():
    data = {
        'nbar': 'calendar'
    }
    return render_template("calendar/calendar.html", data=data)


@calendar_blueprint.route(
    '/get_calender_days', strict_slashes=False
)
def get_calender_days():
    if request.method == 'GET':
        year, month = int(request.args['year']), int(request.args['month'])
        return Response(
            json.dumps(modified_get_days_dict(year, month)),
            content_type='application/javascript; charset=utf8'
        )
