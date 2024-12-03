from tkinter import *

from get_data import get_data_from_files

root = Tk()
root.title("Zadanie programistyczne 2")
root.geometry('1000x1000')
root.config(bg='#d2d5d9')
container = Frame(root, bg='#e6e8eb', width=800, height=600, bd=2, relief=GROOVE)
container.place(x=80, y=150)
buttonFile = Button(root, text="Wczytaj plik", command=lambda: get_data_from_files(container, root))
buttonFile.place(x=50, y=50)
root.mainloop()