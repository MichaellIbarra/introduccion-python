import sqlite3

def conectar():
    con = sqlite3.connect("pruebas.db")
    cursor = con.cursor()
    return con, cursor



def crearTabla(con, cursor):
    sentencia = """
        CREATE TABLE IF NOT EXISTS usuarios
        (ID INTEGER PRIMARY KEY NOT NULL, 
        USUARIO TEXT NOT NULL,
        EMAIL TEXT NOT NULL, 
        CLAVE TEXT NOT NULL);
    """
    cursor.execute(sentencia)
    con.close()
    print("Tabla creada Correctamente")
    
    
def insertarDato(con,cursor, datos):
    # sentencia = "INSERT INTO usuarios (ID, USUARIO, EMAIL, CLAVE) VALUES (1, 'Matichelo', 'matichelo@gmail.com', 'contraseña')"
    # cursor.execute(sentencia)
    
    sentencia = "INSERT INTO usuarios VALUES (null, ?, ?, ?)"
    print(sentencia, datos)
    cursor.executemany(sentencia, datos)
    con.commit()
    con.close()
    print("Datos insertados")
    
    
def mostrarDato(con, cursor):
    sentencia = "SELECT * FROM usuarios"
    resultado = cursor.execute(sentencia)
    # print(resultado.fetchall())
    for i in resultado:
        print(i)
    con.close()
    



def eliminarDato(con, cursor,id):
    sentencia = f"DELETE FROM usuarios WHERE ID = {id}"
    cursor.execute(sentencia)
    con.commit()
    # con.close()
    print("Datos Elminados")
    
def actualizarDato(con, cursor, id, nombre):
    try:
        consulta = f"SELECT * FROM usuarios WHERE ID = {id}"
        cursor.execute(consulta)
        result = cursor.fetchone()
        # print(result)
        if result is None:
            print("No existe el usuario con ese ID")
        else:
            sentencia = f"UPDATE usuarios SET USUARIO = '{nombre}' WHERE ID = {id}"
            cursor.execute(sentencia)
            con.commit()
            print("Datos Actualizados")
            # con.close()
            return True
    except Exception as e:
        print("ERROR AL ACTUALIZAR LOS DATOS", e)
    
if __name__ == "__main__":
    con,cursor = conectar()
    # crearTabla(con, cursor)
    # insertarDato(con, cursor)
    """ datos = [
                ('Michaell', 'michaell@gmail.com', '544321')
                ('fd', 'michafdfdfell@gmail.com', '543251')
                ('Micffvhaell', 'mffdichaell@gmail.com', '543421')
            ] """
            
    """ datos = []
    for i in range(5):
        datos.append(('Michaell'+str(i), 'michaell'+str(i)+'@gmail.com', '544321')) """
        
    # insertarDato(con,cursor, datos)
    actualizarDato(con, cursor, 63, 'Roxana')
    eliminarDato(con, cursor, 6)     
    mostrarDato(con,cursor)