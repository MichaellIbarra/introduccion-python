from tkinter import *

root = Tk()

texto = Text(root)
texto.pack()
texto.config(width=40, height=10, padx=15, pady=15, font=("Curier", 20), selectbackground="red")
label = Label(root, text="Escribe algo")
label.pack()
label.config(bg="red", fg="white", font=("Curier", 20))






root.mainloop()