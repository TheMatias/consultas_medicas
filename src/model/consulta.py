from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Consulta(db.model):
    __tablename__ = "consultas"
    id = db.Column(db.Integer(), primary_key = True)
    horario = db.Column(db.Time(), nullable=False)
    data = db.Column(db.Date(), nullable=False)

    