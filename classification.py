from tkinter import Button, Frame, Label




class Classification:
    def __init__(self, container, root, data):
        self.container = container
        self.data = data
        self.root = root
        self.create_button()
        self.tn = [0, 0]
        self.tp = [0, 0]
        self.fp = [0, 0]
        self.fn = [0, 0]

    def create_button(self):
        button = Button(self.root, text="Klasyfikacyjny", command=lambda: self.start_rating())
        button.place(x=50, y=100)
        button.config(width=15, height=1)

    def start_rating(self):
        matrices = Frame(self.container)
        title = Label(matrices, text="Macierze pomyłek", justify="center", font=("Arial", 30))
        title.pack(side="top")
        self.create_confusion_matrix(matrices, self.data["C50_PV"], 1)
        self.create_confusion_matrix(matrices, self.data["rf_PV"], 2)
        matrices.pack(side="left", anchor="n")
        indicators = Frame(self.container, width=800, height=800, padx=50)
        title = Label(indicators, text="Wskaźniki", justify="center", font=("Arial", 30))
        title.pack(side="top")
        self.create_indicators(indicators)
        indicators.pack(side="left", anchor="n")

    def create_confusion_matrix(self,matrices, pre, index):
        realIndex = index - 1
        true = self.data["income"]
        for i in range(len(pre)):
            if pre[i] == true[i]:
                if pre[i] == ">50K":
                    self.tp[realIndex]=self.tp[realIndex]+1
                else:
                    self.tn[realIndex]=self.tn[realIndex]+1
            else:
                if pre[i] == ">50K":
                    self.fp[realIndex]=self.fp[realIndex]+1
                else:
                    self.fn[realIndex]=self.fn[realIndex]+1
        matrix = Frame(matrices, width=250, height=220, bg="#e6e8eb")
        matrix.pack(side="left", padx=15, pady=15)
        title = Label(matrix, text="Model " + str(index), font=("Arial", 20), bg="#e6e8eb")
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
        label5 = Label(element5, width=81, font=("Arial", 15), text=self.tn[realIndex], bg="#e6e8eb")
        label5.pack(expand=True)
        label6 = Label(element6, width=81, font=("Arial", 15), text=self.fp[realIndex], bg="#e6e8eb")
        label6.pack(expand=True)
        label7 = Label(element8, width=81, font=("Arial", 15), text=self.fn[realIndex], bg="#e6e8eb")
        label7.pack(expand=True)
        label8 = Label(element9, width=81, font=("Arial", 15), text=self.tp[realIndex], bg="#e6e8eb")
        label8.pack(expand=True)

    def create_indicators(self, indicators):
        accuracy_model1 = (self.tp[0] + self.tn[0])/(self.fp[0] + self.fn[0] + self.tp[0] + self.tn[0])
        accuracy_model2 = (self.tp[1] + self.tn[1])/(self.fp[1] + self.fn[1] + self.tp[1] + self.tn[1])
        sensitivity_model1 = self.tp[0]/(self.fn[0] + self.tp[0])
        sensitivity_model2 = self.tp[1]/(self.fn[1] + self.tp[1])
        specificity_model1 = self.tn[0]/(self.tn[0] + self.fp[0])
        specificity_model2 = self.tn[1]/(self.tn[1] + self.fp[1])
        precision_model1 = self.tp[0]/(self.tp[0] + self.fp[0])
        precision_model2 = self.tp[1]/(self.tp[1] + self.fp[1])
        f1_model1 = (2*sensitivity_model1*precision_model1)/(sensitivity_model1+precision_model1)
        f1_model2 = (2*sensitivity_model2*precision_model2)/(sensitivity_model2+precision_model2)
        accuracy_container = Frame(indicators, width=400, height=150)
        accuracy_container.pack_propagate(False)
        accuracy_title = Label(indicators, text="Trafność", font=("Arial", 15), justify="center")
        accuracy_title.pack(side="top")
        accuracy_container.pack(side="top")
        accuracy_value1 = Label(accuracy_container, text="Model 1:" + str(accuracy_model1), font=("Arial", 13), justify="left", bg="#e6e8eb")
        accuracy_value1.pack(side="top")
        accuracy_value2 = Label(accuracy_container, text="Model 2:" + str(accuracy_model2), font=("Arial", 13), justify="left", bg="#e6e8eb")
        accuracy_value2.pack(side="top")
        self.change_colors(accuracy_value1, accuracy_value2, accuracy_model1, accuracy_model2)
        elements1 = Frame(indicators, width=800, height=150)
        elements1.pack_propagate(False)
        sensitivity_container = Frame(elements1, width=350, height=150)
        sensitivity_container.pack_propagate(False)
        sensitivity_container.pack(side="left")
        sensitivity_title = Label(sensitivity_container, text="Czułość", font=("Arial", 15), justify="center")
        sensitivity_title.pack(side="top")
        sensitivity_values = Frame(sensitivity_container, width=350, height=150)
        sensitivity_values.pack_propagate(False)
        sensitivity_values.pack(side="top")
        sensitivity_value1 = Label(sensitivity_values, text="Model 1: " + str(sensitivity_model1), font=("Arial", 13), justify="left", bg="#e6e8eb")
        sensitivity_value1.pack(side="top")
        sensitivity_value2 = Label(sensitivity_values, text="Model 2: " + str(sensitivity_model2), font=("Arial", 13), justify="left", bg="#e6e8eb")
        sensitivity_value2.pack(side="top")
        self.change_colors(sensitivity_value1, sensitivity_value2, sensitivity_model1, sensitivity_model2)
        specificity_container = Frame(elements1, width=400, height=150)
        specificity_container.pack_propagate(False)
        specificity_container.pack(side="left")
        specificity_title = Label(specificity_container, text="Specyficzność", font=("Arial", 15), justify="center")
        specificity_title.pack(side="top")
        specificity_values = Frame(specificity_container, width=350, height=150)
        specificity_values.pack_propagate(False)
        specificity_values.pack(side="top")
        specificity_value1 = Label(specificity_values, text="Model 1: " + str(specificity_model1), font=("Arial", 13), justify="left", bg="#e6e8eb")
        specificity_value1.pack(side="top")
        specificity_value2 = Label(specificity_values, text="Model 2: " + str(specificity_model2), font=("Arial", 13), justify="left", bg="#e6e8eb")
        specificity_value2.pack(side="top")
        self.change_colors(specificity_value1, specificity_value2, specificity_model1, specificity_model2)
        elements1.pack(side="top")
        elements2 = Frame(indicators, width=800, height=150)
        elements2.pack_propagate(False)
        precision_container = Frame(elements2, width=350, height=150)
        precision_container.pack_propagate(False)
        precision_container.pack(side="left")
        precision_title = Label(precision_container, text="Precyzja", font=("Arial", 15), justify="center")
        precision_title.pack(side="top")
        precision_values = Frame(precision_container, width=350, height=150)
        precision_values.pack_propagate(False)
        precision_values.pack(side="top")
        precision_value1 = Label(precision_values, text="Model 1: " + str(precision_model1), font=("Arial", 13), justify="left", bg="#e6e8eb")
        precision_value1.pack(side="top")
        precision_value2 = Label(precision_values, text="Model 2: " + str(precision_model2), font=("Arial", 13), justify="left", bg="#e6e8eb")
        precision_value2.pack(side="top")
        self.change_colors(precision_value1,precision_value2, precision_model1, precision_model2)
        f1_container = Frame(elements2, width=400, height=150)
        f1_container.pack_propagate(False)
        f1_container.pack(side="left")
        f1_title = Label(f1_container, text="F1", font=("Arial", 15), justify="center")
        f1_title.pack(side="top")
        f1_values = Frame(f1_container, width=350, height=150)
        f1_values.pack_propagate(False)
        f1_values.pack(side="top")
        f1_value1 = Label(f1_values, text="Model 1: " + str(f1_model1), font=("Arial", 13), justify="left", bg="#e6e8eb")
        f1_value1.pack(side="top")
        f1_value2 = Label(f1_values, text="Model 2: " + str(f1_model2), font=("Arial", 13), justify="left", bg="#e6e8eb")
        f1_value2.pack(side="top")
        self.change_colors(f1_value1, f1_value2, f1_model1, f1_model2)
        elements2.pack(side="top")

    def change_colors(self, value1, value2, model1, model2):
        if model1 > model2:
            value1.config(fg="green")
            value2.config(fg="red")
        elif model1 < model2:
            value1.config(fg="red")
            value2.config(fg="green")



