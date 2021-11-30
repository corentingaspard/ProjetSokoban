import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QStatusBar
from view.gridView import *
from model.Model import *
from control.crtlMouvement import *
from PyQt5.QtMultimedia import QSound

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sokoban")
        self.setWindowIcon(QIcon("images/logo.png"))
        self.__musicG = QSound("son/Wii.wav")
        self.__model = Model(self)
        self.__view = gridView()
        self.__controller = crtlMouvement()
        self.__view.setModel(self.__model)
        self.__view.setController(self.__controller)
        self.__model.setView(self.__view)
        self.__controller.setView(self.__view)
        self.__controller.setModel(self.__model)
        self.setCentralWidget(self.__view)
        self.menuBarGame()
        self.StatusBarGame()
        self.__view.setFocus()
        self.__view.getMusicG().play()
        self.show()

    def menuBarGame(self):
        self.bar = self.menuBar()
        self.setMenuBar(self.bar)
        self.Jeu = self.bar.addMenu("Jeu")
        self.Theme = self.bar.addMenu("Thèmes")

        self.quitGame = QAction("Quit",self)
        self.quitGame.setShortcut("Ctrl+Q")
        self.Jeu.addAction(self.quitGame)
        self.quitGame.triggered.connect(self.boutonQ)

        self.restartGame = QAction("Restart",self)
        self.restartGame.setShortcut("Ctrl+R")
        self.Jeu.addAction(self.restartGame)
        self.restartGame.triggered.connect(self.boutonR)

        self.MainTheme = QAction("MainTheme",self)
        self.Theme.addAction(self.MainTheme)
        self.MainTheme.triggered.connect(lambda: self.__model.setTheme("MainTheme"))

        self.Ricard = QAction("Ricard", self)
        self.Theme.addAction(self.Ricard)
        self.Ricard.triggered.connect(lambda: self.__model.setTheme("Ricard"))

        self.Ratchet = QAction("Ratchet",self)
        self.Theme.addAction(self.Ratchet)
        self.Ratchet.triggered.connect(lambda: self.__model.setTheme("Ratchet"))

        self.DBZ = QAction("DBZ",self)
        self.Theme.addAction(self.DBZ)
        self.DBZ.triggered.connect(lambda: self.__model.setTheme("DBZ"))

    def boutonR(self):
        self.close()
        self.__view.getMusicG().stop()
        self.__model = Model(self)
        self.__view = gridView()
        self.__controller = crtlMouvement()
        self.__view.setModel(self.__model)
        self.__view.setController(self.__controller)
        self.__model.setView(self.__view)
        self.__controller.setView(self.__view)
        self.__controller.setModel(self.__model)
        self.setCentralWidget(self.__view)
        self.__view.setFocus()
        self.__view.getMusicG().play()
        self.show()

    def boutonQ(self):
        sys.exit(app.exec_())

    def StatusBarGame(self):
        self.Bar = QStatusBar()
        self.setStatusBar(self.Bar)
        self.Bar.showMessage("Nombre de pas : " + str(self.__model.getPas()))

    def updatePas(self):
        self.Bar.showMessage("Nombre de pas : " + str(self.__model.getPas()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


