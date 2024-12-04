from math import sqrt
from tkinter import Button, Frame, Label

class Regression:
    def __init__(self, container, root, data):
        self.root = root
        self.data = data
        self.container=container
        self.create_button()
        self.differences1 = []
        self.differences2 = []
        self.calculate_differences(self.data["przewidywana1"], self.data["przewidywana2"])

    def create_button(self):
        button = Button(self.root, text="Regresyjny", command=lambda: self.start_rating())
        button.place(x=250, y=100)
        button.config(width=15, height=1)



    def start_rating(self):
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


    def change_colors(self, value1, value2, model1, model2):
        if model1 > model2:
            value1.config(fg="green")
            value2.config(fg="red")
        elif model1 < model2:
            value1.config(fg="red")
            value2.config(fg="green")
