from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sialed'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ipdnwmwj:BKXx8NDp8mZ2J1sZmYi3vWJUknzBFnNN@trumpet.db.elephantsql.com/ipdnwmwj'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefixe="/")
    app.register_blueprint(auth, url_prefixe="/")

    from .models import User, Note

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()    
            print('Created Database!')






    


