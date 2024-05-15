class Numero:
    # Constructor de la clase
    #__init__ es un método especial que se llama cuando se crea un objeto de la clase
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def combinar_digitos(self):
        # Obtener el primer dígito del primer número
        primer_digito_num1 = int(str(self.num1)[0])
        
        # Obtener el segundo dígito del segundo número
        segundo_digito_num2 = int(str(self.num2)[1])
        
        # Construir el nuevo número combinando los dígitos
        nuevo_numero = int(str(primer_digito_num1) + str(segundo_digito_num2))
        
        return nuevo_numero

# Función principal
def panel():
    # Solicitar al usuario que ingrese dos números de 2 cifras cada uno
    num1 = int(input("Ingrese el primer número de 2 cifras: "))
    num2 = int(input("Ingrese el segundo número de 2 cifras: "))
    
    # Crear una instancia de la clase Numero
    num_obj = Numero(num1, num2)
    
    # Llamar al método para combinar los dígitos
    resultado = num_obj.combinar_digitos()
    
    # Mostrar el resultado
    print(f"Nuevo número combinando dígitos: {resultado}")


# Llamar a la función principal
panel()