from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os 

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET')

db = SQLAlchemy(app)

from application import routes