import sys
import time

from PyQt5.QtWidgets import *
from PyQt5 import uic  # This isn't causing an error
from selenium.webdriver.common.by import By
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from fetcher.data import Article
from fetcher.allarticles import SearchArticles
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


ui = None
Articles = []
Requested_Articles = []
options = Options()
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none";
permadriver = webdriver.Chrome(desired_capabilities=caps, options=options)

class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    link = ""
    def refresh(self):

        options = Options()
        options.add_argument('headless')
        driver = webdriver.Chrome(options=options)

        website_links = ['https://www.wsj.com/', 'https://www.cnn.com/', 'https://www.foxnews.com/']
        for j in range(len(website_links)):
            driver.get(website_links[j])
            #print(website_links[j], end="\n")
            text_grabbing = driver.find_elements(By.XPATH, "//article//h3")

            for i in range(len(text_grabbing)):
                try:
                    Articles.append(Article(title=text_grabbing[i].text,
                                            link=text_grabbing[i].find_element(By.XPATH, 'a').get_attribute('href')))
                    self.progress.emit(int((i / len(text_grabbing)) * 100))
                except:
                    pass
            self.progress.emit(100)
        driver.close()
        self.finished.emit()


    def open(self):
        permadriver.switch_to.new_window()
        permadriver.get(self.link)
        self.finished.emit()



class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui  # Define UI
        self.loadUI()  # Load the UI
        self.searchButton.clicked.connect(lambda: self.searchKeyword())  # Search Button when pressed action
        self.loadButton.clicked.connect(lambda: self.load())  # Displays all the articles that it found. This is just the entire database
        self.refreshButton.clicked.connect(lambda: self.refresh())  # Regrabs all articles
        self.clearButton.clicked.connect(lambda: self.searchResults.clear())  # Clears all currently displayed article
        self.searchResults.itemDoubleClicked.connect(lambda: self.itemClicked())  # Opens link to the webpage
        self.progressBar.setHidden(True)
        self.refresh()


    def loadUI(self):
        self.ui = uic.loadUi("app.ui", self)
        self.show()




    def addItem(self, element):
        self.searchResults.addItem(element)

    def searchKeyword(self):
        self.searchResults.clear()  # Clears the search results so we can load specific articles.
        Requested_Articles = SearchArticles(Articles, str(self.searchEdit.text()))  # Gets desired articles
        No_Duplicate_Articles = []  # Temp array for removing dups.
        for i in Requested_Articles:
            if i not in No_Duplicate_Articles:  # Basic duplicate checker for loop.
                No_Duplicate_Articles.append(i)

        for i in range(len(No_Duplicate_Articles)):
            self.searchResults.addItem(
                "\n" + No_Duplicate_Articles[i].title + "\n" + No_Duplicate_Articles[
                    i].link)  # Adds results to the display.

    def addItem(self, element):
        self.searchResults.addItem(element)

    # Idea for the refresh button to load new articles and the load button to actually put them on the screen.
    def load(self):
        self.searchResults.clear()
        for i in range(len(Articles)):
            self.searchResults.addItem(
                "\n" + Articles[i].title + "\n" + Articles[i].link)

    def refresh(self):
        Articles.clear()
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.refresh)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.setProgressBar)
        self.thread.start()
        self.setProgressBar(0)
        self.progressBar.setHidden(False)
        self.thread.finished.connect(lambda: self.progressBar.setHidden(True))


    def setProgressBar(self, val):
        self.progressBar.setValue(val)

    def itemClicked(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.link = self.searchResults.selectedItems()[0].text().split("\n")[2]
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.open)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()


def runProgram():
    app = QApplication(sys.argv)
    window = GUI()
    window.show()
    sys.exit(app.exec_())


runProgram()
permadriver.close()
