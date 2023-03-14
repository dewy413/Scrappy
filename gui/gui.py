import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore  # This isn't causing an error
from fetcher.foxnews import GrabFoxArticles, SearchArticles
from fetcher.allarticles import GrabAllArticles
from fetcher.cnn import GrabCNNArticles
from fetcher.wallstreet import GrabWSJArticles
from fetcher.data import Article
from selenium import webdriver


ui = None
Articles = []

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
    #Idea for the refresh button to load new articles and the load button to actually put them on the screen.
    def refresh(self):
        Articles = GrabAllArticles()
        # Articles.extend(GrabWSJArticles())
        # Articles.extend(GrabFoxArticles())
        # Articles.extend(GrabCNNArticles())
        for i in range(len(Articles)):
            self.searchResults.addItem(
                "\nTitle: " + Articles[i].title + "\nLink: " + Articles[i].link + "\n")

    def itemClicked(self):
        print(Articles[self.searchResults.currentRow()].url)


def runProgram():
    app = QApplication(sys.argv)

    window = GUI()
    window.show()

    sys.exit(app.exec_())


runProgram()
