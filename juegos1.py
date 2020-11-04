class Juegos:
    def __init__(self):
        self.juegos = [
            {
                "id": 0,
                "nombre": "juego1",
                "año": 1999,
                "precio": 10.01,
                "categoria": ["cat1"],
                "foto": "foto1.jpg",
                "banner":"banner1.jpg",
                "descripcion":"eta es una descripion chida"
            }
        ]

    def carga(self,string):
        try:                                      #errores
            for linea in string.split('\n'):      #salto de lineas
                obj = {
                    "id": None,
                    "nombre": None,
                    "año":None,
                    "precio":None,
                    "categoria":[],
                    "foto":None,
                    "banner":None,
                    "descripcion":None
                }      

                data = linea.split(',')
                obj['id'] = int(data[0])
                obj['nombre'] = data[1]
                obj['año'] = int(data[2])
                obj['precio'] =  float(data[3])
                obj['foto'] =  data[-3]
                obj['banner'] = data[-2]
                obj['descripcion'] = data[-1]
                if (data[4] != ''):
                    obj ['categoria'].append(data [4])
                if (data[5] != ''):
                    obj ['categoria'].append(data [5])
                if (data[6] != ''):
                    obj ['categoria'].append(data [6])

                obj ['foto'] = data[-3]
                obj ['banner'] = data[-2]
                obj ['descripcion'] = data [-1]
                self.juegos.append(obj)

            return{"ok":True}      #si no hay error da true 
        except:
            return{"ok":False}     #si hay error da false 


    def get_all(self):
        return{"juegos":self.juegos}

