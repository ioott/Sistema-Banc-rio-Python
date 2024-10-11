from flask import Flask
from .database import db
from .routes import main

def create_app():
    app = Flask(__name__)

    # Configurações
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar banco de dados
    db.init_app(app)

    # Registrar rotas
    app.register_blueprint(main)

    # Criar o banco de dados (primeira vez)
    with app.app_context():
        db.create_all()

    return app
