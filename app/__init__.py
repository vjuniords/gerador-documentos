from flask import Flask, render_template
from flask_login import LoginManager
from flask_cors import CORS
from app.models.user import db, User
from app.controllers.auth import auth_bp
from app.controllers.main import main_bp
import os

def criar_app():
    app = Flask(__name__)
    
    # Configurações
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///documentos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializar extensões
    db.init_app(app)
    CORS(app)
    
    # Login Manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Registrar blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)
    
    # Adicionar rota inicial
    @app.route('/')
    def index():
        return render_template('index.html')
    
    # Criar banco de dados
    with app.app_context():
        db.create_all()
    
    return app
