import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/dp/B07W6RPZVY/ref=sspa_dk_detail_4?psc=1&pd_rd_i=B07W6RPZVY&pd_rd_w=fzmO5&pf_rd_p=45a72588-80f7-4414-9851-786f6c16d42b&pd_rd_wg=wkDk1&pf_rd_r=1T5K1V76414JSCENQDDK&pd_rd_r=67a268a2-bfaa-421e-821b-b644514a6ce5&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFQNlpEM0ZJTTUxUFgmZW5jcnlwdGVkSWQ9QTAwNDM3OTkxM0FPVVhMTDdJQVQmZW5jcnlwdGVkQWRJZD1BMDIwMjcxMTJCSkNLRUlOSVRWTEwmd2lkZ2V0TmFtZT1zcF9kZXRhaWwmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'

soup = BeautifulSoup(requests.get(url).text, 'lxml')
price = soup.find("div", "a-section a-spacing-small").span.text

print(price)