import sqlite3

conex = sqlite3.connect('productos.db')
cursor = conex.cursor()
cursor.execute("CREATE TABLE PRODUCTO (CODIGO_P VARCHAR(20) PRIMARY KEY, NOMBRE_P VARCHAR(20) , SECCION_P VARCHAR(20))")

productos = [
    ('AR01', 'POLLO', 'CARNES'),
    ('AR02', 'MANZANA', 'FRUTAS'),
    ('AR03', 'LECHE', 'LACTEOS'),
]

cursor.execute("INSERT INTO PRODUCTO VALUES ('AR04', 'PISCO', 'LICORES')") 
conex.commit()
conex.close()