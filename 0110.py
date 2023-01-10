import pymysql
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore

# ui파일 연결
form_class = uic.loadUiType("ui_jeju.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # ui 시작 인덱스 0으로 고정
        self.stackedWidget.setCurrentIndex(0)

        self.btn_home.clicked.connect(self.home)
        self.btn_search.clicked.connect(self.search1)
        #clendar 관련
        self.cal_widget.setGridVisible(True) #달력 숫자 사이에 줄 생기게 함
        self.cal_widget.clicked.connect(self.show_date) # 클릭시 연결
        # self.cal_widget.selectionChanged.connect(함수) # 날짜 변경 선택했을 시
        self.combo.activated[str].connect(self.combo_clicked)

    def search1(self):
        self.stackedWidget.setCurrentIndex(1)
        print(self.combo_selected, 'yes')
        print(self.selected_date, 'final1')
        
        conn = pymysql.connect(host='localhost', user='root', password='0000', db='jejudo', charset='utf8')   # password 변경 해주세요
        ## conn로부터  결과를 얻어올 때 사용할 Cursor 생성
        cur = conn.cursor()
        ## SQL문 실행
        sql = f"select * from jejudoweather where jijum_name = '{self.combo_selected}'"
        cur.execute(sql)
        print(cur.execute(sql))   # 실행(excute) 했더니 10884줄이 나온다.
        ## 데이타 Fetch

        # row = cur.fetchone()
        # print(row) # ('카페송키','일반음식점..) 한 행이 튜플형태로 나온다.
        self.region = cur.fetchall()
        conn.close()



    def home(self):
        self.stackedWidget.setCurrentIndex(0)

    def combo_clicked(self, text):
        print(text)
        # conn = pymysql.connect(host='localhost', user='root', password='0000', db='jejudo', charset='utf8')   # password 변경 해주세요
        # ## conn로부터  결과를 얻어올 때 사용할 Cursor 생성
        # cur = conn.cursor()
        # ## SQL문 실행
        # sql = f"select * from jejudoweather where jijum_name = '{text}'"
        # cur.execute(sql)
        # print(cur.execute(sql))   # 실행(excute) 했더니 10884줄이 나온다.
        # ## 데이타 Fetch
        # 
        # # row = cur.fetchone()
        # # print(row) # ('카페송키','일반음식점..) 한 행이 튜플형태로 나온다.
        # self.region = cur.fetchall()
        # conn.close()
        # print(rows) # 튜플안에 튜플로 전체 데이터를 불러온다.
        # self.table.setRowCount(len(rows)) # 테이블의 행 갯수를 rows의 길이로 정함
        # self.table.setColumnCount(len(rows[0])+1)  # 테이블의 열 갯수를 rows[0]의 길이로 정함

        # print(region)
        self.combo_selected = text

    def show_date(self, date):
        self.date_edit.setText(date.toString('yyyy년 MM월 dd일'))
        # b = self.cal_widget.selectedDate()
        # print(b)
        print(date.toString('MM-dd'), 'date')
        print(date, 'adf')
        self.selected_date = date.toString('MM-dd')







if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

