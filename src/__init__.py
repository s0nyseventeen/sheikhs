import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_mapping({
            'UPLOAD_FOLDER': os.getenv('UPLOAD_FOLDER'),
            'SECRET_KEY': os.getenv('SECRET_KEY'),
            'SQLALCHEMY_DATABASE_URI': os.getenv('SQLALCHEMY_DATABASE_URI')
        })

    db.init_app(app)

    from .auth import bp
    app.register_blueprint(bp)

    from .gallery import bp
    app.register_blueprint(bp)

    return app
