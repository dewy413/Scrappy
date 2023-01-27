from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from python.scraper import Article









def GrabCNNArticles():
    options = Options()
    options.add_argument("headless")
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.cnn.com/")

    articles = driver.find_elements(By.CSS_SELECTOR, ".cd__headline")
    CNNArticles = []

    # iterate through the articles and print their titles and URLs
    for article in articles:
        tempArticle = Article()
        tempArticle.title = article.find_element(By.TAG_NAME, "a").text
        tempArticle.link = article.find_element(By.TAG_NAME, "a").get_attribute("href")
        CNNArticles.append(tempArticle)

    driver.close()


    return CNNArticles







GrabCNNArticles()