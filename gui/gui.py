import sys, time
from PyQt5.QtWidgets import *
from PyQt5 import uic  #This isn't causing an error
from python.foxnews import *


ui = None
class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui
        self.loadUI()
        self.searchButton.clicked.connect(lambda: self.searchKeyword()) #Sets to when the button is press
        self.refreshButton.clicked.connect(lambda: self.refresh()) #Sets to when the button is press

    def loadUI(self):
        self.ui = uic.loadUi("app.ui", self)
        self.show()

    def searchKeyword(self):
        print("test")
        listOfArticles = GrabFoxArticles()
        print("test")
        desiredArticles = SearchArticles(listOfArticles, str(self.searchEdit.text()))
        print("test")

        for i in range(len(desiredArticles)):
            self.searchResults.addItem("\nTitle: " + desiredArticles[i].title + "\nLink: " + desiredArticles[i].link + "\n")


    def refresh(self):
        listOfArticles = GrabFoxArticles()
        for i in range(len(listOfArticles)):
            self.searchResults.addItem("\nTitle: " + listOfArticles[i].title + "\nLink: " + listOfArticles[i].link + "\n")


def runProgram():
    app = QApplication(sys.argv)

    window = GUI()
    window.show()

    try:
        sys.exit(app.exec_())

    except SystemExit:
        print("Program Closed")


runProgram()
