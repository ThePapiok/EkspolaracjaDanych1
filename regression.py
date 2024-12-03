from tkinter import Button


class Regression:
    def __init__(self, container, root, data):
        self.root = root
        self.data = data
        self.container=container
        self.create_button()

    def create_button(self):
        button = Button(self.root, text="Regresyjny")
        button.place(x=200, y=100)
        button.config(width=15, height=1)