import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'sawanjrkey'

# Connect to PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sawanjr:92JqSPWpltMn2ztLPPa0l35zN9Pe7LXB@dpg-csv51om8ii6s73eo76t0-a/blog_db_y73r'

# Disable track modifications warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Mail server configuration
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
mail = Mail(app)

# Import routes
from flaskblog import routes