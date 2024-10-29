import json
import pytest
import sys
import os

# Insere o caminho do diretório do app no sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'flaskr')))

from flaskr import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_turmas(client):
    response = client.get('/turmas')
    assert response.status_code == 200

def test_create_turma(client):
    response = client.post('/turmas',
                           data=json.dumps({
                               "descricao": "Turma de Teste",
                               "professor": "Professor Teste",
                               "ativo": True
                           }),
                           content_type='application/json')
    assert response.status_code == 201, f"Erro: {response.get_json().get('erro')}"

def test_update_turma(client):
    response = client.post('/turmas',
                           data=json.dumps({
                               "descricao": "Turma de Teste",
                               "professor": "Professor Teste",
                               "ativo": True
                           }),
                           content_type='application/json')
    assert response.status_code == 201, f"Erro: {response.get_json().get('erro')}"

    turma_id = response.get_json().get('id')
    print(f"Turma criada com ID: {turma_id}")

    response = client.put(f'/turmas/{turma_id}',
                          data=json.dumps({
                              "descricao": "Turma Atualizada",
                              "professor": "Professor Atualizado",
                              "ativo": False
                          }),
                          content_type='application/json')

    if response.status_code == 404:
        print(f"Turma com ID {turma_id} não encontrada para atualização")

    assert response.status_code == 200, f"Erro: {response.get_json().get('erro')}"

def test_delete_turma(client):
    response = client.post('/turmas',
                           data=json.dumps({
                               "descricao": "Turma de Teste",
                               "professor": "Professor Teste",
                               "ativo": True
                           }),
                           content_type='application/json')
    assert response.status_code == 201, f"Erro: {response.get_json().get('erro')}"

    turma_id = response.get_json().get('id')
    print(f"Turma criada com ID: {turma_id}")

    response = client.delete(f'/turmas/{turma_id}')

    if response.status_code == 404:
        print(f"Turma com ID {turma_id} não encontrada para deleção")

    assert response.status_code == 200, f"Erro: {response.get_json().get('erro')}"
