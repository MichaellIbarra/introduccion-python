from tkinter import *
def eleccion():
    elegir=""
    
    if pollo.get() ==1:
        elegir += "has elegido pollo \n"
    if pizza.get() ==1:
        elegir += "has elegido pizza \n"
    if hamburguesa.get() ==1:
        elegir += "has elegido hamburguesa \n"
    imprimir.config(text=elegir)
    
    if pollo.get()== 1 and pizza.get()==1 and hamburguesa.get()==1:
        imprimir.config(text="has elegido todo")

root = Tk()
root.geometry("400x300")

frame = Frame(root)
frame.pack()

pizza = IntVar()
hamburguesa = IntVar()
pollo = IntVar()


foto1 = PhotoImage(file="pizza.png")
foto2 = PhotoImage(file="hamburguesa.png")
foto3 = PhotoImage(file="pollo.png")

label1 = Label(root, image=foto1).pack()
label1 = Label(root, image=foto2).pack()
label1 = Label(root, image=foto3).pack()

Checkbutton(frame, text="Pizza", variable=pizza, onvalue=1, offvalue=0, command=eleccion).pack(side=RIGHT)
Checkbutton(frame, text="hamburguesa", variable=hamburguesa, onvalue= 1, offvalue=0, command=eleccion).pack(side=RIGHT)
Checkbutton(frame, text="pollo", variable=pollo, onvalue= 1, offvalue=0, command=eleccion).pack(side=RIGHT)


imprimir = Label(root)
imprimir.pack()


root.mainloop()