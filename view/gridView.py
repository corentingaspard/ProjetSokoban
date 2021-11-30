from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QPainter
from view.viewFinal import *

class gridView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sokoban")
        self.setStyleSheet("background-color:#C3C9C5")
        self.setFixedSize(450,450)
        self.__controller = None
        self.__model = None
        self.__musicG = QSound("son/Wii.wav")


    def setModel(self, model):
        self.__model = model

    def getModel(self):
        return self.__model

    def setController(self, controller):
        self.__controller = controller

    def getController(self):
        return self.__controller

    def updateView(self):
        self.update()

    def getMusicG(self):
        return self.__musicG

    def paintEvent(self,event):
        painter = QPainter(self)
        plateau = self.__model.getPlateau()
        theme = self.__model.getTheme()
        model = self.getModel()
        for i in range(len(plateau)):
            for j in range(len(plateau[i])):
                case = plateau[i][j]
                if (case == 4):
                    r = QtCore.QRect(j * 50, i * 50, 50, 50)
                    im = QtGui.QPixmap("images/"+theme+"/etoile.png")
                    im = im.scaled(r.size())
                    painter.drawPixmap(r, im)
                elif (case == 1):
                    r = QtCore.QRect(j*50,i*50,50,50)
                    im =QtGui.QPixmap("images/"+theme+"/mur.png")
                    im = im.scaled(r.size())
                    painter.drawPixmap(r,im)
                elif (case == 2):
                    r = QtCore.QRect(j*50,i*50,50,50)
                    im =QtGui.QPixmap("images/"+theme+"/Petite_caisse.png")
                    im = im.scaled(r.size())
                    painter.drawPixmap(r,im)
                elif (case == 3):
                    r = QtCore.QRect(j*50,i*50,50,50)
                    im = QtGui.QPixmap("images/"+theme+"/caisseE.png")
                    im = im.scaled(r.size())
                    painter.drawPixmap(r, im)
                if (i == model.getPlayer()[0] and j == model.getPlayer()[1]):
                    r= QtCore.QRect(j*50,i*50,40,50)
                    im = QtGui.QPixmap("images/"+theme+"/perso.png")
                    im = im.scaled(r.size())
                    painter.drawPixmap(r,im)
        self.__controller.Victoire()

    def keyPressEvent(self,event):
        value=event.key() - 16777234
        if value == 0:
            if self.__controller.checkG(self.__model.getPlayer()[0], self.__model.getPlayer()[1]):
                self.__model.updatePlayer([self.__model.getPlayer()[0], self.__model.getPlayer()[1]-1])
                self.__model.addPas()
        elif value == 1:
            if self.__controller.checkH(self.__model.getPlayer()[0], self.__model.getPlayer()[1]):
                self.__model.updatePlayer([self.__model.getPlayer()[0]-1,self.__model.getPlayer()[1]])
                self.__model.addPas()

        elif value == 2:
            if self.__controller.checkD(self.__model.getPlayer()[0],self.__model.getPlayer()[1]):
                self.__model.updatePlayer([self.__model.getPlayer()[0], self.__model.getPlayer()[1]+1])
                self.__model.addPas()

        elif value == 3:
            if self.__controller.checkB(self.__model.getPlayer()[0], self.__model.getPlayer()[1]):
                self.__model.updatePlayer([self.__model.getPlayer()[0]+1, self.__model.getPlayer()[1]])
                self.__model.addPas()


    def updateView(self):
        self.update()

