import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import requests
import xmltodict
import json
import io
import urllib.request
import chardet
from urllib import parse

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setStatusTip('나가기')
        exitAction.triggered.connect(qApp.quit)

        self.lbl = QLabel('개인통관고유부호  :', self)
        self.lbl2 = QLabel('      성        함       :', self)
        self.lineedit = QLineEdit(self)
        self.lineedit2 = QLineEdit(self)
        self.lbl.move(40, 20)
        self.lbl2.move(40, 60)
        self.lbl.resize(120, 20)
        self.lbl2.resize(120, 20)
        self.lineedit.move(170, 20)
        self.lineedit.resize(115, 20)
        self.lineedit2.move(170, 60)
        self.lineedit2.resize(115, 20)
        self.text = QTextBrowser(self)
        self.text.move(30, 100)
        self.text.resize(401, 192)

        btn1 = QPushButton('Confirm', self)
        btn2 = QPushButton('Reset', self)
        btn1.move(340, 20)
        btn1.resize(75, 23)
        btn2.move(340, 60)
        btn2.resize(75, 23)
        btn1.clicked.connect(self.personal)
        self.lineedit2.returnPressed.connect(btn1.click)
        btn2.clicked.connect(self.clear)

        self.setWindowTitle('개인통관부호 확인')
        self.setWindowIcon(QIcon('costoff.png'))
        self.setGeometry(300, 300, 460, 310)
        self.show()
    
    def personal(self):
        sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

        number = self.lineedit.text()

        name = self.lineedit2.text()

        unicode_name = u"{}".format(name)

        word = unicode_name

        url_tmp = "https://unipass.customs.go.kr:38010/ext/rest/persEcmQry/retrievePersEcm?crkyCn=o260w109d162t265i050m050k0&persEcm={0}&pltxNm=".format('P' + number)
        url = url_tmp + word

        resp = requests.get(url)

        rescode = resp.status_code

        if(rescode == 200):
            responseData = resp.text
            rD = xmltodict.parse(responseData)
            rDJ = json.dumps(rD)
            if (number == "") & (name == ""):
                reply = "내용을 적어주세요."
            elif (name == ""):
                reply = "이름을 적어주세요."
            elif (number == ""):
                reply = "개인통관고유부호를 적어주세요."
            else:
                if rDJ[-4] == '1':
                    reply = '해당 개인통관고유부호는 일치합니다.'
                    self.text.append("P{} | {} | 일치".format(number, name))
                else:
                    reply = '미일치합니다.'
                    self.text.append("P{} | {} | 미일치".format(number, name))
        buttonReply = QMessageBox.information(self, 'Confirm', reply)
    
    def clear(self):
        self.lineedit.setText("")
        self.lineedit2.setText("")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())