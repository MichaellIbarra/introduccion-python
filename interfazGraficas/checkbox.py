import tkinter as tk

from tkinter import ttk

class Application(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)

        main_window.title("Checkbutton en tkinter")

        self.checkbox = ttk.Checkbutton(self, text="Opción")

        self.checkbox.place(x=40, y=70)

        self.place(width=300, height=200)

main_window = tk.Tk()

app = Application(main_window)

app.mainloop()