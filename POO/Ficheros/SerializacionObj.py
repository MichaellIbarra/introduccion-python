import pickle

lista = ["Juan", "Antonio", "Pedro", "Herminio"]
fichero = open('lista', 'rb')
lista = pickle.load(fichero)
fichero.close()
print(lista)
""" fichero = open("lista", "wb")

pickle.dump(lista, fichero)
fichero.close() """