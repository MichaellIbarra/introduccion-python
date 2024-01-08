class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    def datosPersonales(self):
        print(f"el nombre de la persona es: {self.nombre}")
        print(f"la edad de la persona es: {self.edad}")
        print(f"el sexo de la persona es: {self.sexo}")
        
print('Registro de Persona')
nombre = input('nombre de la persona: ')
edad = int(input('edad de la persona:'))
sexo = input('ingrese el sexo de la persona: F/M : ')
if sexo == 'F':
    sexo= 'Femenino'
elif sexo == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Indefinido'
p = Persona(nombre, edad, sexo)
p.datosPersonales()