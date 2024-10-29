from flask import Blueprint, request, jsonify, render_template
from ..models.turma import Turma, adicionar_turma, listar_turmas, atualizar_turma, excluir_turma, TurmaNaoEncontrada, turma_por_id

turmas_blueprint = Blueprint('turmas', __name__)

@turmas_blueprint.route('/turmas', methods=['GET'])
def get_turmas():
    try:
        turmas = listar_turmas()
        return render_template('turma/listar_turmas.html', turmas=turmas)
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@turmas_blueprint.route('/turmas/<int:id_turma>', methods=['GET'])
def get_turma(id_turma):
    try:
        turma = turma_por_id(id_turma)  # Função para buscar turma pelo ID
        return jsonify(turma), 200
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não encontrada'}), 404
    
@turmas_blueprint.route('/turmas', methods=['POST'])
def create_turma():
    data = request.json
    if not data or 'descricao' not in data or 'professor' not in data or 'ativo' not in data:
        return jsonify({'erro': 'Dados inválidos ou incompletos'}), 400

    try:
        id_turma = adicionar_turma(data)
        return jsonify({'mensagem': 'Turma criada com sucesso!','id': id_turma}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@turmas_blueprint.route('/turmas/<int:turma_id>', methods=['PUT'])
def update_turma(turma_id):
    data = request.json
    try:
        atualizar_turma(turma_id, data)
        return jsonify({'mensagem': 'Turma atualizada com sucesso!'}), 200
    except TurmaNaoEncontrada:
        return jsonify({'erro': 'Turma não encontrada'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@turmas_blueprint.route('/turmas/<int:turma_id>', methods=['DELETE'])
def delete_turma(turma_id):
    try:
        excluir_turma(turma_id)
        return jsonify({'mensagem': 'Turma removida com sucesso!'}), 200
    except TurmaNaoEncontrada:
        return jsonify({'erro': 'Turma não encontrada'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 500
