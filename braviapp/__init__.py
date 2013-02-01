# third party imports
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# Initialize the app from Flask
braviapp = Flask(__name__)
braviapp.config.from_object('settings')

db = SQLAlchemy(braviapp)

# local application imports
from braviapp import views
