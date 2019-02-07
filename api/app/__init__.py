import os
from flask import Flask
from .v1.views.views import bp_1


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(bp_1)
    
    
    return app