from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget,QScrollArea, QTableWidget, QVBoxLayout,QTableWidgetItem,QApplication
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QIcon
import pandas as pd


class ShowData(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('DATA')
        self.scroll = QScrollArea()
        self.layout = QVBoxLayout()
        self.table = QTableWidget()
        self.scroll.setWidget(self.table)
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)
        self.data = []  # pd.read_csv('../data_sets/HR_comma_sep.csv')
        self.show()

    def view_data(self, data):
        self.data = data
        self.table.setColumnCount(len(self.data.columns))
        self.table.setRowCount(len(self.data.index))
        self.table.setHorizontalHeaderLabels(self.data.columns)   # set columns name
        self.table.resizeColumnsToContents()                 # set Columns width as string len  on header columns
        for i in range(len(self.data.index)):
            for j in range(len(self.data.columns)):
                self.table.setItem(i, j, QTableWidgetItem(str(self.data.iloc[i,j])))


# #
# def main(data):
#     app = QApplication(sys.argv)  ### !!!!!!
#     view = ShowData()
#     view.view_data(data)
#     sys.exit(app.exec_())

