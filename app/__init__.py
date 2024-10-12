from flask import Flask
from flask_migrate import Migrate
from .database import db
from .routes import main
from .config import Config

def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)
    db.init_app(app)

    migrate = Migrate(app, db)

    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app
