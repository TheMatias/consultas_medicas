from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class Pessoa(db.Model):
    id = db.Column(db.Inteder(), primary_key = True)
    nome = db.Column(db.String(80), nullable=False )
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False, index=True)
    data_nasc = db.Column(db.DateTime)
    endereco = db.Column()


    def __init__(self, nome:str, email:str, cpf:str, data_nasc:datetime) -> None:
        super().__init__()
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.data_nasc = data_nasc

    def __str__(self):
        return self.id