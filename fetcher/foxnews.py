from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from fetcher.data import Article




def GrabFoxArticles() -> list[Article]:


    options = Options()
    options.add_argument("headless")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.foxnews.com/")
    
    articles = driver.find_elements(By.XPATH, "//article//h2//a")
    removedDupsText = []
    removedDupsURL = []

    del articles[0:10:1]

    # for i in range(len(articles)):
    #     removedDupsText.append(articles[i].text)
    #     removedDupsURL.append(articles[i].get_attribute('href'))
    #
    # print("List Size Before: ", len(removedDupsText), " ", len(removedDupsURL))
    # removedDupsText = set(removedDupsText)
    # removedDupsURL = set(removedDupsURL)
    # print("List Size After: ", len(removedDupsText), " ", len(removedDupsURL))
    #
    #

    FoxNewsArticles = [Article(article.text, article.get_attribute('href')) for article in articles]
    driver.close()

    return FoxNewsArticles


def SearchArticles(articles: list[Article], keyword: str) -> list[Article]:

    
    return [article for article in articles if keyword.lower() in article.title.lower()]


GrabFoxArticles()