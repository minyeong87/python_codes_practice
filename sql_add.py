import pymysql
import sys
import csv
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("jeju.ui")[0]  # ui연결

class MainWindow(QMainWindow, form_class): #화면을 띄우는데 사용되는 Class 선언
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.table_widget_create()
        # self.btn_search.clicked.connect(self.search)
        self.btn_add.clicked.connect(self.add)


    def table_widget_create(self):
        conn = pymysql.connect(host='localhost', user='root', password='0000', db='jeju_project', charset='utf8')

        # Connection 으로부터 Cursor 생성
        cur = conn.cursor()

        # SQL문 실행
        sql = "select * from jeju_project.jeju_table"
        cur.execute(sql)

        # 데이타 Fetch
        self.rows = cur.fetchall()
        # list1 = list(rows)
        # list2 = []
        # for i in range(len(rows)):
        # #     list2.append()
        # print(list1)


        # print(list1)
        for i in range(len(self.rows)):
            for j in range(len(self.rows[i])):
                self.table.setItem(i, j, QTableWidgetItem(str(self.rows[i][j])))
        print(len(self.rows))

        conn.close()
    #
    # def search(self):
    #     search_name = self.lineEdit.text()
    #     search_result = []
    #
    #     for restaurant_name in self.rows:
    #         if search_name in restaurant_name[12] or search_name in restaurant_name:
    #             search_result.append(restaurant_name)
    #             self.table.clearContents()
    #             self.table.setRowCount(len(search_result))
    #             self.table.setColumnCount(len(search_result[0]))
    #     print(search_result)
    #     for i in range(len(search_result)):
    #         for j in range(len(search_result[i])):
    #             # i번째 줄의 j번째 칸에 데이터를 넣어줌
    #             self.table.setItem(i, j, QTableWidgetItem(search_result[i][j]))

    #
    def add(self):
        # pop_name = self.lineEdit.text()

        confu = pymysql.connect(host='localhost', user='root', password='0000', db='jeju_project',
                               charset='utf8')
        curr = confu.cursor()
        # print(pop_name)
        # SQL문 실행
        RS_name = self.lineEdit_RSname.text()
        Full_address = self.lineEdit_Address.text()
        Post = self.lineEdit_Post.text()

        curr.execute(f"INSERT INTO jeju_project.jeju_table(Restaurant_name,full_address,post) VALUES('{RS_name}', '{Full_address}', '{Post}')")
        curr.execute("select * from jeju_project.jeju_table")
        temp = curr.fetchall()
        confu.commit()
        print(temp)
        self.table.clearContents()
        for i in range(len(temp)):
            for j in range(len(temp[i])):

                self.table.setItem(i, j, QTableWidgetItem(str(temp[i][j])))
        print(len(temp))


        # for i in temp:
        #     print(i)
        # pop = f"DELETE FROM jeju_project.jeju_table WHERE Restaurant_name = {pop_name}"
        # print(pop)
        # curr.execute(sql, pop_name)
        # curr.commit()

        # after_pop = "select * from jeju_project.jeju_table"
        # curr.execute(after_pop)
        # pop_result = curr.fetchall()
        # print(pop_result)


        #
        # for i in range(len(popped)):
        #     for j in range(len(popped[i])):
        #         self.table.setItem(i, j, QTableWidgetItem(str(popped[i][j])))
        # print(len(self.rows))




    # def search(self):
    #     search_name = self.lineEdit.text()
    #     search_result = []
    #
    #     sql = "select * from jeju_project.jeju_table"
    #     cur.execute(sql)
    #
    #     for restaurant_name in self.rows:
    #         if search_name in restaurant_name[12] or search_name in restaurant_name:
    #             search_result.append(restaurant_name)
    #             self.table.clearContents()
    #             self.table.setRowCount(len(search_result))
    #             self.table.setColumnCount(len(search_result[0]))
    #     print(search_result)
    #     for i in range(len(search_result)):
    #         for j in range(len(search_result[i])):
    #             # i번째 줄의 j번째 칸에 데이터를 넣어줌
    #             self.table.setItem(i, j, QTableWidgetItem(search_result[i][j]))



        #
        # # Connection 닫기
        # conn.close()





if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    mainWindow = MainWindow()

    # 프로그램 화면을 보여주는 코드
    mainWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
