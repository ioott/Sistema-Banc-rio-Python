from .database import db
from datetime import datetime

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=False)
    endereco = db.Column(db.String(200))

    contas = db.relationship('Conta', backref='cliente', lazy=True)

class Conta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    saldo = db.Column(db.Float, default=0.0)
    agencia = db.Column(db.String(10), nullable=False)
    numero = db.Column(db.String(10), unique=True, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)

    historico = db.relationship('Historico', backref='conta', lazy=True)

class Historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, default=datetime.now)
    conta_id = db.Column(db.Integer, db.ForeignKey('conta.id'), nullable=False)

class Transacao:
    def registrar(self, conta, valor):
        pass

class Saque(Transacao):
    def registrar(self, conta, valor):
        if conta.saldo >= valor:
            conta.saldo -= valor
            transacao = Historico(tipo='Saque', valor=valor, conta_id=conta.id)
            db.session.add(transacao)
            db.session.commit()

class Deposito(Transacao):
    def registrar(self, conta, valor):
        conta.saldo += valor
        transacao = Historico(tipo='Deposito', valor=valor, conta_id=conta.id)
        db.session.add(transacao)
        db.session.commit()
