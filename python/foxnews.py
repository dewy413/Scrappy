from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("headless")
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
driver.get("https://www.foxnews.com/")


class FoxNewsArticle:
    topic = ""
    title = ""
    link = ""


# def removeCopies(listOfArticles):
#     finalList = []
#
#     for i in range(len(listOfArticles)):
#         if listOfArticles[i].title not in finalList:
#             finalList.append(listOfArticles[i])
#
#     return finalList


def sayHi():
    print("hi")

def GrabFoxArticles():
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

    return FoxNewsArticles


def GrabAllArticles():
    ListOfArticles = driver.find_elements(By.XPATH, "//article")
    ListOfURLS = driver.find_elements(By.XPATH, "//article//div[@class = 'info']//header//h2//a")
    del ListOfArticles[0:10:1]
    del ListOfArticles[45:46:1]
    del ListOfArticles[55:67:1]
    del ListOfURLS[0:10:1]
    FoxNewsArticles = []
    driver.execute_script("window.scrollTo(0,3000)")

    for i in range(len(ListOfArticles)):
        ElementsList = (ListOfArticles[i].text).split("\n")
        try:
            URL = ListOfURLS[i].get_attribute("href")
        except:
            tempArticle = FoxNewsArticle()
            match (len(ElementsList)):
                case 2:
                    tempArticle.topic = ElementsList[0]
                    tempArticle.title = ElementsList[1]
                    tempArticle.link = "No ARTICLE"
                    FoxNewsArticles.append(tempArticle)

        tempArticle = FoxNewsArticle()
        match (len(ElementsList)):
            case 2:
                tempArticle.topic = ElementsList[0]
                tempArticle.title = ElementsList[1]
                tempArticle.link = URL
                FoxNewsArticles.append(tempArticle)

    for i in range(len(FoxNewsArticles)):
        print("\nTitle: " + FoxNewsArticles[i].title + "\nTopic: " + FoxNewsArticles[i].topic + "\nLink: " +
              FoxNewsArticles[i].link)

    return FoxNewsArticles


def SearchArticles(listOfArticles, keyword):

    desiredArticles = []

    for article in listOfArticles:
        if keyword.lower() in article.title.lower():
            desiredArticles.append(article)

    print("List of articles containing " + keyword + ":\n")
    for i in range(len(desiredArticles)):
        print("\nTitle: " + desiredArticles[i].title + "\nLink: " + desiredArticles[i].link)


# listOfArticles = GrabFoxArticles()
# searchTerm = input("Enter a keyword: ")
# desiredArticles = SearchArticles(listOfArticles, searchTerm)

driver.close()
