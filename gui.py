import sys, time, threading
from PyQt5.QtWidgets import *
from PyQt5 import uic  #This isn't causing an error
from fetcher.foxnews import GrabFoxArticles, SearchArticles
from fetcher.cnn import GrabCNNArticles


ui = None
class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui
        self.loadUI()
        self.searchButton.clicked.connect(lambda: self.searchKeyword()) #Sets to when the button is press
        self.refreshButton.clicked.connect(lambda: self.refresh()) #Sets to when the button is press
        self.clearButton.clicked.connect(lambda: self.clearArticles())

    def loadUI(self):
        self.ui = uic.loadUi("./layout/app.ui", self)
        self.show()

    def searchKeyword(self):
        listOfArticles = GrabFoxArticles()
        desiredArticles = SearchArticles(listOfArticles, str(self.searchEdit.text()))

        for i in range(len(desiredArticles)):
            self.searchResults.addItem("\nTitle: " + desiredArticles[i].title + "\nLink: " + desiredArticles[i].link + "\n")


    def clearArticles(self):
        self.searchResults.clear()


    def refresh(self):
        listOfArticles = GrabFoxArticles()
        CNNArticles = GrabCNNArticles()
        for i in range(len(listOfArticles)):
            self.searchResults.addItem("Website: FOX\n" + "\nTitle: " + listOfArticles[i].title + "\nLink: " + listOfArticles[i].link + "\n")
        for i in range(len(CNNArticles)):
            self.searchResults.addItem("Website: CNN\n" + "\nTitle: " + CNNArticles[i].title + "\nLink: " + CNNArticles[i].link + "\n")



def runProgram():
    app = QApplication(sys.argv)

    window = GUI()
    window.show()

    sys.exit(app.exec_())


runProgram()
