# Sistema Bancário

Este é um projeto de exemplo de uma API REST para simular operações bancárias como criação de clientes, contas, depósitos, saques e consulta de histórico.

## Estrutura do Projeto

```bash
.
│
├── app/
│   ├── __init__.py        # Configurações do Flask e inicialização
│   ├── __pycache__/       # Cache dos arquivos compilados
│   ├── app.db             # Banco de dados SQLite
│   ├── config.py          # Configurações da aplicação (chaves, banco de dados)
│   ├── database.py        # Inicialização do banco de dados (SQLAlchemy)
│   ├── models.py          # Modelos de Cliente, Conta, Histórico, Transação
│   └── routes.py          # Rotas da API
│
├── instance/              # Instância da aplicação
│
├── migrations/            # Arquivos de migração do banco de dados
│
├── requirements.txt       # Dependências do projeto
│
├── run.py                 # Arquivo principal para rodar a aplicação
│
└── venv/                  # Ambiente virtual

```

## Como executar o projeto

1. Clone o repositório e entre na pasta:

```bash
git clone https://github.com/seu-usuario/Sistema-Bancario-Python.git
cd Sistema-Bancario-Python
```

2. Crie e ative o ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate  # No Linux/Mac
# No Windows, use: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Rode o servidor Flask:

```bash
python run.py
```

5. A API estará disponível em http://127.0.0.1:5000.

## Endpoints da API

- **Clientes**
  - `POST /clientes`: Cria um novo cliente.
  - `GET /clientes`:  Obtém a lista de clientes.
  - `GET /clientes/{id}`: Obtém informações de um cliente específico.

- **Contas**
  - `POST /contas`: Cria uma nova conta para um cliente.

  - `POST /contas/{id}/depositar`: Realiza um depósito em uma conta.

  - `POST /contas/{id}/sacar`: Realiza um saque em uma conta.

  - `GET /contas/{id}/historico`: Obtém o histórico de transações de uma conta.

## Próximos Passos
- **Documentação**: Adicionar validações e autenticações nos endpoints, implementar testes automatizados, melhorar a documentação da API com Swagger e incluir exemplos de requisições e respostas.
- **Segurança**: Implementar medidas de segurança para proteger os dados sensíveis, como criptografia de senhas.