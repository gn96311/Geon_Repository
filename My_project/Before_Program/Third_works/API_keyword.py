import os
import sys
import json
import urllib.request
from powernad.API import RelKwdStat
import sqlite3
import operator

# 네이버 강고 API 키
KWD_API_CUSTOMER_ID_ID = "1747603"
KWD_API_ACCESS_LICCENSE = "0100000000e144b59503fe498f66cb37d07d95d9b8054c475d53ff53ddd73adeca924d9a86"
KWD_API_SECRET_KEY = "AQAAAADhRLWVA/5Jj2bLN9B9ldm4zdUnLWKSJ1bxL+a7Bje1tA=="
KRW_API_URL = "https://api.naver.com"

# 네이버 광고 API
insert_keyword = str(input())
def naverKwdApi(keword):

    main_key = RelKwdStat.RelKwdStat(KRW_API_URL,KWD_API_ACCESS_LICCENSE, KWD_API_SECRET_KEY,KWD_API_CUSTOMER_ID_ID)

    kwdDataList = main_key.get_rel_kwd_stat_list(None, hintKeywords=keword, showDetail='1')

    keyword_dict = {}
    for outdata in kwdDataList:
        relKeyword = outdata.relKeyword  # 연관 키워드
        '''
        monthlyPcQcCnt = outdata.monthlyPcQcCnt  # 30일간 PC 조회수
        '''
        monthlyMobileQcCnt = outdata.monthlyMobileQcCnt  # 30일간 모바일 조회수
        if str(type(monthlyMobileQcCnt)) == "<class 'int'>":
            pass
        elif str(type(monthlyMobileQcCnt)) == "<class 'str'>":
            monthlyMobileQcCnt = int(10)
        '''
        monthlyAvePcClkCnt = outdata.monthlyAvePcClkCnt  # 4주간 평균 PC 클릭수
        monthlyAveMobileClkCnt = outdata.monthlyAveMobileClkCnt  # 4주간 평균 모바일 클릭수
        monthlyAvePcCtr = outdata.monthlyAvePcCtr  # 4주간 평균 PC 클릭율
        monthlyAveMobileCtr = outdata.monthlyAveMobileCtr  # 4주간 평균 모바일 클릭율
        plAvgDepth = outdata.plAvgDepth  # 4주간 평균 PC 광고수
        compIdx = outdata.compIdx  # PC 광고 기반 경쟁력
        '''
        keyword_dict[relKeyword] = monthlyMobileQcCnt
    sorted_keyword_dict = sorted(keyword_dict.items(), key=lambda x:x[1], reverse=True)
    print(sorted_keyword_dict)
 
naverKwdApi(insert_keyword)