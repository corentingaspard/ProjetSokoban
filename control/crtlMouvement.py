from PyQt5 import Qt, QtCore
from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QIcon, QPainter, QPen
from PyQt5.QtMultimedia import QSound
from view.gridView import *

class crtlMouvement(QWidget):
    def __init__(self):
        super().__init__()
        self.__y = 500
        self.__i = 500
        self.__views = []
        self.__model = None
        self.__controller = None
        self.__view =None
        self.__son = QSound("son/minecraft_click.wav")
        self.__son2 = QSound("son/quack.wav")
        self.__son3 = QSound("son/Sonic-ring-sound-effect.wav")


    def setModel(self,model):
        self.__model = model
    def getModel(self):
        return self.__model
    def setController(self, controller):
        self.__controller = controller
    def getController(self):
        return self.__controller
    def setView (self,view):
        self.__view = view
    def getView (self):
        return self.__view

    def checkD(self,a,b):
        move = False
        plateau = self.__model.getPlateau()
        if(plateau[a][b+1]==1):
            self.__son2.play()
            return move
        elif(plateau[a][b+1]==2):
            if(plateau[a][b+2]==0):
                plateau[a][b+1]=0
                plateau[a][b+2]=2

                self.__son.play()
                move = True

            elif (plateau[a][b+2]==4):
                plateau[a][b+1] = 0
                plateau[a][b+2] = 3
                self.__son3.play()
                self.__son.play()
                move = True

        elif (plateau[a][b+1] == 3):
            if (plateau[a][b+2] == 0):
                plateau[a][b+2] = 2
                plateau[a][b+1] = 4
                move = True

        elif (plateau[a][b + 1] == 0):
            move = True
        elif (plateau[a][b+1] == 4):
            move = True
        return move


    def checkH(self,a,b):
        move = False
        plateau = self.__model.getPlateau()
        if (plateau[a - 1][b] == 1):
            self.__son2.play()
            return move
        elif (plateau[a-1][b] == 2):
            if(plateau[a-2][b]==0):
                plateau[a-1][b]=0
                plateau[a-2][b]=2
                self.__son.play()
                move = True
            elif (plateau[a-2][b] == 4):
                plateau[a-1][b] = 0
                plateau[a-2][b] = 3
                self.__son3.play()
                self.__son.play()
                move = True

        elif (plateau[a-1][b] == 3):
            if (plateau[a-2][b] == 0):
                plateau[a-2][b] = 2
                plateau[a-1][b] = 4
                move = True

        elif (plateau[a-1][b] == 0):
                move = True
        elif (plateau[a-1][b] == 4):
            move = True
        return move

    def checkG(self,a,b):
        move = False
        plateau = self.__model.getPlateau()
        if (plateau[a][b - 1] == 1):
            self.__son2.play()
            return move
        elif (plateau[a][b - 1] == 2):
            if (plateau[a][b - 2] == 0):
                plateau[a][b - 1] = 0
                plateau[a][b - 2] = 2
                self.__son.play()
                move = True
            elif (plateau[a][b - 2] == 4):
                plateau[a][b - 1] = 0
                plateau[a][b - 2] = 3
                self.__son3.play()
                self.__son.play()
                move = True

        elif (plateau[a][b-1] == 3):
            if (plateau[a][b-2] == 0):
                plateau[a][b-2] = 2
                plateau[a][b-1] = 4
                move = True

        elif (plateau[a][b - 1] == 0):
            move = True
        elif (plateau[a][b - 1] == 4):
            move = True

        return move


    def checkB(self,a,b):
        move = False
        plateau = self.__model.getPlateau()

        if (plateau[a + 1][b] == 1):
            self.__son2.play()
            return move
        elif (plateau[a + 1][b] == 2):
            if (plateau[a + 2][b] == 0):
                plateau[a + 1][b] = 0
                plateau[a + 2][b] = 2
                self.__son.play()
                move = True

            elif (plateau[a + 2][b] == 4):
                plateau[a + 1][b] = 0
                plateau[a + 2][b] = 3
                move = True
                self.__son3.play()
                self.__son.play()

        elif(plateau[a+1][b]==3):
            if(plateau[a+2][b]==0):
                plateau[a+2][b]=2
                plateau[a+1][b]=4
                move=True

        elif (plateau[a + 1][b] == 0):
            move = True
        elif (plateau[a + 1][b] == 4):
            move = True

        return move
    def Victoire(self):
        plateau = self.__model.getPlateau()
        win = 0
        for i in range(0,len(plateau)):
            for j in range(0,len(plateau[i])):
                if plateau[i][j] == 3:
                    win = win + 1
        if win == 7:
            self.__view.getMusicG().stop()
            self.viewFinal = viewF()
            self.__view.close()
            self.viewFinal.show()


