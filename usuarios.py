
class Usuarios:
    def __init__(self):
        self.usuarios = [
            {
                "id": 0,
                "tipo": 0,
                "user": "admin",
                "nombre": "admin",
                "apellido": "admin",
                "pass": "1234",
                "biblioteca":[]
            },
            {
                "id": 1,
                "tipo": 1,
                "user": "pamela",
                "nombre": "Pamela",
                "apellido": "Herrera",
                "pass": "0000",
                "biblioteca":[]
            },
            {
                "id": 2,
                "tipo": 1,
                "user": "andy",
                "nombre": "Andres",
                "apellido": "Carvajal",
                "pass": "4321",
                "biblioteca":[]
            }
        ]

    def comprobar(self, user, pswd):
        print(self.usuarios)
        for usuario in self.usuarios:
            if(usuario['user'] == user and usuario['pass'] == pswd):
                return {'user': usuario}
        return {'user': False}

    def registrar(self, user, tipo, pswd, nombre, apellido):
        for usuario in self.usuarios:
            if(usuario['user'] == user):
                return {'ok': False}

        self.usuarios.append({
            "id": len(self.usuarios),
            "tipo": tipo,
            "user": user,
            "nombre": nombre,
            "apellido": apellido,
            "pass": pswd,
            "biblioteca":[]
        })
        return {'ok': True}

    def recuperar(self, user):
        for usuario in self.usuarios:
            if(usuario['user'] == user):
                return {'ok': True, 'pass': usuario['pass']}
        return {'ok': False}

    def editar(self, id, user, pswd, nombre, apellido):
        for usuario in self.usuarios:
            if(usuario['id'] != id and usuario['user'] == user):
                return {'ok': False}

        usuario = self.usuarios[id]
        usuario["user"] = user
        usuario["pass"] = pswd
        usuario["nombre"] = nombre
        usuario["apellido"] = apellido

        print(str(self.usuarios[id]))

        return {"user": self.usuarios[id]}

    def agregar_v(self, id, juego):
        for usuario in self.usuarios:
            if(usuario['id'] == id):
                usuario["biblioteca"].append(juego)
                return {'ok': True}
        return {'ok': True}
