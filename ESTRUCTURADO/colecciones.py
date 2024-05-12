""" 
#!listas -- son mutables
personas = [True, 'pedro']

print(personas[0])
while personas[0]:
# 0 1 2 3 4 5 6 7 8 
# -5 -4  -3  -2  -1
    print(personas[-1]) 

animales = ['gato', 'leon', 'zorro', ['python', 'c++']]
animales.append('serpiente')
del animales[0]
animales.insert(0, 'Gato')

print(animales[3][0]) 

animales = ['gato', 'leon', 'zorro', ['python', 'c++'], 'perro']
print(animales[2:-2]) 

colores = [11, 'python', True, [1,2,3,4,5]]
coloradd = [6,7,8]
colores[3] = coloradd + colores[3]
print(colores)

"""

#! Tuplas -- inmutables
""" lista = [11,11]
print(lista.count(11))
tupla = (11, 'python', True, [1,2,3],11)
print(tupla.count(11))
print(tupla) """

""" #! Diccionarios
diccionarios = {'Michaell': 20, 'Juan': 50}
diccionarios['Michaell'] = 60
diccionarios.pop('Juan')
del diccionarios['Michaell']
print(diccionarios) """
""" edades = input('ingrese el nombre para obtener las edades')
try:
    if diccionarios[edades]:
        print(diccionarios[edades])
except KeyError:
    print('No se encontro')
     """


#TODO: PILAS Y COLA

""" filas = ['Michaell', 'Roxana', 'kimy', 'Jaime']
print(filas)
filas.append('renzo')
print(filas)
i = filas.pop(0)
print(f'están atendiendo a {i}')
lista = ['a', 'b','c']
o = lista.append('d')
"""

#! CONJUNTOS
# un solo elemento no se puede repetir el mismo elemento
# conjunto de coleccion desordenado
""" conjunto = set()
conjunto = {1,2,3,4,5,6,6}
conjunto.add('Matichelo')
conjunto.add('Juan')
conjunto.add('Javier')
print(conjunto) """


""" mi_conjunto = set()  # Crea un conjunto vacío

# Agrega elementos al conjunto
mi_conjunto.add(1)
mi_conjunto.add(2)
mi_conjunto.add(3)
mi_conjunto.discard(1)
mi_conjunto.clear()
print(mi_conjunto) """

""" 
cursos = []  # Mover la declaración fuera del bucle

while True:
    insertarC = input("Insertar curso: ")
    cursos.append(insertarC)
    print(insertarC)
    llave = input('¿Quieres seguir insertando cursos? (s/n): ')
    if llave.lower() == 'n':
        break 
print("Cursos insertados:", cursos)
for i in cursos:
    print(i) """
    
