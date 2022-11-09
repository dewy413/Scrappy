from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By




options = Options()
options.add_argument("headless") #Comment this out if you want to see it open the browser.
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
driver.get("https://www.foxnews.com/")

ExclusiveClipsSection = driver.find_elements(By.XPATH, "//*[@id='wrapper']/div/div[2]/div[1]/aside[1]/div/div/div[3]/section/div/article")
ExclusiveClips = ["" for i in range(len(ExclusiveClipsSection))]

for i in range(1, len(ExclusiveClipsSection)):
    print(driver.find_element(By.XPATH, "//*[@id='wrapper']/div/div[2]/div[1]/aside[1]/div/div/div[3]/section/div/article[{}]".format(i)).get_attribute("textContent"))

driver.close()

