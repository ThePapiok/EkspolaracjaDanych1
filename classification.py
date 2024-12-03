from tkinter import Button

class Classification:
    def __init__(self, container, root, data):
        self.container = container
        self.data = data
        self.root = root
        self.create_button()

    def create_button(self):
        button = Button(self.root, text="Klasyfikacyjny")
        button.place(x=50, y=100)
        button.config(width=15, height=1)
