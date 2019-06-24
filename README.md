# `flask` `mysql` `blueprints` `marshmallow` `sqlalchemy` `flask-jwt-extended` `flask-login` `WTForms` `custom-calender` `session-management` `JavaScript` `AJAX` `JQuery`.

#### Scaffold of `Flask` `Mysql` `Blueprints` `Marshmallow` `SQLAlchemy` `flask cli` `flask-jwt-extended` `flask-login` `WTForms` `custom-calender` `session-management` `JavaScript` `AJAX` `JQuery`

## Requirements
### Recommended editor:
Download from this link ---> [Visual Studio Code](https://code.visualstudio.com/Download)
### Reference Link
Flask link ---> [Flask](http://flask.pocoo.org/)
Marshmallow link ---> [Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
SQLAlchemy link ---> [SQLAlchemy](https://www.sqlalchemy.org/)
Flask SQLAlchemy link ---> [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
flask-jwt-extended link ---> [flask-jwt-extended](https://flask-jwt-extended.readthedocs.io/en/latest/index.html)
Flask Login ---> [Flask Login](https://flask-login.readthedocs.io/en/latest/)

### Prerequisite knowledge:
`VS Code` `Python` `Flask` `Rest API` `MySQL` `marshmallow` `SQLAlchemy` `flask-jwt-extended`

### System requirements:
* `Python 3.6+`
* `mysql`

## Getting started

#### Create virtual environment
`python3 -m venv env`

#### Activate the environment
`source env/bin/activate`


```cd <project_root>```

##### Create `.env` file
###### ***`Copy env variables from .sample.env file and insert in the .env file.`

##### For Dubug mode
`export FLASK_DEBUG=1 # (0: off, 1: on)`

##### Creation of migrations folder
`flask db init`

#### For migrations
`flask db migrate`

#### Applying the migrations
`flask db upgrade`

#### Running the project
`flask run`
or
`gunicorn --bind 0.0.0.0 wsgi:app --log-level DEBUG --reload`

-----Project setup completed-----
