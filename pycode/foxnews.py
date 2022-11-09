from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("headless") #Comment this out if you want to see it open the browser.
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
driver.get("https://www.foxnews.com/")

class FoxNews:
    topic = ""
    title = ""
    link = ""

ExclusiveClipsSection = driver.find_elements(By.XPATH, "//*[@id='wrapper']/div/div[2]/div[1]/aside[1]/div/div/div[3]/section/div/article")
ExclusiveClips = ["" for i in range(len(ExclusiveClipsSection))]


for i in range(1, len(ExclusiveClipsSection)):
    Entry = FoxNews
    topic = driver.find_element(By.XPATH, "//*[@id='wrapper']/div/div[2]/div[1]/aside[1]/div/div/div[3]/section/div/article[{}]/div[2]/header/div/span/a".format(i)).get_attribute("textContent")
    title = driver.find_element(By.XPATH, "//*[@id='wrapper']/div/div[2]/div[1]/aside[1]/div/div/div[3]/section/div/article[{}]/div[2]/header/h2/a".format(i)).get_attribute("textContent")
    link = driver.find_element(By.XPATH, "//*[@id='wrapper']/div/div[2]/div[1]/aside[1]/div/div/div[3]/section/div/article[{}]/div[2]/header/h2/a".format(i)).get_attribute("href")

    Entry.topic = topic
    Entry.title = title
    Entry.link = link
    print(f"Topic: {Entry.topic}\nTitle: {Entry.title}\nLink: {Entry.link}\n")

driver.close()

