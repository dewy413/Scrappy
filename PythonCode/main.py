import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
#options.add_argument("headless")
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
driver.get("https://www.foxnews.com/politics")

clss = driver.find_element(By.XPATH,
                               "/html/body/div[2]/div/div/div/div[2]/div/main/section[1]/div/article[1]").text

print(clss)


