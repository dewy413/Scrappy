import sys, time
from PyQt5.QtWidgets import *
from PyQt5 import uic  #This was a causing so much trouble, but I figured it out eventually.
from python.foxnews import *


ui = None
class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.searchButton = None
        self.ui = ui
        self.loadUI()
        self.searchButton.clicked.connect(lambda: self.printValue())


    def loadUI(self):
        self.ui = uic.loadUi("app.ui", self)
        self.show()


    def printValue(self):
        listOfArticle = GrabFoxArticles()
        PrintArticles(listOfArticle)
        for i in range(len(listOfArticle)):
            self.searchResults.addItem("\nTitle: " + listOfArticle[i].title + "\nLink: " + listOfArticle[i].link + "\n")

        time.sleep(2)


def runProgram():
    app = QApplication(sys.argv)

    window = GUI()
    window.show()

    try:
        sys.exit(app.exec_())

    except SystemExit:
        print("Program Closed")


runProgram()
