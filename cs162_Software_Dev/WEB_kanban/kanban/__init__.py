from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# init the app and set config
app = Flask(__name__) # create the application instance :)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kanban.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
# app.config.from_envvar('YOURAPPLICATION_SETTINGS')

# init encryption 
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)


# init flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#init db
def run_db_init():
	from .kanban_db_init import init_db
	init_db()

run_db_init()
