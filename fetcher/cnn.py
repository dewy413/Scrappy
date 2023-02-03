from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from fetcher.data import Article


def GrabCNNArticles() -> list[Article]:
    options = Options()
    options.add_argument('headless')
    # options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)
    driver.get('https://www.cnn.com/')
    print("test1")

    articles = driver.find_elements(By.CSS_SELECTOR, '.cd__headline')
    print("test1")

    CNNArticles = [Article(article.find_element(By.TAG_NAME, 'a').text,
                           article.find_element(By.TAG_NAME, 'a').get_attribute('href')) for article in articles]
    print("test1")

    driver.close()

    return CNNArticles
