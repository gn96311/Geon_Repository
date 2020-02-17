import requests
from ast import literal_eval

keyword = input()
keyword_list = f"https://ac.search.naver.com/nx/ac?_callback=window.__jindo_callback._$3361_0&q={keyword}&q_enc=UTF-8&st=100&frm=nv&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&ans=2&run=2&rev=4&con=1"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
resp = requests.get(keyword_list)

diction_resp = literal_eval(resp.text[32:])

result = []
for i in range(len(diction_resp.get('items')[0])):
    result.append(diction_resp.get('items')[0][i][0])

print(result)