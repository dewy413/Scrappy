from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from data import Article

def GrabFoxArticles() -> list[Article]:
    
    '''
        Scrape the headlines and URLs of articles from the Fox News website.
    '''
    
    options = Options()
    options.add_argument("headless")
    options.add_argument('--disable-gpu')
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.foxnews.com/")
    
    articles = driver.find_elements(By.XPATH, "//article//h2//a")
    del articles[0:10:1]
    
    FoxNewsArticles = [Article(article.text, article.get_attribute('href')) for article in articles]
    driver.close()

    return FoxNewsArticles


def SearchArticles(articles: list[Article], keyword: str) -> list[Article]:
    
    '''
        Takes in a list of Article objects and a keyword string as inputs.
        returns a new list of Article objects that have the keyword in their title (case-insensitive).
    '''
    
    return [article for article in articles if keyword.lower() in article.title.lower()]

