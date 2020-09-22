import os
from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '2930f806e23feba59318772e021d046a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


mail = Mail(app)

from Oh.Users.routes import users
from Oh.Posts.routes import posts
from Oh.Main.routes import main


app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)