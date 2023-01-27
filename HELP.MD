
# Chat GPT on how to Thread. Might be useful to assist myself, but I prefer to write my own code.

```

import threading
from PyQt5 import QtCore

# GUI code
class MyGui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # set up GUI
        self.start_button = QtWidgets.QPushButton("Start Scraping")
        self.start_button.clicked.connect(self.start_scraping)
        # add button to layout
        self.layout.addWidget(self.start_button)
    def start_scraping(self):
        # create a new thread to run the scraping code
        scraping_thread = threading.Thread(target=self.scraping_function)
        # start the thread
        scraping_thread.start()
    def scraping_function(self):
        # Selenium code to scrape website
        driver = webdriver.Firefox()
        driver.get("https://www.example.com")
        # do scraping
        driver.quit()
```
