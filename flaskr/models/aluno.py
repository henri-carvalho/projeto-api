from ..config import db
from datetime import datetime


class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    turma = db.Column(db.String(50))
    nascimento = db.Column(db.Date)
    nota_primeiro_semestre = db.Column(db.Float)
    nota_segundo_semestre = db.Column(db.Float)
    nota_final = db.Column(db.Float)

    def __init__(self, nome, idade, turma, nascimento, nota_primeiro_semestre, nota_segundo_semestre, nota_final):
        self.nome = nome
        self.idade = idade
        self.turma = turma
        self.nascimento = nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.nota_final = nota_final

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'turma': self.turma,
            'nascimento': self.nascimento.isoformat() if self.nascimento else None,
            'nota_primeiro_semestre': str(self.nota_primeiro_semestre),
            'nota_segundo_semestre': str(self.nota_segundo_semestre),
            'nota_final': str(self.nota_final)
        }

class AlunoNaoEncontrado(Exception):
    pass

def aluno_por_id(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if aluno is None:
        raise AlunoNaoEncontrado(f'Aluno com ID {id_aluno} não encontrado.')
    return aluno.to_dict()

def listar_alunos():
    alunos = Aluno.query.all()
    return [aluno.to_dict() for aluno in alunos]

def adicionar_aluno(aluno_data):
    novo_aluno = Aluno(
        nome=aluno_data['nome'],
        idade=aluno_data['idade'],
        turma=aluno_data['turma'],
        nascimento=datetime.strptime(aluno_data['nascimento'], '%Y-%m-%d').date(),
        nota_primeiro_semestre=aluno_data['nota_primeiro_semestre'],
        nota_segundo_semestre=aluno_data['nota_segundo_semestre'],
        nota_final=aluno_data['nota_final']
    )
    db.session.add(novo_aluno)
    db.session.commit()
    db.session.commit()
    return novo_aluno.id

def atualizar_aluno(id_aluno, novos_dados):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    aluno.nome = novos_dados['nome']
    aluno.idade = novos_dados['idade']
    aluno.turma = novos_dados['turma']
    aluno.nascimento = datetime.strptime(novos_dados['nascimento'], '%Y-%m-%d').date()
    aluno.nota_primeiro_semestre = novos_dados['nota_primeiro_semestre']
    aluno.nota_segundo_semestre = novos_dados['nota_segundo_semestre']
    aluno.nota_final = novos_dados['nota_final']
    db.session.commit()

def excluir_aluno(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    db.session.delete(aluno)
    db.session.commit()