from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def db_init(app):
    app.config.from_object('dbConfig.DbConfig')
    db.init_app(app)
    with app.app_context():
        db.create_all()
