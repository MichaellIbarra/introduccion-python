from tkinter import *
from tkinter import messagebox


def add():
    archivoEdit.add_command(label="Nuevo ga")

def salir():
    i = messagebox.askquestion("Salir", "¿está seguro que desea salir?")
    if i == "yes":
        root.destroy()


def acerca():
    messagebox.showinfo("Acerca de", "matichelo es un programador de python")


root = Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu)
root.title("Interfaz de Matichelo")
root.geometry("500x300")
root.resizable(0, 0)

archivoMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Nuevo archivo")
archivoMenu.add_command(label="Nueva ventana")
archivoMenu.add_separator()
# Agregar el comando "salir"
archivoMenu.add_command(label="Salir", command=salir)

archivoEdit = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Editar", menu=archivoEdit)
archivoEdit.add_command(label="Copiar")
archivoEdit.add_command(label="agregar ", command=add)

archivoAyuda = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)
archivoAyuda.add_command(label="Licencia", command=acerca)

root.mainloop()
