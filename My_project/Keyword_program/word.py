from pandas import DataFrame, read_csv
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setStatusTip('나가기')
        exitAction.triggered.connect(qApp.quit)

        self.lbl = QLabel('Type_One', self)
        self.lbl2 = QLabel('Type_Two', self)
        self.lineedit = QLineEdit(self)
        self.lineedit2 = QLineEdit(self)
        self.lbl.move(310, 50)
        self.lbl2.move(310, 410)
        self.lbl.resize(120, 20)
        self.lbl2.resize(120, 20)
        self.lineedit.move(360, 780)
        self.lineedit.resize(160, 30)
        self.lineedit2.move(40, 780)
        self.lineedit2.resize(160, 30)
        self.text = QTextBrowser(self)
        self.text2 = QTextBrowser(self)
        self.text.move(30, 80)
        self.text.resize(600, 310)
        self.text2.move(30, 440)
        self.text2.resize(600, 310)

        btn1 = QPushButton('Confirm', self)
        btn2 = QPushButton('Reset', self)
        btn3 = QPushButton('To Excel', self)
        btn1.move(210, 780)
        btn1.resize(91, 31)
        btn2.move(530, 20)
        btn2.resize(91, 31)
        btn3.move(530, 780)
        btn3.resize(91, 31)
        btn1.clicked.connect(self.key)
        btn2.clicked.connect(self.clear)
        btn3.clicked.connect(self.to_excel)
        self.lineedit.returnPressed.connect(btn3.click)
        self.lineedit2.returnPressed.connect(btn1.click)

        self.setWindowTitle('키워드 확인')
        self.setWindowIcon(QIcon('costoff.png'))
        self.setGeometry(500, 150, 657, 830)
        self.show()

    def key(self):
        name = self.lineedit2.text()
        try:
            self.text.setText("")
            self.text2.setText("")
            data = read_csv('C:\keyword\Before\{}.csv'.format(name), encoding='euc-kr')
            type_one = (data['총 검색수'] >= 1000) & (data['상품수'] <= 15000) & (data['총 검색수'] >= data['상품수']) & (data['경쟁강도'] >= 0.5) & (data['경쟁강도'] <= 15)
            type_two = (data['총 검색수'] >= 1000) & (data['상품수'] <= 15000) & (data['경쟁강도'] >= 0.5) & (data['경쟁강도'] <= 15)
            self.text.append(str(data[type_one]))
            self.text2.append(str(data[type_two]))
        except FileNotFoundError:
            self.text.append("해당 이름을 가진 문서가 없습니다.")
            self.text2.append("해당 이름을 가진 문서가 없습니다.")
            pass
        
    def to_excel(self):
        after_name = self.lineedit.text()
        before_name = self.lineedit2.text()
        data = read_csv('C:\keyword\Before\{}.csv'.format(before_name), encoding='euc-kr')
        type_one = (data['총 검색수'] >= 1000) & (data['상품수'] <= 15000) & (data['총 검색수'] >= data['상품수']) & (data['경쟁강도'] >= 0.5) & (data['경쟁강도'] <= 15)
        type_two = (data['총 검색수'] >= 1000) & (data['상품수'] <= 15000) & (data['경쟁강도'] >= 0.5) & (data['경쟁강도'] <= 15)
        frame = DataFrame(data[type_one])
        frame_two = DataFrame(data[type_two])
        frame.to_csv('C:\keyword\After\{}_type_one.csv'.format(after_name), encoding="euc-kr")
        frame_two.to_csv('C:\keyword\After\{}_type_two.csv'.format(after_name), encoding="euc-kr")

    def clear(self):
        self.text.setText("")
        self.text2.setText("")
        self.lineedit.setText("")
        self.lineedit2.setText("")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())