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

def FoxNewsScrape():

    Articles = []
    Entry = FoxNewsArticle
    ExclusiveClipsSection = driver.find_elements(By.XPATH, "//*[@id='wrapper']/div/div[2]/div[1]/aside[1]/div/div/div[3]/section/div/article")

    for i in range(1, len(ExclusiveClipsSection)):

        Entry.topic = driver.find_element(By.XPATH, "//*[@id='wrapper']/div/div[2]/div[1]/aside[1]/div/div/div[3]/section/div/article[{}]/div[2]/header/div/span/a".format(i)).get_attribute("textContent")
        Entry.title = driver.find_element(By.XPATH, "//*[@id='wrapper']/div/div[2]/div[1]/aside[1]/div/div/div[3]/section/div/article[{}]/div[2]/header/h2/a".format(i)).get_attribute("textContent")
        Entry.link = driver.find_element(By.XPATH, "//*[@id='wrapper']/div/div[2]/div[1]/aside[1]/div/div/div[3]/section/div/article[{}]/div[2]/header/h2/a".format(i)).get_attribute("href")

        Articles.append(Entry)



        return Articles


articlesList = driver.find_elements(By.TAG_NAME, "article")


for i in range(len(articlesList)):
    print(articlesList[i].find_element(By.XPATH, "/div[2]/header/div/span/a".format(i)).get_attribute("textContent"))



driver.close()

