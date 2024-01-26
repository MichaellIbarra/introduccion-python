import sqlite3


# cursor.execute("CREATE TABLE articulos (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(50), CANTIDAD INTEGER)")

def insertar(cursor):
    nombre = input("ingrese el nombre del articulo")
    cantidad = int(input("ingrese la cantidad del producto"))
    sentencia = "INSERT INTO articulos VALUES (null, ?,?)"
    datos = (nombre, cantidad)
    cursor.execute(sentencia, datos)
    print("Datos insertados")

def mostrar(cursor):
    sentencia = "SELECT * FROM articulos"
    result = cursor.execute(sentencia)
    for i in result:
        print(str(i[0]) + " " + str(i[1]) + " " + str(i[2]))

def actualizar(cursor):
    id = int(input("ingrese el id del articulo a actualizar"))
    nombre = input("ingrese el nuevo nombre del articulo")
    sentencia = "UPDATE articulos SET NOMBRE = ? WHERE ID = ?"
    datos = (nombre, id)
    cursor.execute(sentencia, datos)
    print("Datos actualizados")
    
def eliminar(cursor):
    id = int(input("ingrese el id del articulo a eliminar"))
    sentencia = "DELETE FROM articulos WHERE ID = ?"
    cursor.execute(sentencia, (id,))
    print("Datos eliminados")

def main():
    with sqlite3.connect("articulos.db") as con:
        cursor = con.cursor()
        while True:
            print("1. Insertar datos\n2. Mostrar datos\n3. actualizar\n4. eliminar\n5. Salir")
            opc = int(input("ingrese una opción: "))
            if opc == 1:
                insertar(cursor)
                con.commit()
            elif opc == 2:
                mostrar(cursor)
            elif opc == 3:
                actualizar(cursor)
                con.commit()
            elif opc == 4:
                eliminar(cursor)
                con.commit()
            elif opc == 5:
                break
            else:
                print("ingrese una opción valida")
                
                
if __name__ == '__main__':
    main()