import openpyxl
import sys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

chrome_driver = 'C:\\Users\\Home\\Downloads\\chromedriver'
driver = webdriver.Chrome(chrome_driver)

def cost_check(product_url):
    url = product_url
    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, "priceblock_ourprice"))
            )
    except TimeoutError:
        print('Time out')
    
    soup = BeautifulSoup(driver.page_source, features='lxml')
    driver.quit()

    price = soup.select_one('#priceblock_ourprice')
    text_price = price.get_text()
    return text_price

wb = openpyxl.load_workbook('아마존 리스팅.xlsx')

sheet1 = wb['Sheet1']

for rows in range(2):
    cost_url = sheet1.cell(row=3+rows, column=2).value
    return_price = cost_check(str(cost_url))
    print(return_price)