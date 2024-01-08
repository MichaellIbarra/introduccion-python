
#! 1

class Persona:
    def __init__(self, nombre,apellido,sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
    def Imprimir(self):
        print(f'El nombre de la persona es: {self.nombre}')
        print(f'el apellido de la persona es: {self.apellido}')
        print(f'el sexo de la persona es: {self.sexo}')
class Empleado(Persona):
    def empleado(self, salario):
        self.salario = salario
        print(f'Su salario es: {self.salario} del empleado {self.nombre}')
        
empleado = Empleado('Matichelo', 'Ibarra', 'Masculino')
empleado.Imprimir()
empleado.empleado(100)

#! 2
#creame un sistema de api que esta conectado con chatgpt y que me devuelva una respuesta
