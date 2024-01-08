from tkinter import *
root = Tk()
root.title("Interfaz Gráfica de Matichelo")
frame = Frame(root, width= 500, height= 300)
frame.pack()

entrada = Entry(frame)
entrada.grid(row=0, column= 1,  padx=50)
entrada.config(justify="left", border="5")

entrada2 = Entry(frame)
entrada2.grid(row=1, column= 1, padx=50)
entrada2.config(border="5", justify="center", state="normal", show="*")



label1 = Label(frame, text="Nombre:")
label1.grid(row=0, column=0, sticky="s", padx=15, pady=15)


label2 = Label(frame, text="Password:")
label2.grid(row=1, column=0, padx=15, pady=15)
root.mainloop()