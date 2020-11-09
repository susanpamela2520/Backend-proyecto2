
class Juegos:
    def __init__(self):
        self.juegos = [
            {
                "id": 0,
                "nombre": "juego",
                "año": 1999,
                "precio": 10.01,
                "categoria": ["cat"],
                "foto":"foto.jpg",
                "banner":"banner.jpg",
                "descripcion":"esta es una descripcion chida"
            }
        ]

    def carga(self, string: str):
        try:
            i = 0
            for linea in string.split('\n'):
                i += 1
                if i == 1:
                    continue
                obj = {
                    "id": None,
                    "nombre": None,
                    "año": None,
                    "precio": None,
                    "categoria": [],
                    "foto": None,
                    "banner": None,
                    "descripcion": None
                }
                data = linea.split(',')

                obj['id'] = int(data[0])
                obj['nombre'] = data[1]
                obj['año'] = int(data[2])
                obj['precio'] = float(data[3])

                if(data[4] != ''):
                    obj['categoria'].append(data[4])
                if(data[5] != ''):
                    obj['categoria'].append(data[5])
                if(data[6] != ''):
                    obj['categoria'].append(data[6])

                obj['foto'] = data[-3]
                obj['banner'] = data[-2]
                obj['descripcion'] = data[-1]

                self.juegos.append(obj)

            return {"ok": True}
        except:
            return {"ok": False}

    def get_all(self):
        return {"juegos": self.juegos}

    def insert_v(self, obj):
        self.juegos.append(obj)
        return{'ok', True}

    def edit_v(self, obj):
        for juego in self.juegos:
            if(juego['id'] == obj['id']):
                juego['nombre'] = obj['nombre']
                juego['año'] = obj['año']
                juego['precio'] = obj['precio']
                juego['foto'] = obj['foto']
                juego['banner'] = obj['banner']
                juego['descripcion'] = obj['descripcion']
                return {'ok': True}
        return {'ok': False}
    def del_v(self, id):
        for juego in self.juegos:
            if(juego['id'] == id):
                self.juegos.remove(juego)
                return {'ok': True}
        return {'ok': False}

    def get_v(self, id):
        for juego in self.juegos:
            if(juego['id'] == id):
                return {'ok':True, 'juego': juego}
        return {'ok':False}

"""
1,juego1,2000,5.99,cat1,,cat2,foto2.jpg,banner2.png,esta es otra descripcion
2,juego2,2000,5.99,cat1,,cat2,foto2.jpg,banner2.png,esta es otra descripcion
3,juego3,2000,5.99,cat1,,cat2,foto2.jpg,banner2.png,esta es otra descripcion
4,juego4,2000,5.99,cat1,,cat2,foto2.jpg,banner2.png,esta es otra descripcion
5,juego5,2000,5.99,cat1,,cat2,foto2.jpg,banner2.png,esta es otra descripcion
6,juego6,2000,5.99,cat1,,cat2,foto2.jpg,banner2.png,esta es otra descripcion
7,juego7,2000,5.99,cat1,,cat2,foto2.jpg,banner2.png,esta es otra descripcion
8,juego8,2000,5.99,cat1,,cat2,foto2.jpg,banner2.png,esta es otra descripcion
9,juego9,2000,5.99,cat1,,cat2,foto2.jpg,banner2.png,esta es otra descripcion
10,juego10,2000,5.99,cat1,,cat2,foto2.jpg,banner2.png,esta es otra descripcion
"""
