

""" #! CONDICIONALES 
a = 1
if a >= 18:
    print('es mayor de edad')
else:
    print('es menor') 
    
edad = 18

if edad >= 18 and edad <= 65:
    print('es mayor de edad')
elif edad >= 65:
    print('es mayor de edad')
else: 
    print('es menor')"""
    

#! WHILE
# el bucle termina de ejecutar hasta que sea Falso
""" while True:
    print('hola')
     """
""" a = 1
while a <= 10:
    print(a)
    print(a<10)
    print('ejecuta esto hasta que llegue a 10', a)
    a +=1 
    
while True:
    entrada = int(input('ingrese un numero'))
    if entrada == 10:
        break
    print(entrada)
    a = 0
lenguajes = ['c++', 'python', 'javascript']
while a < len(lenguajes):
    print(lenguajes[a])
    a +=1
    
    """


#! FOR 

# la i es interadora lo que va hacer int
""" frutas = ['manza', 'pera', 'platano']
for i in range(len(frutas)):
    print(i)
    print(frutas[i]) """

""" vehiculos = ['moto', 'avion', 'carro', 'helicoptero']
for i in vehiculos:
    print(i)
 """
 
""" for i in range(1, 11):
    print(i) """
    
""" while True:
    try:
        password = int(input('Ingrese la contraseña: '))
        if password == 123:
            print('Correcto')
            break
        else:
            print('Incorrecto')
    except ValueError:
        print('No es un número')
 """

""" for i in range(5):
    print(i)
else:
    print("Bucle completado sin break") """
