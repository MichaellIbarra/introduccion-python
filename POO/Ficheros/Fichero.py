from io import open


fichero = open("archivo.txt","r") # la creación y apertura
linea = fichero.readlines()
fichero.close()
print(len(linea))

""" texto = "Hola Soy\nMatichelo"
fichero.write(texto)
fichero.close() """
""" texto = fichero.read()
fichero.close()
print(texto) """
# print(texto.split(" ")[0])


gato = open("gato.txt", "a")
gato.write("Miua miua miua")
gato.close()