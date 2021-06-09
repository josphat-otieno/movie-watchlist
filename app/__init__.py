from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


bootstrap = Bootstrap()
db = SQLAlchemy()

login_manager=LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view ='auth.login'

def create_app(config_name):
    app=Flask(__name__)


    # creating the app configuration
    app.config.from_object(config_options[config_name])

    # initialising flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    
    # registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # registering auth blueprint 
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

     
    # stting configuratons
    from .request import configue_request
    configue_request(app)
  
    
    return  app


# iitialising application
# app=Flask(__name__, instance_relative_config=True)

# settting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

# initialising flask extension
# bootstrap=Bootstrap(app)

# from app import views
# from app import error
