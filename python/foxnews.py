from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class FoxNewsArticle:
    topic = ""
    title = ""
    link = ""
    
def GrabFoxArticles():
    options = Options()
    options.add_argument("headless")
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.foxnews.com/")
    ListOfArticles = driver.find_elements(By.XPATH, "//article//h2//a")
    del ListOfArticles[0:10:1]
    FoxNewsArticles = []

    driver.execute_script("window.scrollTo(0,3000)")

    for i in range(len(ListOfArticles)):
        tempArticle = FoxNewsArticle()
        tempArticle.topic = "N/A"
        tempArticle.title = ListOfArticles[i].text
        tempArticle.link = ListOfArticles[i].get_attribute("href")
        FoxNewsArticles.append(tempArticle)

    driver.close()

    return FoxNewsArticles


def PrintArticles(listOfArticles):
    for i in range(len(listOfArticles)):
        print("\nTitle: " + listOfArticles[i].title + "\nLink: " + listOfArticles[i].link + "\n")

def SearchArticles(listOfArticles, keyword):

    desiredArticles = []

    for article in listOfArticles:
        if keyword.lower() in article.title.lower():
            desiredArticles.append(article)

    print("List of articles containing " + keyword + ":\n")
    for i in range(len(desiredArticles)):
        print("\nTitle: " + desiredArticles[i].title + "\nLink: " + desiredArticles[i].link)


