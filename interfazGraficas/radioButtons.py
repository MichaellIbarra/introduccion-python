from tkinter import *

def mostrar():
    if opciones.get() == 1:
        label2.config(text="haz elegido el genero masculino", bg="blue")
        
    elif opciones.get() ==2:
        label2.config(text="haz elegido el genero femenino", bg= "pink")
root = Tk()

opciones = IntVar()
label1 = Label(root, text="elige un genero")
label1.pack()
label1.config(bg="green", font=("Curier 10"))
Radiobutton(root, text="Masculino", variable=opciones, value=1, command=mostrar).pack()  
Radiobutton(root, text="Femenino", variable=opciones, value=2, command=mostrar).pack()  

label2 = Label(root)
label2.pack()

root.mainloop()