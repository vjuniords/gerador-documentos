from flask import Blueprint, render_template, request, jsonify, send_file
from flask_login import login_required, current_user
from app.models.user import Documento, ModeloDocumento, db
from app.services.document_generator import DocumentGenerator
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/dashboard')
@login_required
def dashboard():
    documentos = Documento.query.filter_by(usuario_id=current_user.id).all()
    modelos = ModeloDocumento.query.all()
    return render_template('main/dashboard.html', documentos=documentos, modelos=modelos)

@main_bp.route('/novo_documento')
@login_required
def novo_documento():
    modelos = ModeloDocumento.query.all()
    return render_template('main/novo_documento.html', modelos=modelos)

@main_bp.route('/listar_documentos')
@login_required
def listar_documentos():
    documentos = Documento.query.filter_by(usuario_id=current_user.id).order_by(Documento.data_criacao.desc()).all()
    return render_template('main/listar_documentos.html', documentos=documentos)

@main_bp.route('/criar_documento', methods=['POST'])
@login_required
def criar_documento():
    dados = request.json
    modelo_id = dados.get('modelo_id')
    dados_documento = dados.get('dados', {})

    modelo = ModeloDocumento.query.get(modelo_id)
    if not modelo:
        return jsonify({"erro": "Modelo não encontrado"}), 404

    try:
        gerador = DocumentGenerator()
        caminho_arquivo = gerador.gerar_documento(
            template=modelo.conteudo_template,
            dados=dados_documento
        )

        novo_documento = Documento(
            titulo=dados.get('titulo', 'Documento Sem Título'),
            tipo=modelo.categoria,
            conteudo=str(dados_documento),
            caminho_arquivo=caminho_arquivo,
            usuario_id=current_user.id
        )

        db.session.add(novo_documento)
        db.session.commit()

        return jsonify({
            "mensagem": "Documento criado com sucesso!",
            "documento_id": novo_documento.id
        }), 200

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@main_bp.route('/download_documento/<int:documento_id>')
@login_required
def download_documento(documento_id):
    documento = Documento.query.get_or_404(documento_id)
    
    # Verificar se o documento pertence ao usuário atual
    if documento.usuario_id != current_user.id:
        return jsonify({"erro": "Acesso não autorizado"}), 403

    try:
        return send_file(documento.caminho_arquivo, as_attachment=True)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
