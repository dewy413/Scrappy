import sys
from python.foxnews import *
from PyQt5.QtWidgets import *
from PyQt5 import uic #This was a causing so much trouble, but I figured it out eventually.

from python.foxnews import GrabFoxArticles

listOfArticles = GrabFoxArticles()

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = None
        self.loadUI()
        self.searchButton.clicked.connect(self.searchResults())


    def loadUI(self):
        self.ui = uic.loadUi("app.ui", self)
        self.show()


    def searchResults(self):
        for i in range(len(listOfArticles)):
            print("\nTitle: " + listOfArticles[i].title + "\nLink: " + listOfArticles[i].link)






if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = GUI()
    window.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("Program Closed")
