from flask_sqlalchemy import  SQLAlchemy

db = SQLAlchemy()

class Medico(db.model):
    __tablename__ =  "medicos"
    id_medico = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    data_nasc = db.Column(db.DateTime, nullable=False)
    crm = db.Column(db.String(30), nullable=False)
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