from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from .views import views
from .database import db

def create_app():
    app = Flask(__name__)
    config = '{0}.app_config'.format(__name__)
    app.config.from_object(config)
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DB_CONN'] 
    
    db.init_app(app)

    app.register_blueprint(views)
    
    return app
