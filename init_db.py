from app import criar_app
from app.models.user import db, User, ModeloDocumento

def init_database():
    app = criar_app()
    
    with app.app_context():
        # Limpar dados existentes
        db.drop_all()
        db.create_all()

        # Criar usuário de teste
        usuario_teste = User(
            nome="Usuário Teste", 
            email="teste@exemplo.com", 
            cpf="123.456.789-00"
        )
        usuario_teste.set_senha("senha123")
        db.session.add(usuario_teste)

        # Criar modelos de documentos
        modelos = [
            ModeloDocumento(
                nome="Contrato de Prestação de Serviços",
                descricao="Modelo padrão para contratos de serviços",
                categoria="Serviços",
                conteudo_template="""
                CONTRATO DE PRESTAÇÃO DE SERVIÇOS

                CONTRATANTE: {{ nome_cliente }}
                CPF: {{ cpf }}
                
                CONTRATADO: [NOME DA EMPRESA]
                
                VALOR DO CONTRATO: R$ {{ valor_contrato }}
                
                Termos e condições do contrato...
                """
            ),
            ModeloDocumento(
                nome="Contrato de Aluguel",
                descricao="Modelo para contratos de locação",
                categoria="Imobiliário",
                conteudo_template="""
                CONTRATO DE LOCAÇÃO

                LOCATÁRIO: {{ nome_cliente }}
                CPF: {{ cpf }}
                
                LOCADOR: [NOME DO PROPRIETÁRIO]
                
                VALOR DO ALUGUEL: R$ {{ valor_aluguel }}
                
                Termos e condições do contrato de aluguel...
                """
            )
        ]

        # Adicionar modelos ao banco de dados
        for modelo in modelos:
            db.session.add(modelo)

        # Commit das alterações
        db.session.commit()

        print("Banco de dados inicializado com sucesso!")

if __name__ == '__main__':
    init_database()
