import requests
from ast import literal_eval
from bs4 import BeautifulSoup

keyword = input()
keyword_list = f"https://www.coupang.com/np/search/autoComplete?callback=jQuery111108502009031661315_1573689468696&keyword={keyword}"

resp = requests.get(keyword_list)

diction = literal_eval(resp.text[43:-2])

for i in diction:
    print(i.get("keyword"))