# Sistema de Geração de Documentos

## Requisitos
- Python 3.8+
- pip
- Microsoft Word (para conversão de documentos)

## Instalação

1. Crie um ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate  # No Windows
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Inicialize o banco de dados:
```bash
python init_db.py
```

## Executando o Sistema

1. Inicie o servidor:
```bash
python run.py
```

2. Acesse no navegador:
- URL: `http://localhost:5000/auth/login`

## Credenciais de Teste
- Email: `teste@exemplo.com`
- Senha: `senha123`

## Funcionalidades
- Cadastro de usuários
- Geração de documentos
- Múltiplos modelos
- Download em DOCX e PDF

## Problemas Conhecidos
- Requer Microsoft Word para conversão de documentos
- Versão inicial, alguns recursos ainda em desenvolvimento
