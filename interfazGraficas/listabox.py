from tkinter import *


def addProduct():
    listaProductos.insert(END ,entrada.get())
    
def deleteProducto():
    listaProductos.delete(ANCHOR)
    
root = Tk()


root.geometry("400x400")

productos = Label(root, text="Productos")
productos.pack()

listaProductos = Listbox(root, width=50, height=10)
listaProductos.insert(0, "carne")
listaProductos.insert(1, "pollo")
listaProductos.insert(2, "jugo")
listaProductos.pack()

#eliminar productos
listaProductos.delete(2)


entrada = Entry(root, bd=10)
entrada.pack()


botton = Button(root, text="agregar producto", command=addProduct)
botton.pack()

botton2 = Button(root, text="Delete producto", command=deleteProducto)
botton2.pack()




root.mainloop()