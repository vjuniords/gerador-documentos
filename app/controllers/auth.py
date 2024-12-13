from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.user import User, db
from email_validator import validate_email, EmailNotValidError

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        cpf = request.form.get('cpf')

        # Validações
        try:
            valid = validate_email(email)
            email = valid.email
        except EmailNotValidError:
            flash('Email inválido', 'erro')
            return redirect(url_for('auth.cadastro'))

        if User.query.filter_by(email=email).first():
            flash('Email já cadastrado', 'erro')
            return redirect(url_for('auth.cadastro'))

        novo_usuario = User(nome=nome, email=email, cpf=cpf)
        novo_usuario.set_senha(senha)
        
        db.session.add(novo_usuario)
        db.session.commit()

        flash('Cadastro realizado com sucesso!', 'sucesso')
        return redirect(url_for('auth.login'))

    return render_template('auth/cadastro.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = User.query.filter_by(email=email).first()
        
        if usuario and usuario.check_senha(senha):
            login_user(usuario)
            flash('Login realizado com sucesso!', 'sucesso')
            return redirect(url_for('main.dashboard'))
        
        flash('Credenciais inválidas', 'erro')

    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout realizado com sucesso!', 'sucesso')
    return redirect(url_for('auth.login'))
