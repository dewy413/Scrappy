from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from fetcher.data import Article

def GrabCNNArticles() -> list[Article]:

    options = Options()
    options.add_argument('headless')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)
    driver.get('https://www.cnn.com/')


    driver.close()

    return CNNArticles



GrabCNNArticles()