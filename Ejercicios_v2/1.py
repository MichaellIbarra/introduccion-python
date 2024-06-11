class PaseoEscolar:
    
    def montoAlumno(self, numAlumno):
        if numAlumno >= 30:
            return 10
        elif 20 <= numAlumno <= 29:
            return 15
        elif 10 <= numAlumno <= 19:
            return 17
        else:
            return 30
    
    def montoBus(self):
        return 150
    
    def calculoPagar(self, numAlumno): 
        monto_alumno = numAlumno * self.montoAlumno(numAlumno)
        monto_bus = self.montoBus()
        total = monto_alumno + monto_bus
        return total

numAlumno = int(input("ingrese cantidad alumno: ")) # 30
mostrar = PaseoEscolar()
print(f" Monto a pagar por alumno S/. {mostrar.montoAlumno(numAlumno)}    ")
print(f" Monto del alquiler de bus S/. {mostrar.montoBus()}")
print(f"Total a pagar {mostrar.calculoPagar(numAlumno)} ")