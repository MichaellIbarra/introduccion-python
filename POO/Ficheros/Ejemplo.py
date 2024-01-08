from io import open
import pickle
# 1. Cree un fichero y ábralo en modo escritura, luego asigne un texto a una variable e insértelo en el fichero. Por último, visualice el documento.txt si fue escrito correctamente.

fichero = open("documento.txt", "w")
texto = "Presentación de la tarea"
fichero.write(texto)
fichero.close()
ficheroRead = open("documento.txt", "r")
textRead = ficheroRead.read()
ficheroRead.close()
print(textRead)

#

diccionario = {"Matichelo": 18, "Juan": 24, "Pedro": 30}
ficheroD = open("diccionario", "wb")
pickle.dump(diccionario, ficheroD)
ficheroD.close()