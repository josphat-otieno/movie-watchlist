from logging import error
from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

# iitialising application
app=Flask(__name__, instance_relative_config=True)

# settting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# initialising flask extension
bootstrap=Bootstrap(app)

from app import views
from app import error
