# Problema 1: solucione empleando algoritmo de Funciones y listas (10 ptos.)
# Realizar un programa para una escuela de primaria que dicta N cursos, la secretaria desea ingresar
# el nombre del curso C[] y sus respectivas horas de dictado H[] (entre 3 y 5 hr dictado c/u).
#* Almacenar y mostrar de cada curso, su nombre y respectivo horas de dictado.
#* Permitir al usuario buscar el nombre de un curso y en caso se encuentre tercero en la lista, entonces construir una clave con los 2 primeros caracteres del curso concatenado a sus respectivas horas (ejem: curso: fisica horas: 5 clave será: fi5)
# A todos los cursos cuyo nombre supere 6 caracteres, incrementare 2 hr de duración a su curso Si hay menos de 5 cursos registrados, entonces mostrar el promedio general de horas de dictado, caso contrario, eliminar el curso ubicado segundo en la lista, por orden académico. 

def condicioncion_cursos(cursos, horas):
    # A todos los cursos cuyo nombre supere 6 caracteres, incrementare 2 hr
    for i in range(len(cursos)):
        if len(cursos[i]) > 6:
            horas[i] += 2
    # Si hay menos de 5 cursos registrados, entonces mostrar el promedio general de horas de dictado
    if len(cursos) < 5:
        promedio = sum(horas) / len(horas)
        print(f"Promedio de horas dictadas: {promedio}")
    else:
        # caso contrario, eliminar el curso ubicado segundo en la lista, por orden académico
        cursos.pop(1)
        horas.pop(1)
    

def cursos_ingresado():
    
    nuC = int(input("Ingrese el número de cursos:"))
    
    cursos = []
    horas = []
    
    for i in range(nuC):
        nombreC = input("Ingrese el nombre del curso: ")
        cursos.append(nombreC)
        while True:
            horasC = int(input("Ingrese las horas del curso: "))
            if horasC >= 3 and horasC <= 5:
                horas.append(horasC)
                break
            else:
                print("Error, las horas deben ser entre 3 y 5")
    return cursos, horas
    
    
def mostrar_cursos(cursos, horas):
    for i in range(len(cursos)):
        print("Cursos y Horas mostrados")
        print(f"Curso: {cursos[i]} Horas: {horas[i]}")
    
def buscar_clave(cursos, horas):
    buscar = input("Ingrese el nombre del cursos para buscar")
    if buscar in cursos:
        indice = cursos.index(buscar)
        clave = cursos[indice][0:2] + str(horas[indice])
        print(clave)
  
cursos, horas = cursos_ingresado()
mostrar_cursos(cursos, horas)
buscar_clave(cursos, horas)
condicioncion_cursos(cursos, horas)