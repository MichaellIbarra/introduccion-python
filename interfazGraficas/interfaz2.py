from tkinter import *
import os

root = Tk()
root.title("Interfaz Gráfica de Matichelo")
# w x h
root.resizable(1, 1)
# root.geometry("640x480")
root.iconbitmap("hacker.ico")


miFrame = Frame(root)
# miFrame.pack(side="bottom")
miFrame.pack(fill='x', expand=True)
miFrame.config(width="500", height="400")
miFrame.config(cursor="pirate")
miFrame.config(bg="red")
miFrame.config(bd="20")
miFrame.config(relief="ridge")

root.config(cursor="boat")
root.config(bg="blue")
            
            
root.mainloop()
