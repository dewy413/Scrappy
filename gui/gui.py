import sys, time
from PyQt5.QtWidgets import *
from PyQt5 import uic  #This isn't causing an error
from python.foxnews import *


ui = None
class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.searchButton = None
        self.ui = ui
        self.loadUI()
        self.searchButton.clicked.connect(lambda: self.printValue()) #Sets to when the button is press
        self.refreshButton.clicked.connect(lambda: self.refresh()) #Sets to when the button is press


    def loadUI(self):
        self.ui = uic.loadUi("app.ui", self)
        self.show()

    def refresh(self):
        listOfArticle = GrabFoxArticles()
        self.searchResults.addItems(listOfArticle)
        for i in range(len(listOfArticle)):
            self.searchResults.addItem("\nTitle: " + listOfArticle[i].title + "\nLink: " + listOfArticle[i].link + "\n")


def runProgram():
    app = QApplication(sys.argv)

    window = GUI()
    window.show()

    try:
        sys.exit(app.exec_())

    except SystemExit:
        print("Program Closed")


runProgram()
