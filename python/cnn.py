from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from data import Article

def GrabCNNArticles() -> list[Article]:
    
    options = Options()
    options.add_argument('headless')
    options.add_argument('--disable-gpu')
    
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.cnn.com/')

    articles = driver.find_elements(By.CSS_SELECTOR, '.cd__headline')
    
    CNNArticles = [Article(article.find_element(By.TAG_NAME, 'a').text, article.find_element(By.TAG_NAME, 'a').get_attribute('href')) for article in articles]
    driver.close()

    return CNNArticles