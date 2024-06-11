class Persona:
    
    def solicitarDocumento(self, año_n, año_a):
        edad = año_a - año_n
        if edad >= 18:
            return  "si puedes solcitar el documenta nacional xd"
        else:
            return "no puedes p, menor eres xd"
        
    def tienesAportes(self, eslaboral):
        if eslaboral:
            return " tienes fondos de aporte"
        else:
            return " no tiene vida laboral"

# Herencia
class Michaell(Persona):
    def tienesAportes(self, eslaboral):
        if eslaboral:
            return " tienes fondos de aporte"
        else:
            return " no tiene vida laboral"
        
        
año_nacimiento = int(input("tu año de nacimiento")) # 2005
año_actual = int(input("el año actual")) # 2024

mostrarP = Persona() # creando instancia de clase que se llama Personal
print(mostrarP.solicitarDocumento(año_nacimiento, año_actual))
