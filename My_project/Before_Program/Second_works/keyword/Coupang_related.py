import re
import requests
from bs4 import BeautifulSoup

keyword = input()

url = f"https://www.coupang.com/np/search?component=&q={keyword}&channel=user"

resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")

related_words = soup.find("dl", {"class": "search-related-keyword"}).find_all("dd")

result = []
for i in related_words:
    result.append(i.get_text())

print(result)