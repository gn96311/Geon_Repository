import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import requests
import xmltodict
import json
import io
import urllib.request
import chardet
from urllib import parse

form_class = uic.loadUiType("Entry_program.ui")[0]

class WindowClass(QWidget, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.personal)

    def personal(self):
        sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

        number = self.lineedit.text()

        name = self.lineedit_2.text()

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
            if rDJ[-4] == '1':
                return('해당 개인통관고유부호는 일치합니다.')
            else:
                return('미일치합니다.')

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()