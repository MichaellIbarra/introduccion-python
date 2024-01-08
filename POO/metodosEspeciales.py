class Coche:
    # def __init__(self, marca=None, kilometros=None, anio=None):
    def __init__(self, marca, kilometros, anio):
        # encapsulamiento
        self.__marca = marca
        self.kilometros = kilometros
        self.anio = anio
        self.__ruedas = 4
        print(f"se ha creado un auto {self.__marca} y contiene {self.__ruedas} ruedas")
    def __del__(self):
        print(f"se ha vendido del auto de la marca {self.__marca}")
        
    def __str__(self):
        return "El auto es un {}, tiene {}, y es del año {}".format(self.__marca, self.kilometros, self.anio)
    def arrancamos(self, arrancar):
        self.arrancar = arrancar
        if (self.arrancar):
            print(f"Se arrancó el auto {self.__marca}")
        else:
            print(f"No se arrancó el auto {self.__marca}")
            
    def __len__(self):
        return len(self.__marca)

""" miCoche = Coche()
miCoche.marca = 'Ford'
miCoche.kilometros = 2005
miCoche.anio = 1998 """
miCoche = Coche('Ferrari', 1000, 2013)

miCoche.marca = 'moto'
print(str(miCoche))
print(len(miCoche))
miCoche.arrancamos(False)
del(miCoche)