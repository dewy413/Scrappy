from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from fetcher.data import Article


def GrabAllArticles() -> list[Article]:
    print("Setting up Options", end="\n")

    options = Options()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    print("Option setup complete", end="\n")


    Articles = []
    website_links = ['https://www.wsj.com/', 'https://www.cnn.com/', 'https://www.foxnews.com/']

    print("Starting for loop", end="\n")
    for j in range(len(website_links)):
        print(website_links[j], end="\n")
        driver.get(website_links[j])
        text_grabbing = driver.find_elements(By.XPATH, "//article//h3")
        for i in range(len(text_grabbing)):
            print(i, end="\n")
            try:
                Articles.append(Article(title=text_grabbing[i].text,
                                        link=text_grabbing[i].find_element(By.XPATH, 'a').get_attribute('href')))
            except:
                pass



    driver.close()

    return Articles