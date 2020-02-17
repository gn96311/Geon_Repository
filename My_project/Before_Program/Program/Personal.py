import requests
import xmltodict
import json
import sys
import io
import urllib.request
import chardet
from urllib import parse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


number = str(input())

name = str(input())

unicode_name = u"{}".format(name)

utf_name = name.encode('utf-8')

word = unicode_name

url_tmp = "https://unipass.customs.go.kr:38010/ext/rest/persEcmQry/retrievePersEcm?crkyCn=o260w109d162t265i050m050k0&persEcm={0}&pltxNm=".format('P' + number)
url = url_tmp + word

resp = requests.get(url)

rescode = resp.status_code

if(rescode == 200):
    responseData = resp.text
    rD = xmltodict.parse(responseData)
    rDJ = json.dumps(rD)
    if rDJ[-4] == '1':
        print('해당 개인통관고유부호는 일치합니다.')
    else:
        print('미일치합니다.')