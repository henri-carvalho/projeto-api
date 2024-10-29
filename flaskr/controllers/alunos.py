from flask import Blueprint, request, jsonify, render_template
from ..models.aluno import listar_alunos, adicionar_aluno, atualizar_aluno, excluir_aluno, AlunoNaoEncontrado, aluno_por_id

alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    alunos = listar_alunos()
    return render_template("alunos/listar_alunos.html", alunos=alunos)

@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['GET'])
def get_aluno(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno)
        return jsonify(aluno), 200
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404

@alunos_blueprint.route('/alunos', methods=['POST'])
def create_aluno():
    data = request.json
    try:
        aluno_id = adicionar_aluno(data)
        return jsonify({'message': 'Aluno criado com sucesso!', 'id': aluno_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@alunos_blueprint.route('/alunos/<int:aluno_id>', methods=['PUT'])
def update_aluno(aluno_id):
    data = request.json
    try:
        atualizar_aluno(aluno_id, data)
        return jsonify({'message': 'Aluno atualizado com sucesso!'}), 200
    except AlunoNaoEncontrado:
        return jsonify({'error': 'Aluno não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@alunos_blueprint.route('/alunos/<int:aluno_id>', methods=['DELETE'])
def delete_aluno(aluno_id):
    try:
        excluir_aluno(aluno_id)
        return jsonify({'message': 'Aluno excluído com sucesso!'}), 200
    except AlunoNaoEncontrado:
        return jsonify({'error': 'Aluno não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400
