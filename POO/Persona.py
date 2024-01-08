class Persona:
    def __init__ (self, nombre, edad, sexo, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.nacionalidad = nacionalidad
        
persona = Persona('Matichelo', 18, 'M', 'Peruano')

class Auto:
    def __init__(self, marca, modelo, anio, color, ):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__color = color
    def estado(self, estado):
        self.estado = estado
        if (self.estado):
            print('el auto esta encendido')
        else:
            print('el auto esta apagado')

auto1 = Auto('Ferrari', 'X', 2023, 'negro')
auto1.estado(False)