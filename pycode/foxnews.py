from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("headless") #Comment this out if you want to see it open the browser.
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
driver.get("https://www.foxnews.com/")



class FoxNewsArticle:
    topic = ""
    title = ""
    link = ""
def FoxNewsPrint():
    ListOfThings = FoxNewsScrape()

    for i in ListOfThings:
        print(f"Topic: {i.topic}\n{i.title}\nLink: {i.link}\n")
def FoxNewsHeadline():
    Headline = FoxNewsArticle
    Headline.topic = "HEADLINE"
    Headline.title = driver.find_element(By.XPATH,
                                      "//*[@id='wrapper']/div/div[2]/div[1]/main/div/div/div[1]/div/article/div[2]/header/h2/a").get_attribute(
        "textContent")  # HeadLine Article
    Headline.link = driver.find_element(By.XPATH,
                                     "//*[@id='wrapper']/div/div[2]/div[1]/main/div/div/div[1]/div/article/div[2]/header/h2/a").get_attribute(
        "href")  # HeadLine Link

    return Headline
def FoxNewsScrape():

    Articles = []
    Articles.append(FoxNewsHeadline())

    ExclusiveClipsSection = driver.find_elements(By.XPATH, "//*[@id='wrapper']/div/div[2]/div[1]/aside[1]/div/div/div[3]/section/div/article")

    for i in range(1, len(ExclusiveClipsSection) + 1):

        ExclusiveClips = FoxNewsArticle()
        ExclusiveClips.topic = driver.find_element(By.XPATH, "//*[@id='wrapper']/div/div[2]/div[1]/aside[1]/div/div/div[3]/section/div/article[{}]/div[2]/header/div/span/a".format(i)).get_attribute("textContent")
        ExclusiveClips.title = driver.find_element(By.XPATH, "//*[@id='wrapper']/div/div[2]/div[1]/aside[1]/div/div/div[3]/section/div/article[{}]/div[2]/header/h2/a".format(i)).get_attribute("textContent")
        ExclusiveClips.link = driver.find_element(By.XPATH, "//*[@id='wrapper']/div/div[2]/div[1]/aside[1]/div/div/div[3]/section/div/article[{}]/div[2]/header/h2/a".format(i)).get_attribute("href")

        Articles.append(ExclusiveClips)



    return Articles



FoxNewsPrint()
driver.close()

