from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Especialidade(db.Model):
    __tablename__ = "especialidades"
    id_espec = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(150), nullable=False)
    

    def __str__(self) -> str:
        return self.nome