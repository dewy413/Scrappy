from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



class CNNNewsArticle:
    title = ""
    link = ""






def GrabCNNArticles():
    options = Options()
    options.add_argument("headless")
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.cnn.com/")
    ListOfArticles = driver.find_elements(By.XPATH, '//article//span[@class="cd__headline-text vid-left-enabled"]')
    CNNNewsArticles = []

    driver.execute_script("window.scrollTo(0,3000)")

    for i in range(len(ListOfArticles)):
        tempArticle = CNNNewsArticle()
        tempArticle.title = ListOfArticles[i].text
        tempArticle.link = ListOfArticles[i].get_attribute("href")
        CNNNewsArticles.append(tempArticle)


    for i in range(len(CNNNewsArticles)):
        #print(CNNNewsArticles[i].title + "\n" + CNNNewsArticles[i].link + "\n")

    driver.close()

    return CNNNewsArticles






GrabCNNArticles()