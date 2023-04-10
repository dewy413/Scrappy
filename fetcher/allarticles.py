import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fetcher.data import Article


def GrabAllArticles() -> list[Article]:

    Articles = []
    print("Starting Grabbing Articles")

    Articles.extend(checkWebsite("https://www.cnn.com/"))
    Articles.extend(checkWebsite("https://www.foxnews.com/"))
    Articles.extend(checkWebsite("https://www.wsj.com/"))

    return Articles

def checkWebsite(page) -> list[Article]:
        options = Options()
        options.add_argument('headless')
        driver = webdriver.Chrome(options=options)
        driver.get(page)
        Articles = []
        print(page, end="\n")
        text_grabbing = driver.find_elements(By.XPATH, "//article//h3")
        for i in range(len(text_grabbing)):
            #print(i, end="\n")
            try:
                Articles.append(Article(title=text_grabbing[i].text,
                                        link=text_grabbing[i].find_element(By.XPATH, 'a').get_attribute('href')))
            except:
                pass
        driver.close()
        return Articles
