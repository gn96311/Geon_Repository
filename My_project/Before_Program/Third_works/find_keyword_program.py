import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import re
import requests
from bs4 import BeautifulSoup
from ast import literal_eval
import os
import json
import urllib.request
from powernad.API import RelKwdStat
import sqlite3
import operator

class Find_keyword(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setStatusTip('나가기')
        exitAction.triggered.connect(qApp.quit)

        self.lbl = QLabel('Insert Keyword: ', self)
        self.lbl2 = QLabel('Output Keyword :', self)
        self.lbl3 = QLabel('<광고 키워드: 모바일 조회수>', self)
        self.lbl4 = QLabel('<연관 검색어>', self)
        self.lbl5 = QLabel('<광고 키워드 단어>', self)
        self.lineedit = QLineEdit(self)
        self.textedit1 = QTextEdit(self)
        self.textedit2 = QTextEdit(self)
        self.textedit3 = QTextEdit(self)
        self.lbl.move(25, 30)
        self.lbl2.move(25, 70)
        self.lbl3.move(45, 110)
        self.lbl4.move(375, 110)
        self.lbl5.move(635, 110)
        self.lineedit.move(165, 25)
        self.textedit1.resize(250,190)
        self.textedit1.move(25, 130)
        self.textedit2.resize(250,190)
        self.textedit2.move(300, 130)
        self.textedit3.resize(250,190)
        self.textedit3.move(575, 130)

        btn = QPushButton('Apply', self)
        btn.clicked.connect(self.find_keyword)
        btn.resize(150,30)
        btn.move(400, 22)
        self.lineedit.returnPressed.connect(btn.click)
        self.setWindowTitle('Find Keyword Program')
        self.setGeometry(300, 300, 850, 350)
        self.show()
    
    def naver_keyword(self):
        # 네이버 광고 API 키
        keyword = self.lineedit.text()

        KWD_API_CUSTOMER_ID_ID = "1747603"
        KWD_API_ACCESS_LICCENSE = "0100000000e144b59503fe498f66cb37d07d95d9b8054c475d53ff53ddd73adeca924d9a86"
        KWD_API_SECRET_KEY = "AQAAAADhRLWVA/5Jj2bLN9B9ldm4zdUnLWKSJ1bxL+a7Bje1tA=="
        KRW_API_URL = "https://api.naver.com"

        main_key = RelKwdStat.RelKwdStat(KRW_API_URL,KWD_API_ACCESS_LICCENSE, KWD_API_SECRET_KEY,KWD_API_CUSTOMER_ID_ID)

        kwdDataList = main_key.get_rel_kwd_stat_list(None, hintKeywords=keyword, showDetail='1')

        # 네이버 광고 API
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
        '''
        sorted_keyword_dict = reversed(keyword_dict.items(), key=operator.itemgetter(1))
        '''
        return(keyword_dict)

    def find_keyword(self, words):
        keyword = self.lineedit.text()

        #Find keyword in naver search
        keyword_list = f"https://ac.search.naver.com/nx/ac?_callback=window.__jindo_callback._$3361_0&q={keyword}&q_enc=UTF-8&st=100&frm=nv&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&ans=2&run=2&rev=4&con=1"
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        resp = requests.get(keyword_list)
        diction_resp = literal_eval(resp.text[32:])

        result = []
        for i in range(len(diction_resp.get('items')[0])):
            result.append(diction_resp.get('items')[0][i][0])

        #Find keyword in naver related keyword
        url = f"https://search.shopping.naver.com/search/all.nhn?where=all&frm=NVSCTAB&query={keyword}"

        resp2 = requests.get(url)
        soup = BeautifulSoup(resp2.text, "html.parser")
        try:
            related_words = soup.find("div", {"class": "co_relation_srh"}).find_all("li")
        except AttributeError:
            related_words = []
        for i in related_words:
            first_words = (i.get_text()).rstrip('\n')
            second_words = (i.get_text()).strip()
            result.append(second_words)


        #Find keyword in Coupang
        coupang_keyword_list = f"https://www.coupang.com/np/search/autoComplete?callback=jQuery111108502009031661315_1573689468696&keyword={keyword}"
        resp3 = requests.get(coupang_keyword_list)
        diction = literal_eval(resp3.text[43:-2])
        try:
            for i in diction:
                result.append(i.get("keyword"))
        except AttributeError:
            pass
        result = set(result)
        '''
        your_keyword = ','.join(result)
        '''
        main_result = []
        sub_result = []
        only_main_result = []
        str_of_main_result = ""
        keyword_dict = self.naver_keyword()
        for keyword in result:
            if keyword in keyword_dict.keys():
                main_result.append([keyword,keyword_dict.get(keyword)])
            else: sub_result.append(keyword)
        main_result.sort(key=operator.itemgetter(1), reverse=True)
        for main_keyword in main_result:
            non_blank_keyword = str(main_keyword[0]).replace(" ","")
            only_main_result.append(non_blank_keyword)

        # main_result의 string화
        for insert_keyword in main_result:
            str_of_main_result += str(insert_keyword)
            str_of_main_result += ","
            str_of_main_result += "\n"
        #sub_result의 string화
        str_of_sub_result = ',\n'.join(sub_result)
        #only_main_result의 string화
        str_of_only_main_result = ',\n'.join(only_main_result)

        self.textedit1.setText(str_of_main_result)
        self.textedit2.setText(str_of_sub_result)
        self.textedit3.setText(str_of_only_main_result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Find_keyword()
    sys.exit(app.exec_())