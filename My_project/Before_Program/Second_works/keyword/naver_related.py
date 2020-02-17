import re
import requests
from bs4 import BeautifulSoup

keyword = input()

url = f"https://search.shopping.naver.com/search/all.nhn?where=all&frm=NVSCTAB&query={keyword}"

resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")
result = []
try:
    related_words = soup.find("div", {"class": "co_relation_srh"}).find_all("li")
except AttributeError:
    related_words = []
for i in related_words:
    first_words = (i.get_text()).rstrip('\n')
    second_words = (i.get_text()).strip()
    result.append(second_words)
print(result)