from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from fetcher.data import Article




def GrabFoxArticles() -> list[Article]:
    options = Options()
    options.add_argument("headless")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.foxnews.com/")
    Articles = []
    text_grabbing = driver.find_elements(By.XPATH, "//article//h3")


    for i in range(len(text_grabbing)):
        try:
            Articles.append(Article(title=text_grabbing[i].text,
                                    link=text_grabbing[i].find_element(By.XPATH, 'a').get_attribute('href')))
        except:
            pass


    driver.close()

    return Articles


def SearchArticles(articles: list[Article], keyword: str) -> list[Article]:

    
    return [article for article in articles if keyword.lower() in article.title.lower()]


