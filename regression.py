import math
import numpy as np
from math import sqrt
from tkinter import Button, Frame, Label, Canvas

from matplotlib import pyplot as plt
from networkx.algorithms.operators.binary import difference
from numpy.core.defchararray import center
from scipy.stats import norm


class Regression:
    def __init__(self, container, root, data, button):
        self.root = root
        self.data = data
        self.container=container
        self.create_button()
        self.differences1 = []
        self.differences2 = []
        self.calculate_differences(self.data["przewidywana1"], self.data["przewidywana2"])
        self.button = button
        self.page = 1

    def create_button(self):
        button = Button(self.root, text="Regresyjny", command=lambda: self.start_rating())
        button.place(x=250, y=100)
        button.config(width=15, height=1)



    def start_rating(self):
        self.clear_container()
        self.page = 1
        self.button.config(command=lambda: self.change_page(), text="Histogramy")
        self.button.place(x=1320, y=720)
        mae1 = self.calculate_mae(True)
        mae2 = self.calculate_mae(False)
        mse1 = self.calculate_mse(True)
        mse2 = self.calculate_mse(False)
        rmse1 = self.calculate_rmse(mse1)
        rmse2 = self.calculate_rmse(mse2)
        mape1, equal1_0 = self.calculate_mape(True)
        mape2, equal2_0 = self.calculate_mape(False)
        mae_mape_container = Frame(self.container, height=250)
        mae_mape_container.pack_propagate(False)
        mae_mape_container.pack(side="top", fill="x", pady=30, padx=50)
        mae_container = Frame(mae_mape_container, height=250, width=616)
        mae_container.pack_propagate(False)
        mae_container.pack(side="left")
        mae_title = Label(mae_container, text="MAE", font=("Arial", 20))
        mae_title.pack(side="top", fill="x")
        mae_values = Frame(mae_container, height=120, width=350, bg="#e6e8eb")
        mae_values.pack_propagate(False)
        mae_values.pack(side="top")
        mae_value1 = Label(mae_values, text="Model 1: " + str(mae1), font=("Arial", 15), bg="#e6e8eb")
        mae_value1.pack(side="top")
        mae_value2 = Label(mae_values, text="Model 2: " + str(mae2), font=("Arial", 15), bg="#e6e8eb")
        mae_value2.pack(side="top")
        self.change_colors(mae_value1, mae_value2, mae1, mae2)
        mape_container = Frame(mae_mape_container, height=250, width=616)
        mape_container.pack_propagate(False)
        mape_container.pack(side="left")
        mape_title = Label(mape_container, text="MAPE", font=("Arial", 20))
        mape_title.pack(side="top", fill="x")
        mape_values = Frame(mape_container, height=120, width=350, bg="#e6e8eb")
        mape_values.pack_propagate(False)
        mape_values.pack(side="top")
        mape_value1 = Label(mape_values, text="Model 1: " + str(mape1) + '%', font=("Arial", 15), bg="#e6e8eb")
        mape_value1.pack(side="top")
        if equal1_0:
            warning1 = Label(mape_values, text="Niektóre wartości yi były bliskie lub równe 0", font=("Arial", 15), bg="#e6e8eb")
            warning1.pack(side="top")
        mape_value2 = Label(mape_values, text="Model 2: " + str(mape2) +'%', font=("Arial", 15), bg="#e6e8eb")
        if equal2_0:
            warning2 = Label(mape_values, text="Niektóre wartości yi były bliskie lub równe 0", font=("Arial", 15), bg="#e6e8eb")
            warning2.pack(side="top")
        mape_value2.pack(side="top")
        self.change_colors(mape_value1, mape_value2, mape1, mape2)
        mse_rmse_container = Frame(self.container, height=250)
        mse_rmse_container.pack_propagate(False)
        mse_rmse_container.pack(side="top", fill="x", padx=50)
        mse_container = Frame(mse_rmse_container, height=250, width=616)
        mse_container.pack_propagate(False)
        mse_container.pack(side="left")
        mse_title = Label(mse_container, text="MSE", font=("Arial", 20))
        mse_title.pack(side="top", fill="x")
        mse_values = Frame(mse_container, height=120, width=350, bg="#e6e8eb")
        mse_values.pack_propagate(False)
        mse_values.pack(side="top")
        mse_value1 = Label(mse_values, text="Model 1: " + str(mse1), font=("Arial", 15), bg="#e6e8eb")
        mse_value1.pack(side="top")
        mse_value2 = Label(mse_values, text="Model 2: " + str(mse2), font=("Arial", 15), bg="#e6e8eb")
        mse_value2.pack(side="top")
        self.change_colors(mse_value1, mse_value2, mse1, mse2)
        rmse_container = Frame(mse_rmse_container, height=250, width=616)
        rmse_container.pack_propagate(False)
        rmse_container.pack(side="left")
        rmse_title = Label(rmse_container, text="RMSE", font=("Arial", 20))
        rmse_title.pack(side="top", fill="x")
        rmse_values = Frame(rmse_container, height=120, width=350, bg="#e6e8eb")
        rmse_values.pack_propagate(False)
        rmse_values.pack(side="top")
        rmse_value1 = Label(rmse_values, text="Model 1: " + str(rmse1), font=("Arial", 15), bg="#e6e8eb")
        rmse_value1.pack(side="top")
        rmse_value2 = Label(rmse_values, text="Model 2: " + str(rmse2), font=("Arial", 15), bg="#e6e8eb")
        rmse_value2.pack(side="top")
        self.change_colors(rmse_value1, rmse_value2, rmse1, rmse2)

    def calculate_differences(self, pre1, pre2):
        for i in range(len(pre1)):
            self.differences1.append(self.data["rzeczywista"][i] - pre1[i])
        for i in range(len(pre2)):
            self.differences2.append(self.data["rzeczywista"][i] - pre2[i])

    def calculate_mae(self, type):
        mae = 0
        if type:
            for diff in self.differences1:
                mae += abs(diff)
        else:
            for diff in self.differences2:
                mae += abs(diff)
        return mae / len(self.data["rzeczywista"])

    def calculate_mse(self, type):
        mse = 0
        if type:
            for diff in self.differences1:
                mse += diff**2
        else:
            for diff in self.differences2:
                mse += diff**2
        return mse / len(self.data["rzeczywista"])

    def calculate_rmse(self, mse):
        return sqrt(mse)

    def calculate_mape(self, type):
        equal_0 = False
        len_data = len(self.data["rzeczywista"])
        mape = 0
        for i in range(len_data):
            yi = self.data["rzeczywista"][i]
            if yi < 0.000001:
                equal_0 = True
                continue
            if type:
                mape += (abs(self.differences1[i]))/yi
            else:
                mape += (abs(self.differences2[i]))/yi
        return (mape / len_data) * 100, equal_0

    def hist(self):
        title = Label(self.container, text="Histogramy", font=("Arial", 20), justify="center")
        title.pack(side="top")
        container_hist = Frame(self.container, height=500)
        container_hist.pack_propagate(False)
        container_hist.pack(side="top", fill="x")
        self.create_hist(container_hist, 1, self.differences1)
        padding = Label(container_hist, width=10)
        padding.pack(side="left")
        self.create_hist(container_hist, 2, self.differences2)

    def create_hist(self, container_hist, index, differences):
        hist = Frame(container_hist, width=620, height=500)
        hist.pack_propagate(False)
        hist.pack(side="left")
        hist_title = Label(hist, text="Model " + str(index), font=("Arial", 15))
        hist_title.pack(side="top", fill="x")
        chart_container = Frame(hist, height=470)
        chart_container.pack_propagate(False)
        chart_container.pack(side="top", fill="x")
        y_chart = Canvas(chart_container, width=50, borderwidth=0, highlightthickness=0)
        y_chart.pack_propagate(False)
        y_chart.pack(side="left", fill="y")
        y_chart.create_line(50, 0, 40, 0, fill="black")
        y_chart.create_line(50, 35, 40, 35, fill="black")
        y_chart.create_line(50, 70, 40, 70, fill="black")
        y_chart.create_line(50, 105, 40, 105, fill="black")
        y_chart.create_line(50, 140, 40, 140, fill="black")
        y_chart.create_line(50, 175, 40, 175, fill="black")
        y_chart.create_line(50, 210, 40, 210, fill="black")
        y_chart.create_line(50, 245, 40, 245, fill="black")
        y_chart.create_line(50, 280, 40, 280, fill="black")
        y_chart.create_line(50, 315, 40, 315, fill="black")
        y_chart.create_line(50, 350, 40, 350, fill="black")
        y_chart.create_line(50, 385, 40, 385, fill="black")
        y_chart.create_line(50, 420, 40, 420, fill="black")
        x_chart_and_chart = Frame(chart_container, width=571)
        x_chart_and_chart.pack_propagate(False)
        x_chart_and_chart.pack(side="left", fill="y")
        chart = Canvas(x_chart_and_chart, height=421, borderwidth=0, highlightthickness=0)
        chart.pack(side="top", fill="x")
        chart.create_line(0, 420, 550, 420, fill="#a6a6a6")
        chart.create_line(0, 385, 550, 385, fill="#a6a6a6")
        chart.create_line(0, 350, 550, 350, fill="#a6a6a6")
        chart.create_line(0, 315, 550, 315, fill="#a6a6a6")
        chart.create_line(0, 280, 550, 280, fill="#a6a6a6")
        chart.create_line(0, 245, 550, 245, fill="#a6a6a6")
        chart.create_line(0, 210, 550, 210, fill="#a6a6a6")
        chart.create_line(0, 175, 550, 175, fill="#a6a6a6")
        chart.create_line(0, 140, 550, 140, fill="#a6a6a6")
        chart.create_line(0, 105, 550, 105, fill="#a6a6a6")
        chart.create_line(0, 70, 550, 70, fill="#a6a6a6")
        chart.create_line(0, 35, 550, 35, fill="#a6a6a6")
        x_chart = Canvas(x_chart_and_chart, height=50, borderwidth=0, highlightthickness=0)
        x_chart.pack(side="top", fill="x")
        bins = math.ceil(1 + math.log2(len(differences))) + 2
        inc = int(550 / bins)
        bound, inc_data = self.calculate_inc_data(differences, bins - 2)
        bin_width = inc_data
        bound -= inc_data
        first = True
        left_bound = None
        right_bound = None
        count = []
        min_bound = bound
        max_bound = None
        for i in range(bins + 1):
            if not first:
                right_bound = bound
                count.append(self.find_count_at_range(differences, left_bound, right_bound))
            else:
                first = False
            left_bound = bound
            number = Label(x_chart, text=str(bound), font=("Arial", 10))
            number.place(x=i * inc, y=10)
            bound += inc_data
        max_bound = bound - inc_data
        _, inc_data = self.calculate_inc_data(count, 12)
        bound = 0
        for i in range(13):
            number = Label(y_chart, text=str(bound), font=("Arial", 10))
            number.place(x=20, y=(425 - i*35))
            bound += inc_data
        x1_point = 0
        x2_point = 0
        max_bound_y = bound - inc_data;
        for i in count:
            x2_point += inc
            chart.create_rectangle(x1_point, 421, x2_point, 421 - (i*420/max_bound_y), fill="purple")
            x1_point = x2_point
        x_point = 0
        for i in range(bins + 1):
            chart.create_line(x_point, 0, x_point, 420, fill="#a6a6a6")
            x_chart.create_line(x_point, 0, x_point, 10, fill="black")
            x_point += inc
        self.create_normal_curve(differences, chart, min_bound, max_bound, max_bound_y, bin_width)

    def create_normal_curve(self, data, chart, min_bound, max_bound, max_bound_y, bin_width):
        std = np.std(data)
        mean = np.mean(data)
        print(std)
        print(mean)
        inc_x = 570/abs(max_bound - min_bound)
        inc_y = 420/max_bound_y
        print(data)
        x1_point = 0
        y1_point = 0
        for x in range(min_bound, max_bound + 1):
            y = (1/(std*sqrt(2*math.pi)))*math.e**(-(x - mean)**2/(2*std**2))
            y2_point = y * len(data) * bin_width * inc_y
            x2_point = x1_point + inc_x
            #print(y1_point)
            #print(y2_point)
            #print(y)
            #print("p1 : ", int(x1_point), 420 - int(y1_point))
            #print("p1 : ", int(x2_point), 420 - int(y2_point))
            chart.create_line(int(x1_point), 420 - int(y1_point), int(x2_point), 420 - int(y2_point), fill="orange")
            y1_point = y2_point
            x1_point = x2_point


    def calculate_inc_data(self, data, bins):
        min_data = min(data)
        inc_data = math.ceil((abs(max(data) - min_data))/bins)
        return math.ceil(min_data), inc_data

    def find_count_at_range(self, differences, left_bound, right_bound):
        count = 0
        for diff in differences:
            if left_bound <= diff < right_bound:
                count += 1
        return count



    def change_colors(self, value1, value2, model1, model2):
        if model1 < model2:
            value1.config(fg="green")
            value2.config(fg="red")
        elif model1 > model2:
            value1.config(fg="red")
            value2.config(fg="green")

    def change_page(self):
        if self.page == 1:
            self.page = 2
            self.clear_container()
            self.button.config(text="Ocena jakości")
            self.hist()
        else:
            self.page = 1
            self.clear_container()
            self.start_rating()

    def clear_container(self):
        for children in self.container.winfo_children():
            children.destroy()
