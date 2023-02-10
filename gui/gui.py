import sys, time, threading
import sys
from time import sleep
from PyQt5.QtCore import QObject, QThread, pyqtSignal

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget, QListWidget,
)
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore  # This isn't causing an error
from fetcher.foxnews import GrabFoxArticles, SearchArticles
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from fetcher.data import Article


ui = None


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(str)


    def run(self):
        print("Load Called")
        options = Options()
        options.add_argument("headless")
        options.add_argument("disable-gpu")
        print("Options Loaded")

        print("Driver created")
        driver = webdriver.Chrome(options=options)
        print("Connecting to Fox News")
        driver.get("https://www.foxnews.com/")
        print("Connected to Fox News")

        articles = driver.find_elements(By.XPATH, "//article//h2//a")
        print("Connecting to Finding Elements")

        del articles[0:10:1]
        print("Connecting to deleting unneeded articles")

        print("Loading Articles")

        for article in articles:
            self.progress.emit(article.text + " " + article.get_attribute('href'))
        driver.close()
        self.finished.emit()

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui
        self.loadUI()
        self.searchButton.clicked.connect(lambda: self.searchKeyword()) #Sets to when the button is press
        self.refreshButton.clicked.connect(lambda: self.refresh()) #Sets to when the button is press
        self.clearButton.clicked.connect(lambda: self.clearArticles())

    def loadUI(self):
        self.ui = uic.loadUi("app.ui", self)
        self.show()

    def searchKeyword(self):
        listOfArticles = GrabFoxArticles()
        desiredArticles = SearchArticles(listOfArticles, str(self.searchEdit.text()))

        for i in range(len(desiredArticles)):
            self.searchResults.addItem("\nTitle: " + desiredArticles[i].title + "\nLink: " + desiredArticles[i].link + "\n")


    def clearArticles(self):
        self.searchResults.clear()

    def addItem(self, element):
        self.searchResults.addItem(element)

    def refresh(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.addItem)

        self.thread.start()

        self.refreshButton.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.refreshButton.setEnabled(True)
        )
        self.thread.finished.connect(
            lambda: print("done")
        )


def runProgram():
    app = QApplication(sys.argv)

    window = GUI()
    window.show()

    sys.exit(app.exec_())


runProgram()
