from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def StartEngine():
    options = Options()
    options.add_argument("headless")
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    #driver.get("https://www.foxnews.com/")

    print("Done")