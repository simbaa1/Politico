
from flask import Flask, jsonify
from instance.config import app_config
from .v1.views import parties, offices
from .database.dbsetup import DatabaseConnection as db

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)  
    
    app.config.from_pyfile('config.py')
    app.config.from_object(app_config[config_name])

       
    app.register_blueprint(offices.bp)
    app.register_blueprint(parties.bp)
    # db.connection(config_name)
   
    
    return app