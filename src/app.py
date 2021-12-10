from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
from werkzeug.security import generate_password_hash, check_password_hash

from flask_migrate import Migrate
from models import db
app = Flask(__name__)
app.secret_key = 'flask'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:arduino@localhost:5432/consults'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
migrate = Migrate(app, db)

@app.route('/', methods=['GET'])
def default():
    return render_template("login/login.html")

# AUTENTITACAO DE LOGIN
@app.route('/autenticar', methods=['POST'])
def autenticar():
    
    email = request.form['email']
    senha = request.form['senha']
    senha_hash = generate_password_hash(senha)


    if request.method == 'POST':
        if "usuario":
            return redirect(url_for('principal'),code=302)
        else:
            if email:
                flash('Digite seu e-mail corretamente.')
            if senha:
                flash('Senha incorreta. Tente novamente ou clique em "Esqueceu a senha?" para redefini-la.')
            return redirect(url_for('login'),code=302)
    
    return redirect(url_for('login'),code=302)


@app.route('/cadastrar', methods=['GET'])
def cadastrarPaciente():
    return render_template('cadastro/cadastroPaciente.html')

@app.route('/principal', methods=['GET'])
def principal():
    return render_template('principal/perfil.html')

@app.route('/criar_usuario', methods=['POST'])  
def criar_usuario():
    nome = request.form['nome']
    cpf = request.form['cpf']
    email = request.form['email']
    data_nasc = request.form['data_nasc']
    usuario = request.form['usuario']
    senha = request.form['senha']
    senha2 = request.form['senha2']

    if request.method == 'POST':
        if nome and cpf and data_nasc and usuario and email and senha and senha == senha2:
            senha_hash = generate_password_hash(senha)

            return render_template(
                'dashboard/perfil.html',
                id = str(id),
                nome = nome,
                email = email,
                cpf = cpf,
                data_nasc = data_nasc,
                usuario = usuario,
                senha = senha
            )
        else:
            return render_template(
                "login/login.html",
                msg='create new user ... failed ...'
                )
    else:
        return

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('errors/error.html')


if __name__ == "__main__":
    app.run(debug=True)