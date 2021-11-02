from flask_sqlalchemy import  SQLAlchemy

db = SQLAlchemy()

class Medico(db.model):
    __tablename__ =  "medicos"
    nome = db.Column(db.String(30), nullable=False)
    sobrenome = db.Column(db.String(30), nullable=False)
    idade = db.Column(db.Integer(), nullable=False)
    data_nasc = db.Column(db.DateTime(), nullable=False)
    endereço = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(30), nullable=False)

    def __init__(self, nome, sobrenome, idade, data_nasc, endereco, telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.data_nasc = data_nasc
        self.endereço = endereco
        self.telefone = telefone

    def __str__(self):
        return self.nome