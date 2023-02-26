import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QMainWindow
from name import Ui_Calc
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import operator

class RealCalkish(QMainWindow):
    def __init__(self):

        super(RealCalkish, self).__init__()
        self.ui = Ui_Calc()
        self.ui.setupUi(self)
        self.ui.num0.clicked.connect(lambda: self.write_digit('0'))
        self.ui.num1.clicked.connect(lambda: self.write_digit('1'))
        self.ui.num2.clicked.connect(lambda: self.write_digit('2'))
        self.ui.num3.clicked.connect(lambda: self.write_digit('3'))
        self.ui.num4.clicked.connect(lambda: self.write_digit('4'))
        self.ui.num5.clicked.connect(lambda: self.write_digit('5'))
        self.ui.num6.clicked.connect(lambda: self.write_digit('6'))
        self.ui.num7.clicked.connect(lambda: self.write_digit('7'))
        self.ui.num8.clicked.connect(lambda: self.write_digit('8'))
        self.ui.num9.clicked.connect(lambda: self.write_digit('9'))

    def write_digit(self, symbol: str) -> None:
        if self.ui.lcdNumber.text() == '0':
            self.ui.lcdNumber.setText(symbol)
        else:
            self.ui.lcdNumber.display(symbol)
            self.ui.lcdNumber.repaint()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RealCalkish()
    window.show()
    sys.exit(app.exec_())