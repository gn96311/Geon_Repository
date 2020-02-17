import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import re
import requests
from bs4 import BeautifulSoup
from ast import literal_eval

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
        self.lineedit = QLineEdit(self)
        self.textedit = QTextEdit(self)
        self.lbl.move(50, 30)
        self.lbl2.move(50, 70)
        self.lineedit.move(165, 25)
        self.textedit.resize(500,190)
        self.textedit.move(50, 95)

        btn = QPushButton('Apply', self)
        btn.clicked.connect(self.find_keyword)
        btn.resize(150,30)
        btn.move(400, 22)
        self.lineedit.returnPressed.connect(btn.click)
        self.setWindowTitle('Find Keyword Program')
        self.setGeometry(300, 300, 600, 300)
        self.show()

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
        your_keyword = ','.join(result)
        

        self.textedit.setText(your_keyword)

        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Find_keyword()
    sys.exit(app.exec_())