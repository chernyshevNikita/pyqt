# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calc(object):
    def setupUi(self, Calc):
        Calc.setObjectName("Calc")
        Calc.resize(322, 764)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        Calc.setFont(font)
        Calc.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(Calc)
        self.centralwidget.setObjectName("centralwidget")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(170, 210, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.clear.setFont(font)
        self.clear.setFlat(False)
        self.clear.setObjectName("clear")
        self.fact = QtWidgets.QPushButton(self.centralwidget)
        self.fact.setGeometry(QtCore.QRect(140, 210, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.fact.setFont(font)
        self.fact.setObjectName("fact")
        self.sqrt = QtWidgets.QPushButton(self.centralwidget)
        self.sqrt.setGeometry(QtCore.QRect(110, 210, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.sqrt.setFont(font)
        self.sqrt.setObjectName("sqrt")
        self.pow = QtWidgets.QPushButton(self.centralwidget)
        self.pow.setGeometry(QtCore.QRect(80, 210, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.pow.setFont(font)
        self.pow.setObjectName("pow")
        self.num0 = QtWidgets.QPushButton(self.centralwidget)
        self.num0.setGeometry(QtCore.QRect(80, 180, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.num0.setFont(font)
        self.num0.setObjectName("num0")
        self.point = QtWidgets.QPushButton(self.centralwidget)
        self.point.setGeometry(QtCore.QRect(110, 180, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.point.setFont(font)
        self.point.setObjectName("point")
        self.equal = QtWidgets.QPushButton(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(140, 180, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.equal.setFont(font)
        self.equal.setObjectName("equal")
        self.div = QtWidgets.QPushButton(self.centralwidget)
        self.div.setGeometry(QtCore.QRect(170, 180, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.div.setFont(font)
        self.div.setObjectName("div")
        self.multy = QtWidgets.QPushButton(self.centralwidget)
        self.multy.setGeometry(QtCore.QRect(170, 150, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.multy.setFont(font)
        self.multy.setObjectName("multy")
        self.num9 = QtWidgets.QPushButton(self.centralwidget)
        self.num9.setGeometry(QtCore.QRect(140, 150, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.num9.setFont(font)
        self.num9.setObjectName("num9")
        self.num8 = QtWidgets.QPushButton(self.centralwidget)
        self.num8.setGeometry(QtCore.QRect(110, 150, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.num8.setFont(font)
        self.num8.setObjectName("num8")
        self.num7 = QtWidgets.QPushButton(self.centralwidget)
        self.num7.setGeometry(QtCore.QRect(80, 150, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.num7.setFont(font)
        self.num7.setObjectName("num7")
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(170, 120, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.minus.setFont(font)
        self.minus.setObjectName("minus")
        self.num6 = QtWidgets.QPushButton(self.centralwidget)
        self.num6.setGeometry(QtCore.QRect(140, 120, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.num6.setFont(font)
        self.num6.setObjectName("num6")
        self.num5 = QtWidgets.QPushButton(self.centralwidget)
        self.num5.setGeometry(QtCore.QRect(110, 120, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.num5.setFont(font)
        self.num5.setObjectName("num5")
        self.num4 = QtWidgets.QPushButton(self.centralwidget)
        self.num4.setGeometry(QtCore.QRect(80, 120, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.num4.setFont(font)
        self.num4.setObjectName("num4")
        self.num1 = QtWidgets.QPushButton(self.centralwidget)
        self.num1.setGeometry(QtCore.QRect(80, 90, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.num1.setFont(font)
        self.num1.setObjectName("num1")
        self.num2 = QtWidgets.QPushButton(self.centralwidget)
        self.num2.setGeometry(QtCore.QRect(110, 90, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.num2.setFont(font)
        self.num2.setObjectName("num2")
        self.num3 = QtWidgets.QPushButton(self.centralwidget)
        self.num3.setGeometry(QtCore.QRect(140, 90, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.num3.setFont(font)
        self.num3.setObjectName("num3")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(170, 90, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.plus.setFont(font)
        self.plus.setObjectName("plus")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setEnabled(True)
        self.lcdNumber.setGeometry(QtCore.QRect(80, 50, 121, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        Calc.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calc)
        QtCore.QMetaObject.connectSlotsByName(Calc)

    def retranslateUi(self, Calc):
        _translate = QtCore.QCoreApplication.translate
        Calc.setWindowTitle(_translate("Calc", "RealCalk"))
        self.clear.setText(_translate("Calc", "C"))
        self.fact.setText(_translate("Calc", "!"))
        self.sqrt.setText(_translate("Calc", "???"))
        self.pow.setText(_translate("Calc", "^"))
        self.num0.setText(_translate("Calc", "0"))
        self.point.setText(_translate("Calc", "."))
        self.equal.setText(_translate("Calc", "="))
        self.div.setText(_translate("Calc", "/"))
        self.multy.setText(_translate("Calc", "*"))
        self.num9.setText(_translate("Calc", "9"))
        self.num8.setText(_translate("Calc", "8"))
        self.num7.setText(_translate("Calc", "7"))
        self.minus.setText(_translate("Calc", "-"))
        self.num6.setText(_translate("Calc", "6"))
        self.num5.setText(_translate("Calc", "5"))
        self.num4.setText(_translate("Calc", "4"))
        self.num1.setText(_translate("Calc", "1"))
        self.num2.setText(_translate("Calc", "2"))
        self.num3.setText(_translate("Calc", "3"))
        self.plus.setText(_translate("Calc", "+"))
