from tkinter import Button, Frame, Label, Canvas

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
        self.page = None
        self.calculate_confusion_matrix(self.data["C50_PV"], 0)
        self.calculate_confusion_matrix(self.data["rf_PV"], 1)

    def create_button(self):
        button = Button(self.root, text="Klasyfikacyjny", command=lambda: self.start_rating())
        button.place(x=100, y=100)
        button.config(width=15, height=1)

    def start_rating(self):
        self.clear_container()
        self.page = 1
        button = Button(self.root, text="Następna strona", command=lambda: self.change_page())
        button.place(x=1320, y=720)
        button.config(width=15, height=1)
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

    def calculate_confusion_matrix(self, pre, index):
        true = self.data["income"]
        for i in range(len(pre)):
            if pre[i] == true[i]:
                if pre[i] == ">50K":
                    self.tp[index] = self.tp[index] + 1
                else:
                    self.tn[index] = self.tn[index] + 1
            else:
                if pre[i] == ">50K":
                    self.fp[index] = self.fp[index] + 1
                else:
                    self.fn[index] = self.fn[index] + 1

    def create_confusion_matrix(self,matrices, pre, index):
        real_index = index - 1
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
        label5 = Label(element5, width=81, font=("Arial", 15), text=self.tn[real_index], bg="#e6e8eb")
        label5.pack(expand=True)
        label6 = Label(element6, width=81, font=("Arial", 15), text=self.fp[real_index], bg="#e6e8eb")
        label6.pack(expand=True)
        label7 = Label(element8, width=81, font=("Arial", 15), text=self.fn[real_index], bg="#e6e8eb")
        label7.pack(expand=True)
        label8 = Label(element9, width=81, font=("Arial", 15), text=self.tp[real_index], bg="#e6e8eb")
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

    def roc_auc(self):
        title = Label(self.container, text="Krzywe ROC", font=("Arial", 30), justify="center")
        title.pack(side="top")
        container_roc = Frame(self.container, height=500)
        container_roc.pack_propagate(False)
        container_roc.pack(side="top", fill="x")
        self.create_roc(container_roc, 1, "C50_prob1")
        self.create_roc(container_roc, 2, "rf_prob1")

    def create_roc(self, container_roc, index, type):
        self.data = self.data.sort_values(by=type, ascending=False)
        roc = Frame(container_roc, height=500, width=500, bg="#e6e8eb")
        roc.pack_propagate(False)
        roc.pack(side="left", padx=100, pady=10)
        roc_title = Label(roc, text="Model " + str(index), font=("Arial", 20), justify="center", bg="#e6e8eb")
        roc_title.pack(side="top")
        chart_container = Frame(roc, height=400, width=400, bg="white")
        chart_container.pack_propagate(False)
        chart_container.pack(side="top")
        y_chart = Canvas(chart_container, height=400, width=50, bg="#e6e8eb", borderwidth=0, highlightthickness=0)
        y_chart.create_line(50, 0, 40, 0, fill="black")
        y_chart.create_line(50, 70, 40, 70, fill="black")
        y_chart.create_line(50, 140, 40, 140, fill="black")
        y_chart.create_line(50, 210, 40, 210, fill="black")
        y_chart.create_line(50, 280, 40, 280, fill="black")
        y_chart.create_line(50, 350, 40, 350, fill="black")
        y_chart.pack(side="left")
        y_chart100 = Label(chart_container, text="1.0", font=("Arial", 8), width=2, bg="#e6e8eb")
        y_chart100.place(x=20, y=2)
        y_chart80 = Label(chart_container, text="0.8", font=("Arial", 8), width=2, bg="#e6e8eb")
        y_chart80.place(x=20, y=72)
        y_chart60 = Label(chart_container, text="0.6", font=("Arial", 8), width=2, bg="#e6e8eb")
        y_chart60.place(x=20, y=142)
        y_chart40 = Label(chart_container, text="0.4", font=("Arial", 8), width=2, bg="#e6e8eb")
        y_chart40.place(x=20, y=212)
        y_chart20 = Label(chart_container, text="0.2", font=("Arial", 8), width=2, bg="#e6e8eb")
        y_chart20.place(x=20, y=282)
        y_chart0 = Label(chart_container, text="0.0", font=("Arial", 8), width=2, bg="#e6e8eb")
        y_chart0.place(x=20, y=342)
        x_chart_and_chart = Frame(chart_container, height=400, width=351)
        x_chart_and_chart.pack_propagate(False)
        x_chart_and_chart.pack(side="left")
        chart = Canvas(x_chart_and_chart, height=351, width=351, bg="#e6e8eb", borderwidth=0, highlightthickness=0)
        chart.create_line(0, 0, 0, 350, fill="#a6a6a6")
        chart.create_line(70, 0, 70, 350, fill="#a6a6a6")
        chart.create_line(140, 0, 140, 350, fill="#a6a6a6")
        chart.create_line(210, 0, 210, 350, fill="#a6a6a6")
        chart.create_line(280, 0, 280, 350, fill="#a6a6a6")
        chart.create_line(0, 70, 350, 70, fill="#a6a6a6")
        chart.create_line(0, 140, 350, 140, fill="#a6a6a6")
        chart.create_line(0, 210, 350, 210, fill="#a6a6a6")
        chart.create_line(0, 280, 350, 280, fill="#a6a6a6")
        chart.create_line(0, 350, 350, 350, fill="#a6a6a6")
        chart.pack_propagate(False)
        chart.pack(side="top")
        y_chart_title = Label(roc, text="Czułość", font=("Arial", 10), bg="#e6e8eb")
        y_chart_title.place(x=50, y=15)
        x_chart = Canvas(x_chart_and_chart, height=50, width=351, bg="#e6e8eb", borderwidth=0, highlightthickness=0)
        x_chart.create_line(0, 0, 0, 10, fill="black")
        x_chart.create_line(70, 0, 70, 10, fill="black")
        x_chart.create_line(140, 0, 140, 10, fill="black")
        x_chart.create_line(210, 0, 210, 10, fill="black")
        x_chart.create_line(280, 0, 280, 10, fill="black")
        x_chart.create_line(350, 0, 350, 10, fill="black", width=2)
        x_chart.pack_propagate(False)
        x_chart.pack(side="top")
        x_chart_title = Label(x_chart, text="1 - Specyficzność", font=("Arial", 10), justify="center", bg="#e6e8eb")
        x_chart_title.pack(side="bottom")
        x_chart0 = Label(chart_container, text="0.0", font=("Arial", 8), width=2, bg="#e6e8eb")
        x_chart0.place(x=30, y=360)
        x_chart20 = Label(chart_container, text="0.2", font=("Arial", 8), width=2, bg="#e6e8eb")
        x_chart20.place(x=100, y=360)
        x_chart40 = Label(chart_container, text="0.4", font=("Arial", 8), width=2, bg="#e6e8eb")
        x_chart40.place(x=170, y=360)
        x_chart60 = Label(chart_container, text="0.6", font=("Arial", 8), width=2, bg="#e6e8eb")
        x_chart60.place(x=240, y=360)
        x_chart80 = Label(chart_container, text="0.8", font=("Arial", 8), width=2, bg="#e6e8eb")
        x_chart80.place(x=310, y=360)
        x_chart100 = Label(chart_container, text="1.0", font=("Arial", 8), width=2, bg="#e6e8eb")
        x_chart100.place(x=380, y=360)
        threshold = self.data[type].iloc[0]
        true_0, true_1 = self.calculate_true_count()
        start_index = 0
        tp = 0
        fp = 0
        len_data = len(self.data[type])
        x0 = 0
        y0 = 350
        xp0 = 0
        yp0 = 0
        auc = 0
        for i in range(len_data):
            if self.data[type].iloc[i] != threshold or i == len_data-1:
                threshold = self.data[type].iloc[i]
                tp, fp = self.calculate_predicted_positive_count(start_index, i + 1, tp, fp)
                start_index = i + 1
                xp1, yp1 = self.calculate_false_positive_rate_and_sensitivity(true_0, true_1, tp, fp)
                x1, y1 = self.calculate_point(xp1, yp1)
                chart.create_line(x0, y0, x1, y1, fill="orange")
                auc += ((yp1 + yp0) * (xp1 - xp0)/2)
                xp0, yp0 = xp1, yp1
                x0, y0 = x1, y1
        auc = Label(roc, text="AUC: " + str(auc), font=("Arial", 13), justify="right", bg="#e6e8eb")
        auc.pack(side="top", anchor="ne")

    def calculate_true_count(self):
        true_0 = 0
        true_1 = 0
        for income in self.data["income"]:
            if income == ">50K":
                true_1 +=1
            else:
                true_0 +=1
        return true_0, true_1

    def calculate_predicted_positive_count(self, start_index, stop_index, tp, fp):
        for i in range(start_index, stop_index):
            if self.data["income"].iloc[i] == ">50K":
                tp +=1
            else:
                fp +=1
        return tp, fp

    def calculate_false_positive_rate_and_sensitivity(self, true_0, true_1, tp, fp):
        return fp/true_0, tp/true_1

    def calculate_point(self, xp, yp):
        return int(350*xp), int(350 - (350*yp))

    def change_colors(self, value1, value2, model1, model2):
        if model1 > model2:
            value1.config(fg="green")
            value2.config(fg="red")
        elif model1 < model2:
            value1.config(fg="red")
            value2.config(fg="green")

    def change_page(self):
        if self.page == 1:
            self.page = 2
            self.clear_container()
            self.roc_auc()
        else:
            self.page = 1
            self.clear_container()
            self.start_rating()

    def clear_container(self):
        for children in self.container.winfo_children():
            children.destroy()



