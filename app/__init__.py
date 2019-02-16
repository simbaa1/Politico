import os
import psycopg2
from flask import Flask
from instance.config import app_config
from .v1.views.views import bp_1
from .v1.views import parties, offices
from .database.dbsetup import DatabaseConnection as db

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(bp_1, url_prefix='/api/v1')
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    db.connection(config_name)
   
    
    return app