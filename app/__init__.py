from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from flask_jwt_extended import JWTManager 

db = SQLAlchemy() 
migrate = Migrate()
jwt = JWTManager()


def create_app(config_class="app.config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Register blueprints
    from app.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app