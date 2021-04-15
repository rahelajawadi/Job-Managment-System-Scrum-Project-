from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import finalMain
import adminView

class Ui_MainWindow(object):
    def loadData(self):
            db = sqlite3.connect("jobs.db")
            query = "select * from jobInfo"
            res = db.execute(query)
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(res):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            db.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 750)
        MainWindow.setStyleSheet("QPushButton:hover{\n"
"background-color: #3A75A8;\n"
"border:none;\n"
"color:#fff;\n"
"}\n"
"\n"
"QWidget #btn_search{\n"
"background-color:#3A75A8;\n"
"color:#fff;\n"
"}\n"
"\n"
"QWidget #logout{\n"
"background-color:#3A75A8;\n"
"color:#fff;\n"
"}\n"
"\n"
"QWidget #btn_add{\n"
"background-color:#105687;\n"
"color:#f1f1f1;\n"
"}\n"
"\n"
"QWidget #btn_update{\n"
"background-color: #1BA160;\n"
"color:#f1f1f1;\n"
"}\n"
"\n"
"QWidget #btn_load{\n"
"background-color: #FB8739;\n"
"color:#f1f1f1;\n"
"}\n"
"\n"
"QWidget #btn_delete{\n"
"background-color: #DA4F43;\n"
"color:#f1f1f1;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(410, 180, 711, 451))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tableWidget.setFont(font)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(118)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(15)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(23)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 80, 131, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(1030, 80, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.logout.setFont(font)
        self.logout.setObjectName("logout")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(230, 80, 71, 41))
        self.btn_search.setObjectName("btn_search")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 180, 301, 451))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.title = QtWidgets.QLineEdit(self.groupBox)
        self.title.setGeometry(QtCore.QRect(60, 40, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.btn_update = QtWidgets.QPushButton(self.groupBox)
        self.btn_update.setEnabled(True)
        self.btn_update.setGeometry(QtCore.QRect(60, 340, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_update.setFont(font)
        self.btn_update.setMouseTracking(False)
        self.btn_update.setDefault(False)
        self.btn_update.setFlat(False)
        self.btn_update.setObjectName("btn_update")
        self.organization = QtWidgets.QLineEdit(self.groupBox)
        self.organization.setGeometry(QtCore.QRect(60, 90, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.organization.setFont(font)
        self.organization.setObjectName("organization")
        self.btn_add = QtWidgets.QPushButton(self.groupBox)
        self.btn_add.setEnabled(True)
        self.btn_add.setGeometry(QtCore.QRect(160, 290, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_add.setFont(font)
        self.btn_add.setMouseTracking(False)
        self.btn_add.setDefault(False)
        self.btn_add.setFlat(False)
        self.btn_add.setObjectName("btn_add")
        self.btn_delete = QtWidgets.QPushButton(self.groupBox)
        self.btn_delete.setGeometry(QtCore.QRect(160, 340, 81, 41))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_load = QtWidgets.QPushButton(self.groupBox)
        self.btn_load.setGeometry(QtCore.QRect(60, 290, 81, 41))
        self.btn_load.setObjectName("btn_load")
        self.details = QtWidgets.QLineEdit(self.groupBox)
        self.details.setGeometry(QtCore.QRect(60, 140, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.details.setFont(font)
        self.details.setObjectName("details")
        self.closed = QtWidgets.QDateEdit(self.groupBox)
        self.closed.setGeometry(QtCore.QRect(60, 240, 181, 31))
        self.closed.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 7), QtCore.QTime(0, 0, 0)))
        self.closed.setCalendarPopup(True)
        self.closed.setObjectName("closed")
        self.announced = QtWidgets.QDateEdit(self.groupBox)
        self.announced.setGeometry(QtCore.QRect(60, 190, 181, 31))
        self.announced.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 7), QtCore.QTime(0, 0, 0)))
        self.announced.setCalendarPopup(True)
        self.announced.setObjectName("announced")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(1030, 650, 85, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_apply")
        self.btn_back.setStyleSheet("background-color: #f1f1f1;\n"
                                    "border:none;\n"
                                    "color:#000;")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(4, -1, 1191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: #3A75A8;\n"
"border:none;\n"
"color:#fff;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Calling the methods
        self.loadData()
        self.logout.clicked.connect(lambda: self.closer(MainWindow))
        self.logout.clicked.connect(self.returnToMain)
        self.btn_back.clicked.connect(lambda: self.closer(MainWindow))
        self.btn_back.clicked.connect(self.moveToAdminView)
        self.btn_add.clicked.connect(self.addJob)

    def moveToAdminView(self):
            self.window1 = QtWidgets.QMainWindow()
            self.secondUI = adminView.Ui_jobSeekerLogin()
            self.secondUI.setupUi(self.window1)
            self.window1.show()

    def returnToMain(self):
            self.window1 = QtWidgets.QMainWindow()
            self.secondUI = finalMain.Ui_FirstWindow()
            self.secondUI.setupUi(self.window1)
            self.window1.show()

    def addJob(self):
            title = self.title.text()
            organization = self.organization.text()
            details = self.details.text()
            temp_var = self.announced.date()
            announced = temp_var.toPyDate()
            clz = self.closed.date()
            close = clz.toPyDate()

            # open the existing database
            db = sqlite3.connect("jobs.db")
            message1 = QMessageBox()

            if title == "":
                    message1.setText("Sorry, title field can't be empty !")
                    message1.setIcon(QMessageBox.Warning)
                    x = message1.exec_()
            else:
                    # insert a values into a database
                    db.execute("""INSERT INTO jobInfo(title, organization,details, open, close) VALUES(?,?,?,?,?)""",
                               (title, organization, details, announced, close))
                    db.commit()
                    message1.setText(organization + "'s job added successfully")
                    message1.setIcon(QMessageBox.Information)
                    x = message1.exec_()
                    self.loadData()
            self.title.clear()
            self.organization.clear()
            self.details.clear()

    def closer(self, MainWindow):
            MainWindow.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "tableWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Job ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Job Title"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Organization"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Job Detail"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Announced At"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Closed Date"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "search by ID"))
        self.logout.setText(_translate("MainWindow", "logout"))
        self.btn_search.setText(_translate("MainWindow", "search"))
        self.groupBox.setTitle(_translate("MainWindow", "Modify Jobs"))
        self.title.setPlaceholderText(_translate("MainWindow", "Job Title"))
        self.btn_update.setText(_translate("MainWindow", "Update"))
        self.organization.setPlaceholderText(_translate("MainWindow", "Organization "))
        self.btn_add.setText(_translate("MainWindow", "Add"))
        self.btn_delete.setText(_translate("MainWindow", "Delete"))
        self.btn_load.setText(_translate("MainWindow", "Edit "))
        self.details.setPlaceholderText(_translate("MainWindow", "Job Datails"))
        self.closed.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.announced.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.label.setText(_translate("MainWindow", "Job Application Managment"))
        self.btn_back.setText(_translate("UserTable", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
