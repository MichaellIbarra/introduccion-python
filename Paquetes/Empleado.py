class Empleado:
    def __init__(self, anio, sueldo):
        self.anio = anio
        self.sueldo = sueldo

    def datosEmpleado(self):
        print("Nombre: ", self.anio)
        print("Sueldo: ", self.sueldo)