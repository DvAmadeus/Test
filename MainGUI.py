import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import MainHandle.MainGUIHandle
form_class = uic.loadUiType("MainGUI.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        MainHandle.MainGUIHandle.Handle(self)


if __name__ == "__main__" :
    app = QApplication(sys.argv)

    myWindow = MainClass()
    myWindow.show()
    app.exec_()
