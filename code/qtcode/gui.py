import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic #This was a causing so much trouble, but I figured it out eventually.

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = None
        self.loadUI()

    def loadUI(self):
        self.ui = uic.loadUi("app.ui", self)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = GUI()
    window.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("CLosed")
