# -*- coding: utf-8 -*-
#  модуль генерирущий интерфейс и его элементы


from PyQt5 import QtCore, QtGui, QtWidgets
from pltwidget import DecardWidget, PolarWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 532)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        # виджет декартовой системы
        self.decard_label = DecardWidget(self.centralwidget)
        self.decard_label.setGeometry(QtCore.QRect(10, 10, 500, 500))
        self.decard_label.setObjectName("decard_label")

        # виджет полярной системы
        self.polar_label = PolarWidget(self.centralwidget)
        self.polar_label.setGeometry(QtCore.QRect(10, 10, 500, 500))
        self.polar_label.setObjectName("polar_label")

        # РадиоКнопки
        self.decard = QtWidgets.QRadioButton(self.centralwidget)
        self.decard.setGeometry(QtCore.QRect(520, 10, 141, 41))
        self.decard.setChecked(True)
        self.decard.setObjectName("decard")
        self.polar = QtWidgets.QRadioButton(self.centralwidget)
        self.polar.setGeometry(QtCore.QRect(520, 40, 141, 41))
        self.polar.setObjectName("polar")

        # Элементы для ввода значений
        self.radiusName = QtWidgets.QLabel(self.centralwidget)
        self.radiusName.setGeometry(QtCore.QRect(550, 130, 41, 21))
        self.radiusName.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.radiusName.setObjectName("radiusName")
        self.offsetName = QtWidgets.QLabel(self.centralwidget)
        self.offsetName.setGeometry(QtCore.QRect(520, 163, 71, 21))
        self.offsetName.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.offsetName.setObjectName("offsetName")
        self.radiusBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.radiusBox.setGeometry(QtCore.QRect(600, 127, 51, 26))
        self.radiusBox.setDecimals(1)
        self.radiusBox.setMinimum(0.1)
        self.radiusBox.setMaximum(10.0)
        self.radiusBox.setSingleStep(0.5)
        self.radiusBox.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.radiusBox.setProperty("value", 3.0)
        self.radiusBox.setObjectName("radiusBox")
        self.offsetBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.offsetBox.setGeometry(QtCore.QRect(600, 160, 51, 26))
        self.offsetBox.setDecimals(1)
        self.offsetBox.setMinimum(0.0)
        self.offsetBox.setSingleStep(0.1)
        self.offsetBox.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.offsetBox.setProperty("value", 2.0)
        self.offsetBox.setObjectName("offsetBox")


        #Кнопка "Обновить"
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 200, 111, 23))
        self.pushButton.setObjectName("pushButton")

        #Кнопка "Анимация"
        self.aniButton = QtWidgets.QPushButton(self.centralwidget)
        self.aniButton.setGeometry(QtCore.QRect(540, 240, 111, 23))
        self.aniButton.setObjectName("aniButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # отображаемые имена элементов
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Архимедова спираль"))
        self.decard.setText(_translate("MainWindow", "Decard"))
        self.polar.setText(_translate("MainWindow", "Polar"))
        self.radiusName.setText(_translate("MainWindow", "Радиус"))
        self.offsetName.setText(_translate("MainWindow", "Шаг спирали"))
        self.pushButton.setText(_translate("MainWindow", "Обновить график"))
        self.aniButton.setText(_translate("MainWindow", "Анимация"))
