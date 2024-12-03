from tkinter import *


from get_data import get_data_from_files

root = Tk()
root.title("Zadanie programistyczne 2")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.config(bg='#d2d5d9')
container = Frame(root, width=screen_width - 200, height=screen_height - 300, bd=2, relief=GROOVE)
container.pack_propagate(False)
container.place(x=100, y=150)
buttonFile = Button(root, text="Wczytaj plik", command=lambda: get_data_from_files(container, root))
buttonFile.place(x=50, y=50)
root.mainloop()