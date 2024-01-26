from tkinter import *

def click(valor):
    entrada.insert(END, valor)
    
    
def borrar():
    entrada.delete(0, END)

def operaciones():
    operacion = entrada.get()
    resultado = eval(operacion)
    entrada.delete(0, END)
    entrada.insert(0, resultado)
    
root = Tk()
root.title("Calculadora")

#Entrada
entrada = Entry(root, font=("Calibri 20"))
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


#Botones
# lambda  nose hace escribir funcione en una sola linea y poder argumentos
boton1 = Button(root,text="1", width=5, height=2, command=lambda:click(1))
boton2 = Button(root,text="2", width=5, height=2, command=lambda:click(2))
boton3 = Button(root,text="3", width=5, height=2, command=lambda:click(3))
boton4 = Button(root,text="4", width=5, height=2, command=lambda:click(4))
boton5 = Button(root,text="5", width=5, height=2, command=lambda:click(5))
boton6 = Button(root,text="6", width=5, height=2, command=lambda:click(6))
boton7 = Button(root,text="7", width=5, height=2, command=lambda:click(7))
boton8 = Button(root,text="8", width=5, height=2, command=lambda:click(8))
boton9 = Button(root,text="9", width=5, height=2, command=lambda:click(9))
boton0 = Button(root,text="0", width=15, height=2, command=lambda:click(0))

boton_borrar = Button(root, text="DEL", width=5, height=2, command=lambda:borrar())
boton_parentesis1 = Button(root, text="(", width=5, height=2, command=lambda:click("("))
boton_parentesis2 = Button(root, text=")", width=5, height=2, command=lambda:click(")"))
boton_punto = Button(root, text=".", width=5, height=2, command=lambda:click("."))


boton_multiplicacion = Button(root, text="*", width=5, height=2, command=lambda:click("*"))
boton_division = Button(root, text="/", width=5, height=2, command=lambda:click("/"))
boton_suma = Button(root, text="+", width=5, height=2, command=lambda:click("+"))
boton_resta = Button(root, text="-", width=5, height=2, command=lambda:click("-"))
boton_igual = Button(root, text="=", width=5, height=2, command=lambda:operaciones())


#color botones
boton_borrar.grid(row=1, column=0, padx=5, pady=2)
boton_parentesis1.grid(row=1, column=1, padx=5, pady=2)
boton_parentesis2.grid(row=1, column=2, padx=5, pady=2)
boton_division.grid(row=1, column=3, padx=5, pady=2)

boton7.grid(row=2, column=0, padx=5, pady=2)
boton8.grid(row=2, column=1, padx=5, pady=2)
boton9.grid(row=2, column=2, padx=5, pady=2)
boton_multiplicacion.grid(row=2, column=3, padx=5, pady=2)


boton4.grid(row=3, column=0, padx=5, pady=2)
boton5.grid(row=3, column=1, padx=5, pady=2)
boton6.grid(row=3, column=2, padx=5, pady=2)
boton_suma.grid(row=3, column=3, padx=5, pady=2)

boton3.grid(row=4, column=0, padx=5, pady=2)
boton2.grid(row=4, column=1, padx=5, pady=2)
boton1.grid(row=4, column=2, padx=5, pady=2)
boton_resta.grid(row=4, column=3, padx=5, pady=2)

boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=2)
boton_punto.grid(row=5, column=2, padx=5, pady=2)
boton_igual.grid(row=5, column=3,padx=5, pady=2)




root.mainloop()
