from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time

chrome_driver = 'C:\\Users\\Home\\Downloads\\chromedriver'

driver = webdriver.Chrome(chrome_driver)

url = 'https://www.amazon.com/dp/B07W6RPZVY/ref=sspa_dk_detail_4?psc=1&pd_rd_i=B07W6RPZVY&pd_rd_w=fzmO5&pf_rd_p=45a72588-80f7-4414-9851-786f6c16d42b&pd_rd_wg=wkDk1&pf_rd_r=1T5K1V76414JSCENQDDK&pd_rd_r=67a268a2-bfaa-421e-821b-b644514a6ce5&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFQNlpEM0ZJTTUxUFgmZW5jcnlwdGVkSWQ9QTAwNDM3OTkxM0FPVVhMTDdJQVQmZW5jcnlwdGVkQWRJZD1BMDIwMjcxMTJCSkNLRUlOSVRWTEwmd2lkZ2V0TmFtZT1zcF9kZXRhaWwmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'
url2 = 'https://www.amazon.com/Swanson-Vitamin-Mixed-Tocopherols-Milligrams/dp/B07F94DYLT/ref=pd_sbs_121_3/142-3971664-9480742?_encoding=UTF8&pd_rd_i=B07F94DYLT&pd_rd_r=f92c0793-ea34-464b-a857-a66b6d861de6&pd_rd_w=lmjWh&pd_rd_wg=uU77t&pf_rd_p=bdd201df-734f-454e-883c-73b0d8ccd4c3&pf_rd_r=DE2F7H3KD1Z8DQ38BWWT&psc=1&refRID=DE2F7H3KD1Z8DQ38BWWT'
url_list = []
url_list.append(url)
url_list.append(url2)
for n in url_list:
    driver.get(str(n))

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, "priceblock_ourprice"))
            )
    except TimeoutError:
        print('Time out')

    soup = BeautifulSoup(driver.page_source, features='lxml')

    driver.close()

    price = soup.select_one('#priceblock_ourprice')
    print(price.get_text())