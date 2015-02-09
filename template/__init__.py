from flask import Flask
from template.views import views
from template.models import bcrypt
from template.auth import auth, login_manager

def create_app():
    app = Flask(__name__)
    config = '{0}.app_config'.format(__name__)
    app.config.from_object(config)
    app.register_blueprint(views)
    app.register_blueprint(auth)

    login_manager.init_app(app)
    bcrypt.init_app(app)
    
    return app
