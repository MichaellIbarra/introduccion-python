class Persona:
    def __init__(self, nombre, edad, apellido, sexo):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido
        self.sexo = sexo

    def datosPersonales(self):
        print(f'El nombre de la persona es: {self.nombre}')
        print(f'la edad de la persona es: {self.edad}')
        print(f'el apellido de la persona es: {self.apellido}')
        print(f'el sexo de la persona es: {self.sexo}')

miP = Persona('Michaell', 22, 'Ibarra', 'Masculino')
miP.datosPersonales()
print('************************************************')

class Empleado(Persona):
    def datosEmpleados(self, vacaciones, salario):
        print(f'Su días de vacaciones son: {vacaciones} y su nombre es {self.nombre} ')
        print(f'Su salario es: {salario} ')
        
miEmpleado = Empleado('Matichelo', 22, 'Martinez', 'M')
miEmpleado.datosPersonales()
miEmpleado.datosEmpleados(30,3000)