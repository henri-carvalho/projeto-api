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

def test_get_alunos(client):
    response = client.get('/alunos')
    assert response.status_code == 200

def test_create_aluno(client):
    response = client.post('/alunos',
                           data=json.dumps({
                               "nome": "Teste Aluno",
                               "idade": 21,
                               "turma": "3B",
                               "nascimento": "2003-04-15",
                               "nota_primeiro_semestre": 7.5,
                               "nota_segundo_semestre": 8.0,
                               "nota_final": 7.75
                           }),
                           content_type='application/json')
    assert response.status_code == 201

def test_update_aluno(client):
    response = client.post('/alunos',
                           data=json.dumps({
                               "nome": "Teste Aluno",
                               "idade": 21,
                               "turma": "3B",
                               "nascimento": "2003-04-15",
                               "nota_primeiro_semestre": 7.5,
                               "nota_segundo_semestre": 8.0,
                               "nota_final": 7.75
                           }),
                           content_type='application/json')
    assert response.status_code == 201
    
    aluno_id = response.get_json().get('id')  # Captura o ID do aluno criado
    print(f"Aluno criado com ID: {aluno_id}")

    response = client.put(f'/alunos/{aluno_id}',
                          data=json.dumps({
                              "nome": "Teste Aluno Atualizado",
                              "idade": 22,
                              "turma": "4A",
                              "nascimento": "2002-04-15",
                              "nota_primeiro_semestre": 8.5,
                              "nota_segundo_semestre": 9.0,
                              "nota_final": 8.75
                          }),
                          content_type='application/json')

    if response.status_code == 404:
        print(f"Aluno com ID {aluno_id} não encontrado para atualização")

    assert response.status_code == 200

def test_delete_aluno(client):
    response = client.post('/alunos',
                           data=json.dumps({
                               "nome": "Teste Aluno",
                               "idade": 21,
                               "turma": "3B",
                               "nascimento": "2003-04-15",
                               "nota_primeiro_semestre": 7.5,
                               "nota_segundo_semestre": 8.0,
                               "nota_final": 7.75
                           }),
                           content_type='application/json')
    assert response.status_code == 201
    
    aluno_id = response.get_json().get('id')  # Captura o ID do aluno criado
    print(f"Aluno criado com ID: {aluno_id}")

    response = client.delete(f'/alunos/{aluno_id}')
    
    if response.status_code == 404:
        print(f"Aluno com ID {aluno_id} não encontrado para deleção")

    assert response.status_code == 200
