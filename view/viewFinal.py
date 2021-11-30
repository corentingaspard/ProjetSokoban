from PyQt5 import Qt, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QIcon, QPainter, QPen, QBrush
from PyQt5.QtMultimedia import QSound

class viewF(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sokoban")
        self.setStyleSheet("background-color:black")
        self.setFixedSize(475, 550)
        self.__music = QSound("son/victoryFF.wav")
        self.__music.play()
        self.background()
        self.show()

    def background(self):
        self.__labelBF = QLabel(self)
        self.__labelBF.setGeometry(-550, 0, 1600, 1800)
        self.__labelBF.move(0,0)
        self.__labelBF.setStyleSheet("background-image:url(images/MainTheme/duran.jpg)")







