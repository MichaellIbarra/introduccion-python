from tkinter import *
def imprimirL():
    imprimir.config(text=w.get())
def imprimirC():
    imprimir2.config(text=e.get())    
    

root = Tk()

root.geometry("400x400")


label = Label(root, text="Elige una opción")
label.pack()
w = Spinbox(root, values=("python", "html5", "java", "JavaScript"), command=imprimirL)
w.pack()
e = Spinbox(root, values=("carne", "pollo", "fruta", "jamon"), command=imprimirC)
e.pack()


imprimir = Label(root)
imprimir.pack()
imprimir2 = Label(root)
imprimir2.pack()

root.mainloop()