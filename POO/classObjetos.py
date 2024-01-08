class Perro:
    # self es hacer referencias las caracteristicas metodos funciones etc
    def __init__(self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color
    def ver(self):
        print(f"El nombre del perro es {self.nombre}")
        print(f"la edad del perro es {self.edad}")
        print(f"El color del perro es {self.color}")
""" 
perro1 = Perro('Boby', 5, 'negro')
perro1.ver()
print()
perro2 = Perro('Juan', 10, 'blanco')
perro2.ver() """

print('bienvenido a nuestro consultorio de perros \nregistre su perro')
nombre = input('nombre del perrro: ')
edad = int(input('edad del perrro: '))
color = input('color del perrro: ')
perroR = Perro(nombre, edad, color)
print('fue registrado su perro')
perroR.ver()

