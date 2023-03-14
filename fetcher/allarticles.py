from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from fetcher.data import Article


def GrabAllArticles() -> list[Article]:
    options = Options()
    options.add_argument('headless')

    driver = webdriver.Chrome(options=options)
    driver.get('https://www.cnn.com/')
    Articles = []
    website_links = ['https://www.wsj.com/', 'https://www.cnn.com/', 'https://www.foxnews.com/']

    for j in range(len(website_links)):
        driver.get(website_links[j])
        text_grabbing = driver.find_elements(By.XPATH, "//article//h3")
        for i in range(len(text_grabbing)):
            try:
                Articles.append(Article(title=text_grabbing[i].text,
                                        link=text_grabbing[i].find_element(By.XPATH, 'a').get_attribute('href')))
            except:
                pass



    driver.close()

    return Articles