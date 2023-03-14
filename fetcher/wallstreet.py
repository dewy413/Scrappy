import selenium.webdriver.chromium.webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from fetcher.data import Article


def GrabWSJ() -> list[Article]:
    options = Options()
    options.add_argument("headless")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.wsj.com/")
    Articles = []
    text_grabbing = driver.find_elements(By.XPATH, "//article//h3")

    for i in range(len(text_grabbing)):
        try:
            print(text_grabbing[i].text, " ", text_grabbing[i].find_element(By.XPATH, 'a').get_attribute('href'))
            Articles.append(Article(title=text_grabbing[i].text, link=text_grabbing[i].find_element(By.XPATH, 'a').get_attribute('href')))
        except:
            pass



    return Articles

GrabWSJ()