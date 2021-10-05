
from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'flask'
app.config['MONGO_URI']='mongodb://localhost/consultas_medicas'
mongo = PyMongo(app)
Bootstrap(app)

# PAGINA DE LOGIN URL PADRÃO

@app.route('/', methods=['GET'])
def defaul():
    return redirect(url_for('login'),code=302)

@app.route('/login', methods=['GET'])
def main():
    return render_template("login/index.html")

# AUTENTITACAO DE LOGIN
@app.route('/autenticar', methods=['POST'])
def autenticar():
    
    email = request.form['email']
    senha = request.form['senha']

    if request.method == 'POST':
        if email =='admin' and senha =='admin':
            return redirect(url_for('dashboard'),code=302)
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


@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard/perfil.html')



@app.route('/criar_usuario', methods=['POST'])
def criar_usuario():
    nome = request.form['nome']
    email = request.form['email']
    cpf = request.form['cpf']
    data_nasc = request.form['data_nasc']
    usuario = request.form['usuario']
    senha = request.form['senha']
    senha2 = request.form['senha2']

    if request.method == 'POST':
        if nome and cpf and data_nasc and usuario and email and senha and senha == senha2:
            senha_hash = generate_password_hash(senha)

            id = mongo.db.usuarios.insert({
                'nome': nome,
                'email': email, 
                'cpf': cpf,
                'data_nasc': data_nasc,
                'usuario':usuario, 
                'status': 'USUARIO_ATIVO',
                'senha':senha_hash
                })
            # response = {
            #     'id': str(id),
            #     'nome': nome,
            #     'email': email, 
            #     'cpf': cpf,
            #     'data_nasc': data_nasc,
            #     'usuario':usuario, 
            #     'senha':senha_hash
            # }
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
                "login/index.html",
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