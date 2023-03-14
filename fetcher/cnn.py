from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from fetcher.data import Article

def GrabCNNArticles() -> list[Article]:

    options = Options()
    options.add_argument('headless')

    driver = webdriver.Chrome(options=options)
    driver.get('https://www.cnn.com/')
    Articles = []

    wait = WebDriverWait(driver, 2)

    text_grabbing = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'cd__headline')))

    print(len(text_grabbing))
    for i in range(len(text_grabbing)):
        try:
            Articles.append(Article(title=text_grabbing[i].text, link=text_grabbing[i].find_element(By.XPATH, 'a').get_attribute('href')))
        except:
            pass


    driver.close()

    return Articles


GrabCNNArticles()