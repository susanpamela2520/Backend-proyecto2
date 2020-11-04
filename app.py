from flask import Flask, request
from usuarios import Usuarios
from flask_cors import CORS
from juegos1 import Juegos

app = Flask (__name__)
cors = CORS(app, resourses={r"/*":{"origin":"*"}})
usuarios = Usuarios()
juegos = Juegos()

@app.route("/" , methods = ['GET'])
def inicio():
	return "Todo Good!"

@app.route("/login" , methods = ['GET'])
def login():
	user = request.args.get('user')
	pswd = request.args.get('pswd')
	return usuarios.comprobar(user, pswd)

@app.route("/registro" , methods = ['POST'])
def registro():
	content = request.get_json()
	return usuarios.registrar(content['user'], content['pswd'], content['nombre'], content['apellido'])

@app.route("/recuperacion" , methods = ['GET'])
def recuperar():
	user = request.args.get('user')
	return usuarios.recuperar(user)

@app.route("/usuario/editar" , methods = ['POST'])
def usuario_editar():
	content = request.get_json()
	return usuarios.editar(content['id'], content['user'], content['pswd'], content['nombre'], content['apellido'])


########################################################################################################################
#carga masiva#

@app.route("/juego" , methods = ['GET'])
def juego():
	return juegos.get_all()


@app.route("/carga" , methods = ['POST'])
def carga():
	content = request.get_json()
	return juegos.carga(content['data'])




if __name__ == "__main__":
	app.run(host= '0.0.0.0', threaded = True, port=5001, debug=True, use_reloader=True)

