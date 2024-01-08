from tkinter import *

root = Tk()

image = PhotoImage(file="tenor.gif")
label = Label(root, image=image)
label.pack()

texto_nuevo= StringVar()
texto_nuevo.set("Nuevo Texto")

root.title("Interfaz Gráfica de Matichelo")
root.resizable(0, 0)
root.config(width=500, height=300)

label = Label(root, text="Hola que tal")
label.place(x=100, y=50)
label.config(bg="blue", fg="white", font=("Curier", 20))

label = Label(root, text="Test label Function")
label.place(x=100, y=100)
label.config(bg="red", fg="green", font=("Comic Sans Ms", 18, "bold"), textvariable=texto_nuevo)











root.mainloop()