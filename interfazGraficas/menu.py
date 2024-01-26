from tkinter import *

def salir():
    root.destroy()

root = Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu)

archivoMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Nuevo archivo")
archivoMenu.add_command(label="Nueva ventana")
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=salir)  # Agregar el comando "salir"

archivoEdit = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Editar", menu=archivoEdit)
archivoEdit.add_command(label="Copiar")
archivoEdit.add_command(label="Pega")

archivoAyuda = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)
archivoAyuda.add_command(label="Licencia")

root.mainloop()