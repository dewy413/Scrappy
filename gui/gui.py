import sys
import threading
from PyQt5.QtWidgets import *
from PyQt5 import uic  # This isn't causing an error
from fetcher.foxnews import SearchArticles
from fetcher.allarticles import GrabAllArticles
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ui = None
Articles = []
Requested_Articles = []



class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui # Define UI
        self.loadUI() # Load the UI
        self.searchButton.clicked.connect(lambda: self.searchKeyword())  # Search Button when pressed action
        self.loadButton.clicked.connect(lambda: self.load())  # Displays all the articles that it found. This is just the entire database
        self.refreshButton.clicked.connect(lambda: self.refresh()) # Regrabs all articles
        self.clearButton.clicked.connect(lambda: self.searchResults.clear()) # Clears all currently displayed article
        self.searchResults.itemDoubleClicked.connect(lambda: self.itemClicked()) # Opens link to the webpage

    def loadUI(self):
        self.ui = uic.loadUi("app.ui", self)
        self.show()

    def addItem(self, element):
        self.searchResults.addItem(element)

    def searchKeyword(self):
        self.searchResults.clear() # Clears the search results so we can load specific articles.
        Requested_Articles = SearchArticles(Articles, str(self.searchEdit.text())) # Gets desired articles
        No_Duplicate_Articles = [] #Temp array for removing dups.
        for i in Requested_Articles:
            if i not in No_Duplicate_Articles: # Basic duplicate checker for loop.
                No_Duplicate_Articles.append(i)

        for i in range(len(No_Duplicate_Articles)):
            self.searchResults.addItem(
                "\n" + No_Duplicate_Articles[i].title + "\n" + No_Duplicate_Articles[i].link) # Adds results to the display.


    def addItem(self, element):
        self.searchResults.addItem(element)

    # Idea for the refresh button to load new articles and the load button to actually put them on the screen.
    def load(self):
        # Articles.extend(GrabWSJArticles())
        # Articles.extend(GrabFoxArticles())
        # Articles.extend(GrabCNNArticles())
        for i in range(len(Articles)):
            self.searchResults.addItem(
                "\n" + Articles[i].title + "\n" + Articles[i].link)

    def refresh(self):
        Articles.clear()
        Articles.extend(GrabAllArticles())
    def itemClicked(self):

        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        link = self.searchResults.selectedItems()[0].text().split("\n")[2]
        driver.get(link)


def runProgram():
    app = QApplication(sys.argv)
    print("Starting program")
    window = GUI()
    window.show()
    sys.exit(app.exec_())


runProgram()