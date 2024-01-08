
#! Herencia Multiple 
class Clase1:
    def metodo1(self):
        print("Metodo 1")

class Clase2:
    def metodo2(self):
        print("Metodo 2")
        
        #hereda los parametros de las clases anteriores
class Clase3(Clase1, Clase2):
    def metodo3(self):
        print("Metodo 3")
        
multiple = Clase3()
multiple.metodo1()
multiple.metodo3()