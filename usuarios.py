class Usuarios:  #nombre de la clase

	def __init__(self):     #declaramos la funcion para el usuario adminitrador
		self.usuarios = [  #arreglo para los usuarios admin

			{
				"user":"admin",     #se creo el diccionario, osea los valores de administrador 
				"pass": "1234",
				"nombre":"admin",
				"apellido":"admin",
				"tipo": 0,
				"id":0
			},
			{
				"tipo": 1,
				"user":"Pamela",
				"nombre":"Pamela",
				"apellido":"Herrera",
				"pass": "0000",
				"id":1
			}
		]


	def comprobar (self, user, pswd):   #funcion comprobar, para verificar si esta correcta la info del usuario (credenciales)
		
		print(self.usuarios)
		for usuario in self.usuarios:
			if(usuario['user'] == user and usuario['pass'] == pswd): #verificacion de informacion
				return {'user':user}
		return {'user':False}


	def registrar (self, user, pswd, nombre, apellido):
		for usuario in self.usuarios:
			if (usuario ['user'] == user):
				return {'ok': False}

		self.usuarios.append({
			"id": len(self.usuarios),
			"user":user,
			"pass":pswd,
			"nombre":nombre,
			"apellido":apellido,
			"tipo":1,
			

		})
		return{'ok':True}


	def recuperar (self, user):
		for usuario in self.usuarios:
			if (usuario ['user'] == user):
				return {'ok': True, 'pass': usuario['pass']}
		return {'ok': False}


	def editar (self, id, user, pswd, nombre, apellido):
		for usuario in self.usuarios:
			if (usuario ['id'] !=id and usuario ['user'] == user):      #comprueba que los usuarios no se repitan, condicion
				return {'ok': False}

		usuario = self.usuarios[id]
		usuario["user"]=user
		usuario["pass"]=pswd
		usuario["nombre"]=nombre
		usuario["apellido"] = apellido
		
		print(str(self.usuarios[id]))
		return {"user": self.usuarios[id]}













