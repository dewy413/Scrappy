import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore  # This isn't causing an error
from fetcher.foxnews import GrabFoxArticles, SearchArticles
from fetcher.allarticles import GrabAllArticles
from fetcher.cnn import GrabCNNArticles
from fetcher.wallstreet import GrabWSJArticles
from fetcher.data import Article
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ui = None
Articles = []
Requested_Articles = []


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui
        self.loadUI()
        self.searchButton.clicked.connect(lambda: self.searchKeyword())  # Sets to when the button is press
        self.refreshButton.clicked.connect(lambda: self.refresh())  # Sets to when the button is press
        self.clearButton.clicked.connect(lambda: self.clearArticles())
        self.searchResults.itemDoubleClicked.connect(lambda: self.itemClicked())
        # Articles.extend(GrabWSJArticles())
        Articles.extend(GrabAllArticles())

    def loadUI(self):
        self.ui = uic.loadUi("app.ui", self)
        self.show()

    def searchKeyword(self):
        self.searchResults.clear()
        Requested_Articles = SearchArticles(Articles, str(self.searchEdit.text()))
        No_Duplicate_Articles = []
        for i in Requested_Articles:
            if i not in No_Duplicate_Articles:
                No_Duplicate_Articles.append(i)

        for i in range(len(No_Duplicate_Articles)):
            self.searchResults.addItem(
                "\n" + No_Duplicate_Articles[i].title + "\n" + No_Duplicate_Articles[i].link)
        No_Duplicate_Articles.clear()

    def clearArticles(self):
        self.searchResults.clear()

    def addItem(self, element):
        self.searchResults.addItem(element)

    # Idea for the refresh button to load new articles and the load button to actually put them on the screen.
    def refresh(self):
        # Articles.extend(GrabWSJArticles())
        # Articles.extend(GrabFoxArticles())
        # Articles.extend(GrabCNNArticles())
        for i in range(len(Articles)):
            self.searchResults.addItem(
                "\n" + Articles[i].title + "\n" + Articles[i].link)

    def itemClicked(self):

        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        link = self.searchResults.selectedItems()[0].text().split("\n")[2]
        driver.get(link)


def runProgram():
    app = QApplication(sys.argv)

    window = GUI()
    window.show()

    sys.exit(app.exec_())


runProgram()
