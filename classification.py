from tkinter import Button, Frame, Label


class Classification:
    def __init__(self, container, root, data):
        self.container = container
        self.data = data
        self.root = root
        self.create_button()
        self.tn = 0
        self.tp = 0
        self.fp = 0
        self.fn = 0

    def create_button(self):
        button = Button(self.root, text="Klasyfikacyjny", command=lambda: self.start_rating())
        button.place(x=50, y=100)
        button.config(width=15, height=1)

    def start_rating(self):
        matrices = Frame(self.container)
        title = Label(matrices, text="Macierze pomyłek", justify="center", font=("Arial", 30))
        title.pack(side="top")
        self.create_confusion_matrix(matrices, self.data["C50_PV"], "1")
        self.create_confusion_matrix(matrices, self.data["rf_PV"], "2")
        matrices.pack(side="top", anchor="nw")

    def create_confusion_matrix(self,matrices, pre, index):
        true = self.data["income"]
        for i in range(len(pre)):
            if pre[i] == true[i]:
                if pre[i] == ">50K":
                    self.tp=self.tp+1
                else:
                    self.tn=self.tn+1
            else:
                if pre[i] == ">50K":
                    self.fp=self.fp+1
                else:
                    self.fn=self.fn+1
        matrix = Frame(matrices, width=250, height=220, bg="#e6e8eb")
        matrix.pack(side="left", padx=15, pady=15)
        title = Label(matrix, text="Model " + index, font=("Arial", 20), bg="#e6e8eb")
        title.place(x=80, y=2)
        elements = Frame(matrix, width=250, height=180, bg="black")
        elements.place(x=0, y=40)
        element1 = Frame(elements, width=82, height=58, bg="#e6e8eb")
        element1.place(x=0, y=0)
        element2 = Frame(elements, width=81, height=58, bg="#e6e8eb")
        element2.place(x=85, y=0)
        element2.pack_propagate(False)
        element3 = Frame(elements, width=81, height=58, bg="#e6e8eb")
        element3.place(x=169, y=0)
        element3.pack_propagate(False)
        element4 = Frame(elements, width=82, height=58, bg="#e6e8eb")
        element4.place(x=0, y=61)
        element4.pack_propagate(False)
        element5 = Frame(elements, width=81, height=58, bg="#e6e8eb")
        element5.place(x=85, y=61)
        element5.pack_propagate(False)
        element6 = Frame(elements, width=81, height=58, bg="#e6e8eb")
        element6.place(x=169, y=61)
        element6.pack_propagate(False)
        element7 = Frame(elements, width=82, height=58, bg="#e6e8eb")
        element7.place(x=0, y=122)
        element7.pack_propagate(False)
        element8 = Frame(elements, width=81, height=58, bg="#e6e8eb")
        element8.place(x=85, y=122)
        element8.pack_propagate(False)
        element9 = Frame(elements, width=81, height=58, bg="#e6e8eb")
        element9.place(x=169, y=122)
        element9.pack_propagate(False)
        label1 = Label(element2, width=81, font=("Arial", 30), text="0", bg="#e6e8eb")
        label1.pack(expand=True)
        label2 = Label(element3, width=81, font=("Arial", 30), text="1", bg="#e6e8eb")
        label2.pack(expand=True)
        label3 = Label(element4, width=81, font=("Arial", 30), text="0", bg="#e6e8eb")
        label3.pack(expand=True)
        label4 = Label(element7, width=81, font=("Arial", 30), text="1", bg="#e6e8eb")
        label4.pack(expand=True)
        label5 = Label(element5, width=81, font=("Arial", 15), text=self.tn, bg="#e6e8eb")
        label5.pack(expand=True)
        label6 = Label(element6, width=81, font=("Arial", 15), text=self.fp, bg="#e6e8eb")
        label6.pack(expand=True)
        label7 = Label(element8, width=81, font=("Arial", 15), text=self.fn, bg="#e6e8eb")
        label7.pack(expand=True)
        label8 = Label(element9, width=81, font=("Arial", 15), text=self.tp, bg="#e6e8eb")
        label8.pack(expand=True)

