from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# modelo de paciente
class Paciente(db.Model):
    __tablename__ = "pacientes"
    id_paciente = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    data_nasc = db.Column(db.DateTime, nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    telefone = db.Column(db.String(30), nullable=False)

    def __init__(self, nome:str, data_nasc:datetime, cpf:str, telefone:str) -> None:
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf
        self.telefone = telefone

    def __str__(self) -> str:
        return self.nome

    
# modelo de medico
class Medico(db.model):
    __tablename__ =  "medicos"
    id_medico = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    data_nasc = db.Column(db.DateTime, nullable=False)
    crm = db.Column(db.String(30), nullable=False)
    telefone = db.Column(db.String(30), nullable=False)

    def __init__(self, nome:str, cpf:str, data_nasc:datetime, crm:str, telefone:str) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.data_nasc = data_nasc
        self.endereço = endereco
        self.telefone = telefone

    def __str__(self) -> str:
        return self.nome


# modelo de endereco
class Endereco(db.Model):
    __tablename__ = "enderecos"
    id_endereco = db.Column(db.Integer(), primary_key = True)
    cep = db.Column(db.String(30), nullable = False)
    estado = db.Column(db.String(40), nullable = False)
    cidade = db.Column(db.String(50), nullable = False)
    logradouro = db.Column(db.String(150), nullable = False)
    numero = db.Column(db.Integer, nullable = False)

    def __init__(self, cep:str, estado:str, cidade:str, logradouro:str, numero:int) -> None:
        self.cep = cep
        self.estado = estado
        self.cidade = cidade
        self.logradouro = logradouro
        self.numero = numero
        
    def __str__(self) -> str:
        return self.cep

    
# modelo de especialidade
class Especialidade(db.Model):
    __tablename__ = "especialidades"
    id_espec = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(150), nullable=False)

    def __init__(self, nome_espec:str, descricao:str) -> None:
        self.nome = nome_espec
        self.descricao = descricao

    def __str__(self) -> str:
        return self.nome


# modelo de consultas
class Consulta(db.model):
    __tablename__ = "consultas"
    id = db.Column(db.Integer(), primary_key = True)
    horario = db.Column(db.Time(), nullable=False)
    data = db.Column(db.Date(), nullable=False)
    
    def __init__(self, horario:datetime, data:datetime) -> None:
        self.horario = horario
        self.data = data

    def __str__(self) -> any:
        return self.horario