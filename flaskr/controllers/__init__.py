from flask import Blueprint
from .alunos import alunos_blueprint
from .professores import professores_blueprint
from .turmas import turmas_blueprint
from .default import default_blueprint

def register_blueprints(app):
    app.register_blueprint(alunos_blueprint)
    app.register_blueprint(professores_blueprint)
    app.register_blueprint(turmas_blueprint)
    app.register_blueprint(default_blueprint)
