import re
import requests
from bs4 import BeautifulSoup
from ast import literal_eval

#Insert Keyword
keyword = input()

#Find keyword in naver search
keyword_list = f"https://ac.search.naver.com/nx/ac?_callback=window.__jindo_callback._$3361_0&q={keyword}&q_enc=UTF-8&st=100&frm=nv&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&ans=2&run=2&rev=4&con=1"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
resp = requests.get(keyword_list)
diction_resp = literal_eval(resp.text[32:])

result = []
for i in range(len(diction_resp.get('items')[0])):
    result.append(diction_resp.get('items')[0][i][0])

#Find keyword in naver related keyword
url = f"https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query={keyword}"
resp2 = requests.get(url)
soup = BeautifulSoup(resp2.text, "html.parser")
try:
    related_words = soup.find("ul", {"class": "_related_keyword_ul"}).find_all("li")
except AttributeError:
    related_words = []
for i in related_words:
    result.append(i.get_text())

#Find keyword in Coupang
coupang_keyword_list = f"https://www.coupang.com/np/search/autoComplete?callback=jQuery111108502009031661315_1573689468696&keyword={keyword}"
resp3 = requests.get(coupang_keyword_list)
diction = literal_eval(resp3.text[43:-2])

try:
    for i in diction:
        result.append(i.get("keyword"))
except AttributeError:
    pass

your_keyword = ','.join(result)

print(your_keyword)