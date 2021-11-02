from typing import Tuple
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from model.pessoa import Pessoa

db = SQLAlchemy()

class Paciente(db.Model):
    __tablename__ = "pacientes"
    id = db.Column(db.Integer(), primary_key = True)
    nome = db.Column(db.String(30), nullable=False)
    sobrenome = db.Column(db.String(30), nullable=False)
    idade = db.Column(db.Integer(), nullable=False)
    data_nasc = db.Column(db.DateTime(), nullable=False)
    endereço = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(30), nullable=False)


    def __init__(self, nome: str, email: str, cpf: str, data_nasc: datetime) -> None:
        super().__init__(nome, email, cpf, data_nasc)

    def __str__(self):
        return super().__str__()

