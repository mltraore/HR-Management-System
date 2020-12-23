import numpy as np
import pandas as pd
from pandasgui import show
from view_data import main
import matplotlib.pyplot as plt


class HRRetention:
    def __init__(self):
        self.data = []
        pass

    def load_data(self):
        self.data = pd.read_csv('../data_sets/HR_comma_sep.csv')

    def view_data(self):
        main(self.data)
        # print(self.data)
        # show(self.data)
        print(self.data.columns)

    def view_pie(self, col_name, labels):
        # Getting the count of desirable column
        col_count = self.data[col_name].value_counts()
        plt.pie(col_count, labels=labels)
        plt.show()

    def describe(self):
        # pass
        print(np.max(self.data['satisfaction_level']))

    def plot_per_column(self):
        pass









hr = HRRetention()
hr.load_data()
# hr.view_data()
# hr.view_pie('left',['not leave', 'leave'])
# hr.describe()
hr.view_pie('sales')
