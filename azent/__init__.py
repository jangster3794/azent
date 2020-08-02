from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import atexit

from datetime import datetime

db = SQLAlchemy()

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    # app.config.from_object('config.Config')

    db.init_app(app)

    application = Flask(__name__)

    @atexit.register
    def shutdown():
        print('shutting down')

    with app.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create sql tables for our data models

        return app