from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Endereco(db.Model):
    __tablename__ = "enderecos"
    id = db.Column(db.Integer(), primary_key = True)
    cep = db.Column(db.String(30), nullable = False)
    logradouro = db.Column(db.String(150), nullable = False)
    numero = db.Column(db.Integer(), nullable = False)

    def __init__(self, cep:str, logradouro:str, numero:int) -> None:
        super().__init__()
        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        
    def __str__(self) -> str:
        return dict(self.id, self.cep, self.logradouro, self.numero)