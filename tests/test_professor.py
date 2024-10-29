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

def test_get_professores(client):
    response = client.get('/professores')
    assert response.status_code == 200

def test_create_professor(client):
    response = client.post('/professores',
                           data=json.dumps({
                               "nome": "Teste Professor",
                               "idade": 40,
                               "materia": "Matemática",
                               "observacoes": "Nenhuma"
                           }),
                           content_type='application/json')
    assert response.status_code == 201

def test_update_professor(client):
    response = client.post('/professores',
                           data=json.dumps({
                               "nome": "Teste Professor",
                               "idade": 40,
                               "materia": "Matemática",
                               "observacoes": "Nenhuma"
                           }),
                           content_type='application/json')
    assert response.status_code == 201

    professor_id = response.get_json().get('id')
    print(f"Professor criado com ID: {professor_id}")

    response = client.put(f'/professores/{professor_id}',
                          data=json.dumps({
                              "nome": "Teste Professor Atualizado",
                              "idade": 42,
                              "materia": "Física",
                              "observacoes": "Atualizado"
                          }),
                          content_type='application/json')
    
    if response.status_code == 404:
        print(f"Professor com ID {professor_id} não encontrado para atualização")

    assert response.status_code == 200

def test_delete_professor(client):
    response = client.post('/professores',
                           data=json.dumps({
                               "nome": "Teste Professor",
                               "idade": 40,
                               "materia": "Matemática",
                               "observacoes": "Nenhuma"
                           }),
                           content_type='application/json')
    assert response.status_code == 201

    professor_id = response.get_json().get('id')
    print(f"Professor criado com ID: {professor_id}")

    response = client.delete(f'/professores/{professor_id}')
    
    if response.status_code == 404:
        print(f"Professor com ID {professor_id} não encontrado para deleção")

    assert response.status_code == 200