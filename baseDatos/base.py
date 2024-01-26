import sqlite3

conex = sqlite3.connect("miBase.db")
cursor = conex.cursor()

# cursor.execute("CREATE TABLE USUARIOS(NOMBRE VARCHAR(50), EDAD INTEGER, SEXO VARCHAR(50))")

# cursor.execute("INSERT INTO USUARIOS VALUES('Roxana', 50, 'Femenino')")
# cursor.execute("SELECT * FROM USUARIOS")
# usuarios = cursor.fetchone()
""" for i in usuarios:
    print(str(i[0])+" contiene la edad "+str(i[1]) ) """
# print(usuarios)

""" print("Hola Ingrese sus datos")
nombre = input("ingrese su nombre")
edad = int(input("ingrese su edad"))
genero = input("ingrese su genero")

muchosUsuarios = [
    (''+ nombre +'',''+str(edad)+'', ''+ genero +''),
]


cursor.executemany("INSERT INTO USUARIOS VALUES(?,?,?)", muchosUsuarios) """


def verusuarios():
    cursor.execute("SELECT * FROM USUARIOS")
    verusuarios = cursor.fetchall()
    for i in verusuarios:
        print(str(i[0])+" contiene la edad "+str(i[1])+" y es de genero "+str(i[2]))
while 1:
    print("\n1. Ver usuarios")
    print("2. Agregar usuarios")
    print("3. Ver Usuarios Masculinos")
    print("5. Salir \n")
    opcion= int(input("ingrese una opcion"))
    if opcion==1:
        verusuarios()
    elif opcion==2:
        print("Hola Ingrese sus datos")
        nombre = input("ingrese su nombre")
        edad = int(input("ingrese su edad"))
        genero = input("ingrese su genero")
        muchosUsuarios = [
            (''+ nombre +'',''+str(edad)+'', ''+ genero +''),
        ]
        cursor.executemany("INSERT INTO USUARIOS VALUES(?,?,?)", muchosUsuarios)
    elif opcion==3:
        cursor.execute("SELECT * FROM USUARIOS WHERE SEXO='Masculino'")
        soloM = cursor.fetchall()
        print("Usuarios Masculinos")
        print(soloM)
    else:
        print("opcion no valida")
    
    
conex.commit()
conex.close()










