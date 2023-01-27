from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from dataclasses import dataclass

@dataclass
class Article:
    title: str
    link: str


def GrabFoxArticles():
    
    options = Options()
    options.add_argument("headless")
    options.add_argument('--disable-gpu')
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.foxnews.com/")
    
    ListOfArticles = driver.find_elements(By.XPATH, "//article//h2//a")
    del ListOfArticles[0:10:1]
    
    FoxNewsArticles = [Article(article.text, article.getAttribute('href')) for article in ListOfArticles]
    driver.close()

    return FoxNewsArticles


def SearchArticles(listOfArticles, keyword):
    return [article for article in listOfArticles if keyword.lower() in article.title.lower()]

