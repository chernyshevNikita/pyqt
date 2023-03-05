import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QMainWindow
from name import Ui_Calc
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import operator
nums = ['0','1','2','3','4','5','6','7','8','9']

class RealCalkish(QMainWindow, Ui_Calc):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.num0.clicked.connect(lambda: self.write_digit())
        self.num1.clicked.connect(lambda: self.write_digit())
        self.num2.clicked.connect(lambda: self.write_digit())
        self.num3.clicked.connect(lambda: self.write_digit())
        self.num4.clicked.connect(lambda: self.write_digit())
        self.num5.clicked.connect(lambda: self.write_digit())
        self.num6.clicked.connect(lambda: self.write_digit())
        self.num7.clicked.connect(lambda: self.write_digit())
        self.num8.clicked.connect(lambda: self.write_digit())
        self.num9.clicked.connect(lambda: self.write_digit())
        self.clear.clicked.connect(lambda : self.clear_all())
        self.point.clicked.connect(lambda : self.add_point())
        self.plus.clicked.connect(lambda: self.operation_plus())
        self.minus.clicked.connect(lambda: self.operation_minus())
        self.multy.clicked.connect(lambda: self.operation_multyply())
        self.div.clicked.connect(lambda: self.operation_div())
        self.pow.clicked.connect(lambda: self.operation_pow())
        self.equal.clicked.connect(lambda: self.equation())
        self.Num = 0
        self.a = 0
        self.b = False
        self.last_operation = ''

    def write_digit(self):

        if self.b == False:
            btn = int(self.sender().text())
            self.Num = self.Num * 10 + btn
            self.lcdNumber.display(str(self.Num))
        else:
            self.Num = 0
            btn = int(self.sender().text())
            self.Num = self.Num * 10 + btn
            self.lcdNumber.display(str(self.a)+self.last_operation+str(self.Num))
            self.b = False


    def clear_all(self):
        self.lcdNumber.display('0')
        self.b = False
        self.Num = 0

    def add_point(self):
        if self.sender().text() == ".":
            self.lcdNumber.display(str(self.Num) + '.')
    def operation_plus(self):
        if self.sender().text() == "+":
            self.a = self.Num
            self.last_operation = '+'
            self.lcdNumber.display(str(self.Num) + '+')
            self.b = True
    def operation_minus(self):
        if self.sender().text() == "-":
            self.a = self.Num
            self.last_operation = '-'
            self.lcdNumber.display(str(self.Num) + '-')
            self.b = True
    def operation_multyply(self):
        if self.sender().text() == "*":
            self.a = self.Num
            self.last_operation = '*'
            self.lcdNumber.display(str(self.Num) + '*')
            self.b = True
    def operation_div(self):
        if self.sender().text() == "/":
            self.a = self.Num
            self.last_operation = '/'
            self.lcdNumber.display(str(self.Num) + '/')
            self.b = True
    def operation_pow(self):
        if self.sender().text() == "^":
            self.a = self.Num
            self.last_operation = '^'
            self.lcdNumber.display(str(self.Num) + '^')
            self.b = True
    def equation(self):
        if self.sender().text() == "=":
            eq = eval(str(self.a)+self.last_operation+str(self.Num))
            print(eq)
            self.lcdNumber.display(str(eq))
            self.Num = eq

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RealCalkish()
    window.show()
    sys.exit(app.exec_())
