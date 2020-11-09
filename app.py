from flask import Flask, request
from usuarios import Usuarios
from flask_cors import CORS
from juegos import Juegos
import random


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin":"*"}})
usuarios = Usuarios()
juegos = Juegos()

@app.route('/', methods=['GET'])
def check():
    return "Todo_good!"

@app.route('/login', methods=['GET'])
def login():
    user = request.args.get('user')
    pswd = request.args.get('pswd')
    return usuarios.comprobar(user, pswd)

@app.route('/registro', methods=['POST'])
def registro():
    content = request.get_json()
    return usuarios.registrar(content['user'], content['tipo'], content['pswd'], content['nombre'], content['apellido'])

@app.route('/recuperar', methods=['GET'])
def recuperar():
    user = request.args.get('user')
    return usuarios.recuperar(user)

@app.route('/usuario/editar', methods=['POST'])
def usuario_editar():
    content = request.get_json()
    return usuarios.editar(content['id'], content['user'], content['pswd'], content['nombre'], content['apellido'])

@app.route('/usuario/add', methods=['POST'])
def usuario_add():
    content = request.get_json()
    return usuarios.agregar_v(content['id'], content['juego'])

@app.route('/juego', methods=['GET'])
def juego():
    return juegos.get_all()

@app.route('/juego/get', methods=['GET'])
def juego_get():
    id = request.args.get('id')
    return juegos.get_v(id)    

@app.route('/juego/new', methods=['POST'])
def juego_new():
    content = request.get_json()
    data = content['data']
    obj = {
        "id": random.randint(1, 999999),
        "nombre": data['name'],
        "año": data['price'],
        "categoria": [data['cat1'], data['cat2'], data['cat3']],
        "foto": data['photo'],
        "banner": data['banner'],
        "descripcion": data['desc']
    }
    return juego.insert_v(obj)

@app.route('/juego/edit', methods=['POST'])
def juego_edit():
    content = request.get_json()
    data = content['data']
    obj = {
        "id": data['id'],
        "nombre": data['name'],
        "año": data['price'],
        "categoria": [data['cat1'], data['cat2'], data['cat3']],
        "foto": data['photo'],
        "banner": data['banner'],
        "descripcion": data['desc']
    }
    return juegos.edit_v(obj)

@app.route('/juego/del', methods=['POST'])
def juego_del():
    id = request.args.get('id')
    return juegos.del_v(id)
        

@app.route('/carga', methods=['POST'])
def carga():
    content = request.get_json()
    return juegos.carga(content['data'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)

"""
login
registro #diferente user #nombre y apellido
recuperar contraseña
catalogo videojuegos 
"""
# pip install Flask-Cors