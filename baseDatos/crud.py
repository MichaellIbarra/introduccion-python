""" 
C = CREATE
R = READ
U = UPDATE
D = DELETE

"""

import sqlite3


conex = sqlite3.connect('MISPRODUCTOS.db')
cursor = conex.cursor()


""" # ! CREATE
cursor.execute("INSERT INTO MISPRODUCTOS VALUES (null, 'GEOMTRY DASH', 'VIDEOJUEGOS')") """

""" 
! READ
cursor.execute("SELECT * FROM MISPRODUCTOS WHERE SECCION = 'LACTEOS'")
productos = cursor.fetchall()
print(productos) """

""" 
! UPDATE
cursor.execute("UPDATE MISPRODUCTOS SET SECCION = 'DEPORTE' WHERE SECCION= 'DEPORTES'") """

"""
! DELETE
cursor.execute("DELETE FROM MISPRODUCTOS WHERE ID = 8") """
conex.commit()
conex.close()