from tkinter import *
from tkinter import filedialog

root= Tk()


def abrir():
    archivo = filedialog.askopenfilename(title="Abrir", initialdir="Documentos", filetypes=[("Archivos de texto", "*.txt"),("Archivos de photoshop", "*.psd")])
    # archivo = filedialog.askopenfilename(title="Abrir", initialdir="Documentos", filetypes=(("Archivos de texto", "*.txt"), ("Archivos de photoshop", "*.psd")))
    print(archivo)

button = Button(root, text="abrir archivo", command=abrir).pack()

root.mainloop()