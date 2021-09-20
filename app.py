# from paciente import Paciente
from flask import Flask, request, template_rendered

# export FLASK_APP=app
# export FLASK_ENV=development
app = Flask(__name__)

notas = [
    {
        "title": "Nota de Aula",
        "conteudo": "Introdução ao Flask",
        "data_criacao": "2021-09-13",
        "data_alteracao": "2021-09-13",
        "status": "ativa"
    },
    {
        "title": "Nota de Aula 2",
        "conteudo": "Introdução ao Flask 2",
        "data_criacao": "2021-09-13",
        "data_alteracao": "2021-09-13",
        "status": "ativa"
    },
    {
        "title": "Nota de Aula 3",
        "conteudo": "Introdução ao Flask 3",
        "data_criacao": "2021-09-13",
        "data_alteracao": "2021-09-13",
        "status": "ativa"
    }]
    
@app.route("/")
def hello_world():
    return "<h1>hello flask</h1>"

@app.route("/usuarios")
def notas():
    return notas
    

@app.route("/perfil")
def perfil():
    return template_rendered(
        "perfil.html",
        # name: "Matias"
    )