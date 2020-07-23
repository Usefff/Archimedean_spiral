# импорт необходимых библиотек
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import matplotlib

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.animation import TimedAnimation
from matplotlib.lines import Line2D
import matplotlib.animation as animation
from matplotlib.collections import LineCollection
import gui


# определение класса, отвечающего за взаимодействие с графическим интерфейсом
class MainWindow(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('arh.png'))
        self.decard_label.hide()  # скрываем виджет декартовой системы
        self.polar_label.hide()  # скрываем виджет полярной системы

        # вводим переменные
        self.flag_decard = 0  # флаг декартовой системы
        self.flag_polar = 0  # флаг полярной системы
        self.breaker = 0  # флаг анимации
        self.x = []  # данные по оси Х
        self.y = []  # данные по оси Y

        # связываем функции и элементы интерфейса
        self.polar.toggled.connect(self.OnClickButton)
        self.decard.toggled.connect(self.OnClickButton)
        self.radius = self.radiusBox.value()  # вводим в переменную данные из поля "Радиус"
        self.offset = self.offsetBox.value()  # вводим в переменную данные из поля "Смещение"
        self.pushButton.clicked.connect(self.renew_graph)  # привязываем функцию к кнопке "Обновить график"
        self.aniButton.clicked.connect(self.animation_start)  # привязываем функцию к кнопке "Анимация"

        # отрисовываем кривую при старте программы
        self.renew_graph()

    # Функция анимации
    def animation_start(self):
        self.renew_graph()
        self.breaker = 0
        # старт анимации в декартовой системе
        if self.decard.isChecked():
            # отрисовываем точку
            self.scat_decard = self.decard_label.canvas.decard.scatter([], [], s=50, c='r', zorder=3)
            # запускаем анимацию
            ani = animation.FuncAnimation(self.decard_label.fig, self.update_decard, frames=len(self.x), interval=0.5,
                                          blit=True, repeat=False)

        # старт анимации в полярной системе
        else:
            self.scat_polar = self.polar_label.canvas.polar.scatter([], [], s=50, c='r', zorder=3)
            ani = animation.FuncAnimation(self.polar_label.fig, self.update_polar, frames=len(self.x), interval=2,
                                          blit=True, repeat=False)

    # функция обновления координат анимации полярной системы
    def update_polar(self, frame):
        while self.breaker == 0:
            self.scat_polar.set_offsets([self.x[frame], self.y[frame]])
            return self.scat_polar,

    # функция обновления координат анимации декартовой системы
    def update_decard(self, frame):
        while self.breaker == 0:
            self.scat_decard.set_offsets([self.x[frame], self.y[frame]])
            return self.scat_decard,

    # Функция обновления графика с новыми параметрами
    def renew_graph(self):
        self.breaker = 1
        # определяем график какой из систем обновлять, в зависимости от активной радиокнопки
        if self.decard.isChecked():
            self.decard_draw(self.radiusBox.value(), self.offsetBox.value())
        else:
            self.polar_draw(self.radiusBox.value(), self.offsetBox.value())

    # Функция реакции при переключении радиокнопок
    def OnClickButton(self):
        radio_btn = self.sender()
        # запускаем отрисовку графика, в зависимости от переключенной радиокнопки
        if radio_btn.isChecked():
            if radio_btn.objectName() == 'polar':
                self.polar_draw(self.radiusBox.value(), self.offsetBox.value())
            elif radio_btn.objectName() == 'decard':
                self.decard_draw(self.radiusBox.value(), self.offsetBox.value())

    # Функция отрисовки кривой в полярной системе координат
    def polar_draw(self, radius, offset):

        if self.flag_polar == 0:
            self.polar_label.show()  # отображаем виджет полярной системы
            self.decard_label.hide()  # скрываем виджет декартовой системы
            self.decard_label.canvas.decard.clear()  # очищаем декарт. кривую

        elif self.flag_polar == 1:
            self.polar_label.canvas.polar.clear()  # очищаем полярн. кривую

        r = np.arange(0, radius, 0.001)  # генерируем координаты Y
        theta = offset * np.pi * r  # генерируем координаты X

        self.x = theta
        self.y = r

        # определяем, сколько радиальных осей отображать, в зависимости от радиуса, с шагом 0.5
        rticks = []
        for i in range(int(radius)):
            rticks.append(i)
            rticks.append(i + 0.5)

        self.polar_label.canvas.polar.plot(theta, r)  # отрисовывем кривую
        self.polar_label.canvas.polar.set_rticks(rticks)  # отрисовываем радиальные оси
        self.polar_label.canvas.polar.set_rmax(radius)  # устанавливаем максимальный отоброжаемый радиус
        self.polar_label.canvas.polar.set_rlabel_position(-25)  # отодвигаем метки от границы графика

        self.polar_label.canvas.draw()  # выводим график на виджет

        # переключаем флаги
        self.flag_polar = 1
        self.flag_decard = 0
        self.breaker = 0

    # Функция отрисовки кривой в декартовой системе координат
    def decard_draw(self, radius, offset):

        if self.flag_decard == 0:
            self.decard_label.show()  # отображаем виджет декартовой системы
            self.polar_label.hide()  # скрываем виджет полярной системы
            self.polar_label.canvas.polar.clear()  # очищаем полярн. кривую

        elif self.flag_decard == 1:
            self.decard_label.canvas.decard.clear()  # очищаем декарт. кривую

        self.decard_label.canvas.decard.grid(color='black', linewidth=0.3)  # отрисовываем сетку координат

        r = np.arange(0, radius, 0.001)
        theta = offset * np.pi * r
        xoffset, yoffset = 0, 0
        yy = 1 * r * np.sin(theta) + yoffset  # генерируем координаты Y

        xx = r * np.cos(theta) + xoffset  # генерируем координаты X

        spiral = zip(xx, yy)  # упаковываем массивы с координатами

        self.x = xx
        self.y = yy

        self.collection = LineCollection([list(spiral)], colors='orange')  # отрисовываем кривую

        # выставляем центральные осевые линии и координаты
        self.decard_label.canvas.decard.spines['left'].set_position('zero')
        self.decard_label.canvas.decard.spines['right'].set_color('none')
        self.decard_label.canvas.decard.spines['bottom'].set_position('zero')
        self.decard_label.canvas.decard.spines['top'].set_color('none')
        self.decard_label.canvas.decard.xaxis.set_ticks_position('bottom')
        self.decard_label.canvas.decard.yaxis.set_ticks_position('left')
        self.decard_label.canvas.decard.add_collection(self.collection)

        # выставляем лимиты по отображению графика, в зависимости от значения "Радиус"
        self.decard_label.canvas.decard.set_xlim(-radius, radius)
        self.decard_label.canvas.decard.set_ylim(-radius, radius)
        self.decard_label.canvas.decard.tick_params(axis='x', colors='darkblue')
        self.decard_label.canvas.decard.tick_params(axis='y', colors='darkblue')

        self.decard_label.canvas.draw()  # выводим график на виджет

        # переключаем флаги
        self.breaker = 0
        self.flag_decard = 1
        self.flag_polar = 0

    # Функция масштабирования объектов, при изменении размеров окна
    def resizeEvent(self, event):
        self.decard_label.resize(self.width() - 180, self.height() - 20)
        self.polar_label.resize(self.width() - 180, self.height() - 20)
        self.decard.setGeometry(QtCore.QRect(self.width() - 150, 10, 141, 41))
        self.polar.setGeometry(QtCore.QRect(self.width() - 150, 40, 141, 41))
        self.offsetName.setGeometry(QtCore.QRect(self.width() - 170, 163, 71, 21))
        self.offsetBox.setGeometry(QtCore.QRect(self.width() - 90, 160, 51, 26))
        self.radiusName.setGeometry(QtCore.QRect(self.width() - 140, 130, 41, 21))
        self.radiusBox.setGeometry(QtCore.QRect(self.width() - 90, 127, 51, 26))
        self.pushButton.setGeometry(QtCore.QRect(self.width() - 150, 200, 111, 23))
        self.aniButton.setGeometry(QtCore.QRect(self.width() - 150, 240, 111, 23))


# Создание экземпляра класса MainWindow и запуск приложения
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()  # создаем экземпляр класса
    window.show()  # запускаем приложение

    sys.exit(app.exec_())
