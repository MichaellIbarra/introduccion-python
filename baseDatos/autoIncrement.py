import sqlite3

conex = sqlite3.connect('MISPRODUCTOS.db')
cursor = conex.cursor()

# cursor.execute("CREATE TABLE MISPRODUCTOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(20), SECCION VARCHAR(20))")

productos = [
    ('ASADO', 'CARNE'),
    ('PLATANO', 'FRUTAS'),
    ('RON', 'LICORES'),   
]

cursor.executemany("INSERT INTO MISPRODUCTOS VALUES (null, ?,?)", productos)
conex.commit()
conex.close()