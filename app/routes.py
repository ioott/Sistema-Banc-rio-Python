from flask import Blueprint, request, jsonify
from .models import Cliente, Conta, Deposito, Saque
from .database import db

main = Blueprint('main', __name__)

@main.route('/clientes', methods=['POST'])
def criar_cliente():
    data = request.json
    novo_cliente = Cliente(nome=data['nome'], cpf=data['cpf'], data_nascimento=data['data_nascimento'], endereco=data['endereco'])
    db.session.add(novo_cliente)
    db.session.commit()
    return jsonify({'mensagem': 'Cliente criado com sucesso!'}), 201

@main.route('/contas', methods=['POST'])
def criar_conta():
    data = request.json
    cliente = Cliente.query.get(data['cliente_id'])
    if cliente:
        nova_conta = Conta(agencia=data['agencia'], numero=data['numero'], cliente_id=cliente.id)
        db.session.add(nova_conta)
        db.session.commit()
        return jsonify({'mensagem': 'Conta criada com sucesso!'}), 201
    return jsonify({'erro': 'Cliente não encontrado!'}), 404

@main.route('/contas/<int:conta_id>/depositar', methods=['POST'])
def depositar(conta_id):
    conta = Conta.query.get(conta_id)
    if conta:
        valor = request.json['valor']
        deposito = Deposito()
        deposito.registrar(conta, valor)
        return jsonify({'mensagem': 'Depósito realizado com sucesso!'}), 200
    return jsonify({'erro': 'Conta não encontrada!'}), 404

@main.route('/contas/<int:conta_id>/sacar', methods=['POST'])
def sacar(conta_id):
    conta = Conta.query.get(conta_id)
    if conta:
        valor = request.json['valor']
        saque = Saque()
        saque.registrar(conta, valor)
        return jsonify({'mensagem': 'Saque realizado com sucesso!'}), 200
    return jsonify({'erro': 'Conta não encontrada!'}), 404

@main.route('/contas/<int:conta_id>/historico', methods=['GET'])
def historico(conta_id):
    conta = Conta.query.get(conta_id)
    if conta:
        transacoes = [{"tipo": h.tipo, "valor": h.valor, "data": h.data} for h in conta.historico]
        return jsonify(transacoes), 200
    return jsonify({'erro': 'Conta não encontrada!'}), 404
