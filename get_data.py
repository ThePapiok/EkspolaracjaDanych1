from tkinter import messagebox
from tkinter.filedialog import askopenfile

from spyder_kernels.utils.lazymodules import pandas

from classification import Classification
from regression import Regression


def get_data_from_files(container, root):
    classification_data = None
    regression_data = None
    while True:
        file = askopenfile(
            title='Wczytaj model regresyjny',
            filetypes=([("csv", "*.csv")])
        )
        if file:
            regression_data = pandas.read_csv(file, sep=",", header=0)
            if len(regression_data.columns) == 3:
                break
            else:
                messagebox.showwarning("Ostrzeżenie", "To nie model regresyjny, spróbuj ponownie")
        else:
            return
    while True:
        file = askopenfile(
            title='Wczytaj model klasyfikacjny',
            filetypes=([("csv", "*.csv")])
        )
        if file:
            classification_data = pandas.read_csv(file, sep=",", header=0)
            if len(classification_data.columns) == 5:
                break
            else:
                messagebox.showwarning("Ostrzeżenie", "To nie model klasyfikacyjny, spróbuj ponownie")
        else:
            return
    Classification(container, root, classification_data)
    Regression(container, root, regression_data)
