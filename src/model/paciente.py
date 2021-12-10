from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Paciente(db.Model):
    __tablename__ = "pacientes"
    id_paciente = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    data_nasc = db.Column(db.DateTime, nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    telefone = db.Column(db.String(30), nullable=False)

    def __init__(self, nome: str, email: str, cpf: str, data_nasc: datetime) -> None:
        super().__init__(nome, email, cpf, data_nasc)

    def __str__(self):
        return self.nome

