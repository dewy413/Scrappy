import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore  # This isn't causing an error
from fetcher.foxnews import GrabFoxArticles, SearchArticles
from fetcher.cnn import GrabCNNArticles
from fetcher.wallstreet import GrabWSJArticles
from fetcher.data import Article

ui = None


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui
        self.loadUI()
        self.searchButton.clicked.connect(lambda: self.searchKeyword())  # Sets to when the button is press
        self.refreshButton.clicked.connect(lambda: self.refresh())  # Sets to when the button is press
        self.clearButton.clicked.connect(lambda: self.clearArticles())
        self.searchResults.itemDoubleClicked.connect(lambda: self.itemClicked())

    def loadUI(self):
        self.ui = uic.loadUi("app.ui", self)
        self.show()

    def searchKeyword(self):
        listOfArticles = GrabFoxArticles()
        desiredArticles = SearchArticles(listOfArticles, str(self.searchEdit.text()))

        for i in range(len(desiredArticles)):
            self.searchResults.addItem(
                "\nTitle: " + desiredArticles[i].title + "\nLink: " + desiredArticles[i].link + "\n")

    def clearArticles(self):
        self.searchResults.clear()

    def addItem(self, element):
        self.searchResults.addItem(element)

    def refresh(self):
        theseArticles = GrabWSJArticles()
        # theseArticles.extend(GrabFoxArticles())
        # theseArticles.extend(GrabCNNArticles())
        for i in range(len(theseArticles)):
            self.searchResults.addItem(
                "\nTitle: " + theseArticles[i].title + "\nLink: " + theseArticles[i].link + "\n")

    def itemClicked(self):
        print("Double clicked", self.searchResults.currentRow())


def runProgram():
    app = QApplication(sys.argv)

    window = GUI()
    window.show()

    sys.exit(app.exec_())


runProgram()
