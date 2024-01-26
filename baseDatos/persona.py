import sqlite3
"""

if not variable = es para verificar si la variable esta vacia
if variable is None = es para verificr si la variable es nula 
C = CREATE
R = READ
U = UPDATE
D = DELETE
"""

# conex = sqlite3.connect('persona.db')
# cursor = conex.cursor()

# cursor.execute(" CREATE TABLE PERSONA (NOMBRE VARCHAR(80), EDAD INTEGER, SEXO VARCHAR(50), DNI INTEGER PRIMARY KEY)")


def insertarDato(cursor):
    nombre = input("INGRESE SU NOMBRE:")
    edad = int(input("INGRESE SU EDAD:"))
    sexo = input("INGRESE SU GENERO, F O M:")
    dni = int(input("INGRESE SU DNI, 12345678: "))
    cursor.execute("INSERT INTO PERSONA VALUES (?,?,?,?)",
                  (nombre, edad, sexo, dni))


def verDato(cursor):
    cursor.execute("SELECT * FROM PERSONA")
    verpersona = cursor.fetchall()
    if not verpersona:
        print("\n NO HAY DATOS DE PERSONAS \n")
    else:
        for i in verpersona:
            print(str(i[0]) + " " + str(i[1]) +
                  " " + str(i[2]) + " " + str(i[3]))


def actualizarDato(cursor):
    print("ACTUALIZAR DATOS \n 1. NOMBRE \n 2. EDAD")
    print("INGRESE SU DNI PARA ACTUALIZAR SUS DATOS")
    dni = int(input("INGRESE SU DNI, 12345678: "))
    opcion = int(input("INGRESE SU OPCION"))
    if opcion == 1:
        nombre = input("INGRESE NUEVO NOMBRE:")
        cursor.execute(
            "UPDATE PERSONA SET NOMBRE = ? WHERE DNI = ?", (nombre, dni))
    elif opcion == 2:
        edad = int(input("INGRESE NUEVA EDAD: "))
        cursor.execute(
            "UPDATE PERSONA SET EDAD = ? WHERE DNI = ?", (edad, dni))
    else:
        print("DEBE SELECIONAR UNA OPCIÓN VALIDA")


def eliminarDato(cursor):
    try:
        print("ELIMINAR PERSONA")
        dni = int(input("INGRESE SU DNI, 12345678: "))
        cursor.execute("SELECT * FROM PERSONA WHERE DNI = ?", (dni,))
        result = cursor.fetchone()
        print(result)
        if result is None:
            print("NO SE PUEDE ELIMINAR POR QUE NO EXISTE LA PERSONA EN LA BASE DE DATOS")
        else:
            cursor.execute("DELETE FROM PERSONA WHERE DNI=?", (dni,))
            print("SE ELIMINO SATISFACTORIAMENTE")
    except ValueError as a:
        print("ERROR AL ELIMINAR",  a)


def main():
    with sqlite3.connect('persona.db') as conex:
        cursor = conex.cursor()
        while True:
            print("1. Insertar datos")
            print("2. Ver datos")
            print("3. Actualizar datos")
            print("4. Eliminar datos")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                insertarDato(cursor)
                conex.commit()
            elif opcion == "2":
                verDato(cursor)
            elif opcion == "3":
                actualizarDato(cursor)
                conex.commit()
            elif opcion == "4":
                eliminarDato(cursor)
                conex.commit()
            elif opcion == "3":
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
                
                
if __name__ == "__main__":
    main()