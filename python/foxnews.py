from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Article:
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

    for i in range(len(ListOfArticles)):
        tempArticle = Article()
        tempArticle.title = ListOfArticles[i].text
        tempArticle.link = ListOfArticles[i].get_attribute("href")
        FoxNewsArticles.append(tempArticle)

    driver.close()

    return FoxNewsArticles


def SearchArticles(listOfArticles, keyword):
    return [article for article in listOfArticles if keyword.lower() in article.title.lower()]

