from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(14), unique=True)
    tipo_usuario = db.Column(db.String(20), default='padrao')
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    documentos = db.relationship('Documento', backref='autor', lazy=True)

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def check_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

class Documento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    conteudo = db.Column(db.Text)
    caminho_arquivo = db.Column(db.String(300))
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class ModeloDocumento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    categoria = db.Column(db.String(50))
    conteudo_template = db.Column(db.Text, nullable=False)
    tags = db.Column(db.String(200))
