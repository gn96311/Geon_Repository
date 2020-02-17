from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time
import sys

keyword = list(map(str, input().split()))

chrome_driver = 'C:\\Users\\Home\\Downloads\\chromedriver'
driver = webdriver.Chrome(chrome_driver)

def item_scout(keyword):
    time.sleep(1)
    item_scout_url = f'https://itemscout.io/keyword/'
    driver.get(item_scout_url)
    search = driver.find_element_by_class_name("input-keyword")
    search.clear()
    search.send_keys(keyword)
    search.send_keys(Keys.RETURN)
    WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"related-keywords")))
    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")
    related_words = soup.select('.related-keywords a')
    result_3 = []
    for j in related_words:
        result_3.append((j.get_text().split())[0])
    print(result_3)

item_scout(keyword[0])