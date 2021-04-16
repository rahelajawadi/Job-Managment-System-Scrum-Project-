

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import finalMain
import userView
import Apply
import sqlite3

class Ui_UserTable(object):

    def setupUi(self, UserTable):
        UserTable.setObjectName("UserTable")
        UserTable.resize(1200, 750)
        UserTable.setStyleSheet("\n"
"\n"
"\n"
"QWidget #logout{\n"
"background-color:#3A75A8;\n"
"color:#fff;\n"
"}\n"
"\n"
"QWidget #btn_apply{\n"
"background-color: #5AAA78;\n"
"color:#f1f1f1;\n"
"}\n"
"\n"
"QWidget #btn_search{\n"
"background-color: #FB8739;\n"
"color:#f1f1f1;\n"
"}\n"
"\n"
"")
        UserTable.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(UserTable)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(80, 180, 1051, 451))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(1)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(174)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(15)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(25)
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(4, -1, 1191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: #5AAA78;\n"
"border:none;\n"
"color:#fff;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btn_apply = QtWidgets.QPushButton(self.centralwidget)
        self.btn_apply.setGeometry(QtCore.QRect(310, 80, 71, 41))
        self.btn_apply.setObjectName("btn_apply")

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
        UserTable.setCentralWidget(self.centralwidget)

        self.retranslateUi(UserTable)
        QtCore.QMetaObject.connectSlotsByName(UserTable)

        #Calling the methods
        self.btn_apply.clicked.connect(self.moveToApply)
        self.btn_apply.clicked.connect(lambda: self.closer(UserTable))

    def closer(self, UserTable):
        UserTable.hide()

    def moveToApply(self):
        self.window1 = QtWidgets.QMainWindow()
        self.secondUI = Apply.Ui_addCV()
        self.secondUI.setupUi(self.window1)
        self.window1.show()

    def retranslateUi(self, UserTable):
        _translate = QtCore.QCoreApplication.translate
        UserTable.setWindowTitle(_translate("UserTable", "tableWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("UserTable", "Job ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("UserTable", "Job Title"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("UserTable", "Organization"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("UserTable", "Job Detail"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("UserTable", "Announced At"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("UserTable", "Closed Date"))
        self.lineEdit.setPlaceholderText(_translate("UserTable", "search by ID"))
        self.logout.setText(_translate("UserTable", "logout"))
        self.btn_search.setText(_translate("UserTable", "search"))
        self.label.setText(_translate("UserTable", "Job Application Managment System"))
        self.btn_apply.setText(_translate("UserTable", "Apply"))
        self.btn_back.setText(_translate("UserTable", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserTable = QtWidgets.QMainWindow()
    ui = Ui_UserTable()
    ui.setupUi(UserTable)
    UserTable.show()
    sys.exit(app.exec_())
