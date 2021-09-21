from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/consultas_medicas'
mongo = PyMongo(app)


@app.route('/', methods=['GET'])
def main():
    return render_template("index.html")


@app.route('/criar_usuario', methods=['POST'])
def criar_usuario():
    usuario = request.json['usuario']
    email = request.json['email']
    senha = request.json['senha']
    
    if usuario and email and senha:
        senha_hash = generate_password_hash(senha)
        id = mongo.db.usuarios.insert({
            'usuario':usuario, 
            'email':email, 
            'senha':senha_hash
            })
        response = {
            'id': str(id),
            'usuario':usuario, 
            'email':email, 
            'senha':senha
        }
        return response
    else:
        { 'message': 'create new user ... failed ...' }




if __name__ == "__main__":
    app.run(debug=True)