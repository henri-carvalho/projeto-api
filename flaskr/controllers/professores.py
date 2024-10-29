import traceback
from flask import Blueprint, request, jsonify, render_template
from ..models.professor import Professores, adicionar_professor, atualizar_professor, excluir_professor, listar_professores, ProfessorNaoEncontrado, professor_por_id

professores_blueprint = Blueprint('professores', __name__)
@professores_blueprint.route('/professores', methods=['GET'])
def get_professores():
    try:
        professores = listar_professores()
        return render_template('professor/listar_professores.html', professores=professores)
    except Exception as e:
        print(traceback.format_exc())  # Imprime a stack trace do erro no console
        return jsonify({'erro': str(e)}), 500

@professores_blueprint.route('/professores/<int:id_professor>', methods=['GET'])
def get_professor(id_professor):
    try:
        professor = professor_por_id(id_professor)  # Função para buscar professor pelo ID
        return jsonify(professor), 200
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404


@professores_blueprint.route('/professores', methods=['POST'])
def create_professor():
    data = request.json
    if not data or 'nome' not in data or 'idade' not in data or 'materia' not in data:
        return jsonify({'erro': 'Dados inválidos ou incompletos'}), 400
    try:
        professor_id = adicionar_professor(data)
        return jsonify({'mensagem': 'Professor criado com sucesso!','id': professor_id}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@professores_blueprint.route('/professores/<int:professor_id>', methods=['PUT'])
def update_professor(professor_id):
    data = request.json
    try:
        atualizar_professor(professor_id, data)
        return jsonify({'mensagem': 'Professor atualizado com sucesso!'}), 200
    except ProfessorNaoEncontrado:
        return jsonify({'erro': 'Professor não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@professores_blueprint.route('/professores/<int:professor_id>', methods=['DELETE'])
def delete_professor(professor_id):
    try:
        excluir_professor(professor_id)
        return jsonify({'mensagem': 'Professor removido com sucesso!'}), 200
    except ProfessorNaoEncontrado:
        return jsonify({'erro': 'Professor não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 500