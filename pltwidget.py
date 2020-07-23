from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib import pyplot as plt
from matplotlib.figure import Figure


# класс создающий связывающий декартовый виджет и фигуру декартовой системы от матплота
class DecardWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.fig = Figure()
        self.canvas = FigureCanvasQTAgg(self.fig)
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.canvas.decard = self.canvas.figure.add_subplot(111)
        plt.style.use('Solarize_Light2')
        self.setLayout(vertical_layout)


# класс создающий и связывающий полярный виджет и фигуру полярной системы от матплота
class PolarWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.fig = Figure()
        self.canvas = FigureCanvasQTAgg(self.fig)
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.canvas.polar = self.canvas.figure.add_subplot(111, projection='polar')
        plt.style.use('Solarize_Light2')
        self.setLayout(vertical_layout)
