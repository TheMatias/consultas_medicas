from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from model.pessoa import Pessoa

db = SQLAlchemy()

class Paciente(db.Model, Pessoa):
    __tablename__ = "pacientes"
    
    def __init__(self, nome: str, email: str, cpf: str, data_nasc: datetime) -> None:
        super().__init__(nome, email, cpf, data_nasc)

    def __str__(self):
        return super().__str__()