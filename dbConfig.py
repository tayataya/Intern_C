from flask_sqlalchemy import SQLAlchemy


class DbConfig:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
        'user': 'jseintern',
        'password': 'jseintern+',
        'host': 'localhost:3306',
        'db_name': 'jse_intern'
    })

    SQLALCHEMY_TRACK_MODIFICATIONS = False
