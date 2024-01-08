import pickle

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def datosPersonales(self):
        print("Nombre:", self.nombre)
        return print("Edad:", self.edad)


persona1 = Persona("Matichelo", 18)
persona2 = Persona("Juan", 24)


""" listaPersonas = [persona1, persona2]
fichero = open("personas", "wb")
pickle.dump(listaPersonas, fichero)
fichero.close()
del(fichero) """

fichero = open('perosonas', 'rb')
lista = pickle.load(fichero)
fichero.close()

for i in lista:
    i.datosPersonales()